from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'randify.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'landing.views.index', name='landing'),
    url(r'^auth/', include('access.urls', namespace='access')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^admin/', include(admin.site.urls)),
]
