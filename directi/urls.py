from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'directi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^chefeditor/', include('chefeditor.urls', namespace="chefeditor")),
    url(r'^admin/', include(admin.site.urls)),
)
