import os
import random

from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from ..profiles.models import UserNet as User


def generate_username(name):
    username = "".join(name.split(' ')).lower()
    while User.objects.filter(username=username).exists():
        username = username + str(random.randint(0, 1000))
    return username


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(
                email=email, password=os.environ.get('GOOGLE_CLIENT_SECRET')
            )
            if registered_user is None:
                raise AuthenticationFailed(detail='Invalid credentials')

            return {
                'username': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens()}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'username': generate_username(name), 'email': email,
            'password': os.environ.get('GOOGLE_CLIENT_SECRET')}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=os.environ.get('GOOGLE_CLIENT_SECRET'))
        return {
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens()
        }
