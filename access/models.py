from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

import requests


class User(AbstractUser):
	access_token = models.CharField(max_length=128)
	token_type = models.CharField(max_length=200)
	scope = models.CharField(max_length=100)

	@classmethod
	def create_from_uber(klass, access_token, token_type, scope, *args, **kwargs):
		response = requests.get(
			'https://api.uber.com/v1/me',
			headers={
				'Authorization': '{0} {1}'.format(token_type, access_token)
			}
		)

		json_response = response.json()

		user, created = klass.objects.get_or_create(
			username=json_response.get('email'),
			email=json_response.get('email'),
			defaults={
				'first_name': json_response.get('first_name'),
				'last_name': json_response.get('last_name'),
				'access_token': access_token,
				'token_type': token_type,
				'scope': scope
			}
		)

		if not created:
			user.access_token = access_token
			user.token_type = token_type
			user.scope = scope
			user.save()

		return user, created



