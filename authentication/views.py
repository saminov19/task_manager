from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, TokenRefreshSerializer
from django.http import HttpRequest


@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration(request):
    if request.method == 'POST':
        if isinstance(request, HttpRequest):
            data = request.data
        else:
            data = request.data

        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class CustomObtainJSONWebToken(TokenObtainPairView):
    serializer_class = UserLoginSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    return CustomObtainJSONWebToken.as_view()(request)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def token_refresh(request):
    if request.method == 'POST':
        if isinstance(request, HttpRequest):
            data = request.data
        else:
            data = request.data

        serializer = TokenRefreshSerializer(data=data)
        if serializer.is_valid():
            return TokenRefreshView.as_view()(request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def token_verify(request):
    if request.method == 'POST':
        return TokenVerifyView.as_view()(request)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
