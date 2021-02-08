import moviepy.editor as mpe
from pytube import YouTube
import pytube
import os


class Video():

    previousprogress = 0
    liveprogress = 0
    title = ''

    def __init__(self, url):
        if url:
            self.url = url
        else:
            raise ValueError("Please enter a video url")

    def check(self):
        try:
            self.video_obj = YouTube(
                self.url, on_progress_callback=self.on_progress)
            self.title = ''.join(
                [i for i in self.video_obj.title if i.isalnum()])
        except pytube.exceptions.RegexMatchError:
            raise ValueError('Please check the URL')
        except pytube.exceptions.LiveStreamError:
            raise ValueError('Video is streaming live and cannot be loaded.')
        except pytube.exceptions.VideoPrivate:
            raise ValueError('This is a private video.')
        except pytube.exceptions.RecordingUnavailable:
            raise ValueError(
                'This video does not have a live stream recording available.')
        except pytube.exceptions.MembersOnly:
            raise ValueError("This is a member's only video.")
        except pytube.exceptions.VideoRegionBlocked:
            raise ValueError("This video is not available in your region.")

    def resolution(self):
        types = self.video_obj.streams.filter(file_extension='mp4')
        self.streams = {}
        self.streams["Title"] = self.video_obj.title
        for stream in types:
            if stream.mime_type == "audio/mp4":
                self.streams["audio"] = {}
                self.streams["audio"]["itag"] = stream.itag
                self.streams["audio"]["progressive"] = stream.is_progressive
                self.streams["audio"]["url"] = stream.url
                continue
            if stream.is_progressive:
                self.streams[stream.resolution] = {}
                self.streams[stream.resolution]["itag"] = stream.itag
                self.streams[stream.resolution]["progressive"] = stream.is_progressive
                self.streams[stream.resolution]["url"] = stream.url
                continue
            if stream.resolution not in self.streams.keys():
                self.streams[stream.resolution] = {}
                self.streams[stream.resolution]["itag"] = stream.itag
                self.streams[stream.resolution]["progressive"] = stream.is_progressive
                continue

        return self.streams

    def download(self, choice):
        if self.streams[choice]["progressive"] == True:
            self.download_files("video", choice)
        elif self.streams[choice]["progressive"] == False and choice == "audio":
            self.download_files("audio", choice)
        else:
            print("You have selected a choice which is an adaptive stream.\nThat means YouTube keeps the audio and video files separated for adaptive.\nBut don't worry I got you.\nThis can take some time so sit back and relax.")
            self.download_files("both", choice)
            self.merge_files()

    def download_files(self, type, choice):
        if type == "video" or type == "audio":
            self.video_obj.streams.get_by_itag(
                self.streams[choice]["itag"]).download()
        if type == "both":
            self.video_obj.streams.get_by_itag(
                self.streams[choice]["itag"]).download(filename=f'video{self.title}', output_path=f'downloads/{self.title}')
            self.video_obj.streams.get_by_itag(
                self.streams["audio"]["itag"]).download(filename=f'audio{self.title}', output_path=f'downloads/{self.title}')

    def merge_files(self):
        video_name = 'video' + self.title + '.mp4'
        audio_name = 'audio' + self.title + '.mp4'
        video = mpe.VideoFileClip(
            f'downloads/{self.title}/{video_name}')
        audio = mpe.AudioFileClip(
            f'downloads/{self.title}/{audio_name}')
        out = video.set_audio(audio)
        out.write_videofile(
            f'downloads/{self.title}/{self.title}.mp4')
        os.remove(
            f'downloads/{self.title}/{video_name}')
        os.remove(
            f'downloads/{self.title}/{audio_name}')

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining

        self.liveprogress = (int)(bytes_downloaded / total_size * 100)
        if self.liveprogress > self.previousprogress:
            self.previousprogress = self.liveprogress
        elif self.liveprogress == 100:
            self.previousprogress = 0
