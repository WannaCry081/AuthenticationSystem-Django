from rest_framework import serializers
from rest_framework.exceptions import (ParseError,
                                       AuthenticationFailed)
from api.v1.models import User
from api.v1.utils import CodeGenerator


class ForgotPasswordSerializer(serializers.Serializer):
    
    email = serializers.EmailField(
                    required = True)

    def validate(self, attrs):
        
        if "email" not in attrs:
            raise ParseError(
                detail = "Invalid request. Please try again.")
            
        user = User.objects.get(email = attrs.get("email"))
        code : str = CodeGenerator()
        if not user:
            raise AuthenticationFailed(
                detail = "Invalid credentials. Please try again.")
        
        user.reset_code = code
        user.save()        
    
        attrs["user"] = user
        return attrs


class ResetPasswordSerializer(serializers.Serializer):
    
    email = serializers.EmailField(
                    required = True)
    resetCode = serializers.CharField(
                    required = True)
    newPassword = serializers.CharField(    
                    required = True)
