from rest_framework import serializers
from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """
    Вывод инфо о user
    """

    class Meta:
        model = UserNet
        exclude = ('last_login',
                   'password',
                   'phoneNumber',
                   'is_active',
                   'is_staff',
                   'is_superuser',
                   'groups',
                   'user_permissions'
                   )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """
    Вывод публичной инф о user
    """

    class Meta:
        model = UserNet
        exclude = (
            'email',
            'phoneNumber',
            'last_login',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )
