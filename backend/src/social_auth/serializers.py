import os
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from . import google
from .register import register_social_user


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)

        if not user_data:
            raise serializers.ValidationError("The token is invalid or expired. Please login again")

        if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(provider=provider, name=name, email=email, user_id=user_id)
