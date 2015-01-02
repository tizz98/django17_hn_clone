from django.conf.urls import patterns, include, url
from django.contrib import admin
from links.views import LinkListView

urlpatterns = patterns('',
    url(r'^$', LinkListView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)