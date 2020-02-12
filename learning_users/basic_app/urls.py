from django.conf.urls import url
from . import views

# Template urls

app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^special/$', views.special, name='special')
]