from django.conf.urls import include, url
from django.contrib import admin

from access import views as access_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'randify.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^uber/$', access_views.uber_handler, name='uber')
]
