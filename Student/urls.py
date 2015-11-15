from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^homepage/(?P<index>[0-9]+)$', views.student_homepage, name='homepage'),
    url(r'^register/$', views.registerIndex, name='register'),
    url(r'^login/$', views.loginIndex, name='login'),
    url(r'^reg$', views.register, name='reg'),
    url(r'^log$', views.login, name='log'),
]