from rest_framework import serializers
from truesync.models.user import User


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.CharField()
    full_name = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'full_name',
            'profile',
            'profile_url'
        ]
        extra_kwargs = {
            'email': {
                'read_only': True
            },
            'profile_url': {
                'read_only': True
            },
            'profile': {
                'write_only': True
            }
        }