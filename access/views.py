from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

import requests


def uber_handler(request):
    if not 'code' in request.GET:
        return redirect(reverse('landing'))

    data = {
        'redirect_uri': '{0}{1}'.format(settings.APP_URL, reverse('access:uber')),
        'code': request.GET.get('code', None),
        'grant_type': 'authorization_code'
    }

    response = requests.post(
        'https://login.uber.com/oauth/token',
        auth=(
            settings.UBER_CLIENT_ID,
            settings.UBER_CLIENT_SECRET,
        ), 
        data=data
    )
    
    json_response = response.json()

    return redirect(
        "{base_url}?access_token={access_token}&type={token_type}&scope={scope}".format(**{
            'base_url': '/',
            'access_token': json_response.get('access_token'),
            'scope': json_response.get('scope'),
            'token_type': json_response.get('token_type')
        })
    )