from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('overview', views.overview, name='overview'),
    path('welcome', views.welcome, name='welcome'),
    path('logout', views.logoutUser, name='logout'),
    path('upload', views.upload, name='upload'),
    path('uploadDownload', views.uploadDownload, name='uploadDownload'),
    path('tech', views.tech, name='tech'),
    path('listAccounts', views.listAccounts, name='listAccounts'),
    path('addUser', views.addUser, name='addUser'),
    path('test', views.test, name='test'),
    path('reportUpload', views.reportUpload, name='reportUpload'),

    path('dp', views.dp),
    path('dpw', views.dpw)



]
