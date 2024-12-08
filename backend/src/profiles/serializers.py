from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        if hasattr(user, 'patient'):
            token['username'] = user.username
            token['email'] = user.email
            token['first_name'] = user.patient.first_name
            token['last_name'] = user.patient.last_name
            token['avatar'] = str(user.patient.avatar)
            token['gender'] = user.patient.gender
            token['birthday'] = user.patient.birthday
            token['role'] = user.patient.role
            token['verified'] = user.patient.verified
        else:
            token['username'] = user.username
            token['email'] = user.email
            token['first_name'] = ''
            token['last_name'] = ''
            token['avatar'] = ''
            token['gender'] = ''
            token['birthday'] = ''
            token['role'] = ''
            token['verified'] = False

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = UserNet
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = UserNet.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
