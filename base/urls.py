from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('overview/<str:pk>/', views.overview, name='overview'),
    path('welcome', views.welcome, name='welcome'),
    path('logout', views.logoutUser, name='logout'),
    path('upload', views.upload, name='upload'),
    path('uploadDownload', views.uploadDownload, name='uploadDownload'),
    path('tech', views.tech, name='tech'),
    path('listAccounts', views.listAccounts, name='listAccounts'),
    path('dataOverview', views.dataOverview, name='dataOverview'),
    path('addUser', views.addUser, name='addUser'),
    path('addAccount', views.addAccount, name='addAccount'),
    path('test', views.test, name='test'),
    path('DataCollection/<str:pk>/', views.dataCollection, name='dataCollection'),
    path('FinalPack/<str:pk>/', views.finalPack, name='finalPack'),
    path('businessUnits/<str:pk>/', views.businessUnits, name='businessUnits'),
    path('tech/deleteUser/<str:pk>/', views.deleteUser, name='deleteUser'),


    path('dp', views.dp),
    path('overview/<str:pk>/dpw', views.dpw)



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
