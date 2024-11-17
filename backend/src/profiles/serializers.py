from rest_framework import serializers
from .models import UserNet, Patient, Doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(required=False)  # Вложенный сериализатор

    class Meta:
        model = Patient
        fields = '__all__'


class GetUserNetSerializer(serializers.ModelSerializer):
    """
    Вывод инфо о user
    """
    profile = PatientSerializer(required=False)

    class Meta:
        model = UserNet
        exclude = ('last_login',
                   'password',
                   'is_staff',
                   'email',
                   'is_superuser',
                   'groups',
                   'user_permissions'
                   )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """
    Вывод публичной инф о user
    """
    profile = PatientSerializer(required=False)

    class Meta:
        model = UserNet
        exclude = (
            'email',
            'last_login',
            'password',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )
