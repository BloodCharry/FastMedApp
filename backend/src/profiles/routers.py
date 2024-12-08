from .views import MyTokenObtainPairView, UserNetViewSet
from . import views

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.utils import extend_schema


# Объявление endpoint с документацией
class CustomTokenRefreshView(TokenRefreshView):
    pass


custom_token_refresh_view = CustomTokenRefreshView()


@extend_schema(tags=["auth"])
@extend_schema(
    description="Обновление токена доступа с использованием refresh токена",
    request=custom_token_refresh_view.get_serializer_class(),
    responses=custom_token_refresh_view.get_serializer_class()
)
class DocumentedTokenRefreshView(CustomTokenRefreshView):
    pass


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('profile/<int:pk>/', views.UserNetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('<int:pk>/', views.UserSetPublicViewSet.as_view({'get': 'retrieve'})),
    path('users/', UserNetViewSet.as_view({'get': 'list'})),

    path('token/refresh/', DocumentedTokenRefreshView.as_view(), name='token_refresh'),
    path('token/', views.MyTokenObtainPairView.as_view()),
]
