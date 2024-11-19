from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView, UserNetViewSet
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('profile/<int:pk>/', views.UserNetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('<int:pk>/', views.UserSetPublicViewSet.as_view({'get': 'retrieve'})),
    path('users/', UserNetViewSet.as_view({'get': 'list'})),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', views.MyTokenObtainPairView.as_view()),
    # path('login/', MyTokenObtainPairView.as_view()),
]
