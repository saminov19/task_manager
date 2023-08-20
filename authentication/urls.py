from django.urls import path
from .views import user_registration, user_login, token_refresh, token_verify

urlpatterns = [
    path('register/', user_registration, name='user_registration'),
    path('login/', user_login, name='user_login'),
    path('refresh-token/', token_refresh, name='token_refresh'),
    path('verify-token/', token_verify, name='token_verify'),
]