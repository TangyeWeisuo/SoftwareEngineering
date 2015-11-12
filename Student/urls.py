from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^homepage/(?P<index>[0-9]+)$', views.student_homepage, name='homepage'),
]