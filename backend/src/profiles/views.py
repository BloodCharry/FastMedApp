from django.shortcuts import redirect
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics, status
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import UserNet
from .serializers import (GetUserNetSerializer,
                          GetUserNetPublicSerializer,
                          MyTokenObtainPairSerializer,
                          RegisterSerializer)


@extend_schema(tags=["users"])
@extend_schema_view(
    retrieve=extend_schema(
        summary="Публичный вывод информации о пользователе",
    ),
)
class UserSetPublicViewSet(ModelViewSet):
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["users"])
@extend_schema_view(
    retrieve=extend_schema(
        summary="Вывод информации авторизированному пользователю",
    ),
    update=extend_schema(
        summary="Изменение информации авторизированного пользователя"
    ),
)
class UserNetViewSet(ModelViewSet):
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@extend_schema(tags=["users"])
@extend_schema_view(
    post=extend_schema(
        summary="Регистрация пользователя",
    ),
)
class RegisterView(generics.CreateAPIView):
    queryset = UserNet.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     if response.status_code == status.HTTP_201_CREATED:
    #         return redirect('login')
    #     return response



