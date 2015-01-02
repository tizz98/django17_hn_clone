from django.conf.urls import patterns, include, url
from django.contrib import admin
from links.views import LinkListView, UserProfileDetailView, UserProfileEditView
from django.contrib.auth.decorators import login_required as auth

urlpatterns = patterns('',
    url(r'^$', LinkListView.as_view(), name='home'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name="login"),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name="logout"),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name='profile'),
	url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),

    url(r'^admin/', include(admin.site.urls)),
)