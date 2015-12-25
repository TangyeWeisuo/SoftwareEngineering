from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/(?P<current>[0-9]+)/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    # url(r'^agenda/(?P<index>[0-9]+)/$', views.agenda, name='agenda'),
    url(r'^favorite/$', views.favorite, name='favorite'),
    url(r'^teacher/(?P<selected>[0-9]+)/$', views.agenda, name='teacher'),
    url(r'^tmessage/(?P<selected>[0-9]+)/(?P<current>[0-9]+)/$', views.tmessage, name='tmessage'),
    url(r'^tboard/(?P<selected>[0-9]+)/(?P<current>[0-9]+)/$', views.tboard, name='tboard'),
    url(r'^tinfo/(?P<selected>[0-9]+)/$', views.tinfo, name='ttinfo'),
    url(r'^msg/(?P<current>[0-9]+)/$', views.msg, name='msg'),
    url(r'^date/$', views.date, name='date'),
    url(r'^search/$', views.recommend, name='search'),
    url(r'^information/$', views.choice_search, name='info'),
    url(r'^information/(?P<selected>[0-9]+)/$', views.teacher_information, name='tinfo'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^studentview/$', views.studentview, name='studentview'),

]