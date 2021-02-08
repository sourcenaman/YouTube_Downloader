import smtplib
from .youtube import Video
from django.shortcuts import render, redirect, reverse
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import mimetypes
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class Download():

    @classmethod
    def index(self, request):
        self.base_url = request.build_absolute_uri()
        template = 'youtube_downloader/index.html'
        context = {
            'form': True,
        }
        if request.method == 'POST':
            url = request.POST['url']
            self.video = Video(url)
            self.video.check()
            resolutions = self.video.resolution()
            context = {
                'resolutions': resolutions,
                'title': resolutions['Title'],
            }
            return render(request, template, context)
        return render(request, template, context)

    @classmethod
    def download(self, request):
        if request.method == 'POST':
            resolution = request.POST['resolution']
            self.download_thread = threading.Thread(
                target=self.video.download, args=(resolution,))
            self.download_thread.start()
            email = request.POST['email']
            title = self.video.title
            email_thread = threading.Thread(
                target=self.send_email, args=(email, title, self.base_url))
            email_thread.start()
            # return redirect("youtube_downloader:progress", token=request.POST['csrfmiddlewaretoken'])
            return redirect('youtube_downloader:index')

    @classmethod
    def send_email(self, email, title, base_url):
        self.download_thread.join()
        sender_email_id = 'ispythonmale@gmail.com'
        sender_email_id_password = 'IsPythonMale?'
        receiver_email_id = email
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, sender_email_id_password)
        msg = MIMEMultipart()
        html = base_url + "video/" + title
        msg.attach(MIMEText(html, 'html'))
        message = msg.as_string()
        s.sendmail(sender_email_id, receiver_email_id, message)
        s.quit()

    @classmethod
    def file_download(self, request, filename):
        fl_path = "downloads/" + filename + "/" + filename + ".mp4"
        fl = open(fl_path, 'rb')
        mime_type, _ = mimetypes.guess_type(fl_path)
        response = HttpResponse(fl, content_type=mime_type)
        response['Content-Disposition'] = f"attachment; filename={filename}.mp4"
        return response

    @classmethod
    @csrf_exempt
    def progress(self, request, token):
        template = 'youtube_downloader/index.html'
        context = {
            'token': token
        }
        if request.method == "POST":  # os request.GET()
            print('ajax called me')
            # Do your logic here coz you got data in `get_value`
            data = {}
            data['progress'] = self.video.liveprogress
            return HttpResponse(json.dumps(data), content_type="application/json")
        return render(request, template, context)
