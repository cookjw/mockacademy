from django.conf.urls import patterns, include, url
from app.views import shorten

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^shorten/$', shorten, name='shorten'),
    url(r'^(.*)', 'app.views.elsewhere', name='elsewhere'), 
    # url(r'^shrtd/(.*)', 'app.views.elsewhere', name='elsewhere'),    
)
