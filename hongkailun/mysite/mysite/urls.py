from django.conf.urls import patterns, include, url

from django.contrib import admin
from system.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^recommend/',recommend),
    url(r'^information/',teacher_imformation),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
