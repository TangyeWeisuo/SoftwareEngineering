from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/(?P<index>[0-9]+)/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
]