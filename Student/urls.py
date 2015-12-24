from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/(?P<index>[0-9]+)/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^agenda/(?P<index>[0-9]+)/$', views.agenda, name='agenda'),
    url(r'^favorite/$', views.favorite, name='favorite'),
    url(r'^teacher/(?P<selected>[0-9]+)/$', views.agenda, name='teacher'),
    url(r'^msg/', views.msg, name='msg'),
    url(r'^date/', views.date, name='date'),
]