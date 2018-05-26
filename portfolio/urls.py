from django.conf.urls import url
from portfolio import views

urlpatterns = [
	url(r'^$', views.home_page, name="home_page"),
	url(r'^projects/$', views.projects, name="projects"),
	url(r'^contact_me/$', views.contact_me, name="contact_me"),
]