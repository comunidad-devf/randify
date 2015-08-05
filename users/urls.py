from django.conf.urls import include, url
from django.contrib import admin
from users import views as users_views

urlpatterns = [
    url(r'^(?P<user_id>\d{1,})/', users_views.profile, name='profile'),
]
