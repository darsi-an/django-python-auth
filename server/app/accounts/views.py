from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, LoginSerializer

# Django passses request data to SignupView which attempts to create a new user with UserSerializer
class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# View for login
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
