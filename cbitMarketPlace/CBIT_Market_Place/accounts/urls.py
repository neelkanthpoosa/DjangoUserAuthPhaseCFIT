from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout

app_name="accounts"


urlpatterns=[
    url(r'^$',views.home),
    url(r'^login/$',login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$',logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$',views.register,name='register'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),

]
