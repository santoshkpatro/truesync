from django.contrib.auth import authenticate
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .serializers import LoginSerializer, RegistrationSerializer, ProfileSerializer
from truesync.models.user import User


@api_view(['POST'])
def login_view(request):
    login_serializer = LoginSerializer(data=request.data)   

    if not login_serializer.is_valid():
        return Response(data={'detail': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

    login_credentials = login_serializer.data
    user = authenticate(**login_credentials)

    if not user:
        return Response(data={'detail': 'Either email or password is invalid'}, status=status.HTTP_401_UNAUTHORIZED)

    access_token = str(AccessToken.for_user(user))
    refresh_token = str(RefreshToken.for_user(user))

    return Response(data={'access_token': access_token, 'refresh_token': refresh_token}, status=status.HTTP_200_OK)


@api_view(['POST'])
def registration_view(request):
    registration_serializer = RegistrationSerializer(data=request.data)

    if not registration_serializer.is_valid():
        return Response(data={'detail': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

    registration_detail = registration_serializer.data

    email = registration_detail.get('email')

    try:
        User.objects.get(email=email)
        return Response(data={'detail': 'Account already exists with this email address'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        password = registration_detail.pop('password')
        confirm_password = registration_detail.pop('confirm_password')

        if not password == confirm_password:
            return Response(data={'detail': 'Password and confirm password is not same'}, status=status.HTTP_400_BAD_REQUEST)
        
        new_user = User(**registration_detail)
        new_user.set_password(password)
        new_user.save()
        
        return Response(data={'detail': 'Registration successfull'}, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        logged_in_user = self.request.user
        return logged_in_user