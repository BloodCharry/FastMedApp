from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import GoogleSocialAuthSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema(tags=["social_auth"])
@extend_schema_view(
    post=extend_schema(
        summary="Авторизация через Google",
    ),
)
class GoogleSocialAuthView(GenericAPIView):
    """ Social Auth with google """

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """
        POST with "auth_token"

        Send an idtoken as from google to get user information

        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response(data, status=status.HTTP_200_OK)
