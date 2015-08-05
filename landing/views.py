from django.shortcuts import render

from django.conf import settings

def index(request):
	return render(request, 'landing/index.html', {
		'uber_client_id': settings.UBER_CLIENT_ID,
		'uber_redirect_url': settings.UBER_REDIRECT_URL
	})
