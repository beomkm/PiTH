from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.log_list, name='log_list'),
	url(r'^register/', views.register, name='register'),
	url(r'^clear/', views.clear, name='clear'),
]
