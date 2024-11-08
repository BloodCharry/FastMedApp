from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions

from .models import UserNet
from .serializers import GetUserNetSerializer


@extend_schema(tags=["users"])
@extend_schema(summary="Получить информацию о пользователе")
class GetUserNetView(RetrieveAPIView):
    """ Вывод инфо о user """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer


class UpdateUserNetView(UpdateAPIView):
    """ Редактирование пользователя """
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """ Редактирование только авторизованного пользователя """
        return UserNet.objects.filter(id=self.request.user.id)
