from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xiangmu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$','haha.views.login'),
    url(r'^apd/$','haha.views.apd'),
    url(r'^append/$','haha.views.append'),
    url(r'^enterin/$','haha.views.enterin'),

)
