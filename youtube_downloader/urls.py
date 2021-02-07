from django.urls import path
from . import views

app_name = 'youtube_downloader'
urlpatterns = [
    path('', views.Download.index, name='index'),
    path('download/', views.Download.download, name='download'),
    path('progress/<str:token>', views.Download.progress, name='progress'),
    path('video/<str:filename>/', views.Download.file_download, name='file_download'),
]
