from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer


@extend_schema(tags=["public_users"])
@extend_schema_view(
    retrieve=extend_schema(
        summary="Публичный вывод информации о пользователе",
    ),
)
class UserSetPublicViewSet(ModelViewSet):
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["auth_users"])
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