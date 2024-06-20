from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from api.v1.models import User


class LoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField(
                    required = True)
    password = serializers.CharField(
                    required = True)

    
    def validate(self, attrs):

        user = User.objects.get(email = attrs.get("email"))
        if not check_password(attrs.get("password"), 
                              user.password):
            raise AuthenticationFailed(
                    detail = "Invalid credentials. Please try again.")
        
        attrs["user"] = user
        return attrs