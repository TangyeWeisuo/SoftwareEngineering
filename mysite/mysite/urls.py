from django.conf.urls import patterns, include, url

from django.contrib import admin
from system.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^search/',recommend),
    url(r'^information/$',choice_search),
    url(r'^information/(\S+)/$',teacher_imformation),    
    #url(r'^lab_teachers/',lab_teachers),    
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
