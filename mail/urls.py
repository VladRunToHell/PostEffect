from django.urls import path
from . import views


urlpatterns = [
    path('', views.Login, name='login'),
    path('mail/', views.Mail, name='mail'),
    path('razv/', views.razv, name='razv'),
    path('korO/', views.kor, name='korO'),
    path('chit/', views.chit, name='chit'),
    path('rass/', views.rass, name='rass'),
    path('spam/', views.spam, name='spam'),
    path('kor0/', views.kor2, name='kor0'),
]
