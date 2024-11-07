from rest_framework import serializers
from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """
    Вывод инфо о user
    """

    class Meta:
        model = UserNet
        exclude = ('last_login', 'password', 'is_active', 'is_staff', 'is_superuser')
