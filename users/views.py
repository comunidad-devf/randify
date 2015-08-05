from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from access.models import User

import json


def profile(request, user_id):
	user = get_object_or_404(User, id=user_id)
	return HttpResponse(json.dumps({
		'id': user.id,
		'username': user.username,
		'email': user.email
	}))