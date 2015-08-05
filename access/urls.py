from django.conf.urls import include, url
from django.contrib import admin

from access import views as access_views

urlpatterns = [
    url(r'^uber/$', access_views.uber_handler, name='uber')
]
