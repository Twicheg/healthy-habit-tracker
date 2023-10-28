from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import UserListApiView, UserCreateApiView, UserDestroyApiView

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserListApiView.as_view(), name='users_list'),
    path('users/create', UserCreateApiView.as_view(), name='user_create'),
    path('users/delete', UserDestroyApiView.as_view(), name='user_destroy'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
