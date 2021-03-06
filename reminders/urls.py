from django.conf.urls import patterns, url

from reminders import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logged-in/$', views.user_logged_in, name='logged-in'),
	url(r'^home/$', views.home, name='home'),
	url(r'^account/$', views.account, name='account'),
	url(r'^about/$', views.about, name='about'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout")
)

