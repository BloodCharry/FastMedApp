from rest_framework.generics import RetrieveAPIView
from .models import UserNet

from .serializers import GetUserNetSerializer


class GetUserNetView(RetrieveAPIView):
    """ Вывод инфо о user """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer
