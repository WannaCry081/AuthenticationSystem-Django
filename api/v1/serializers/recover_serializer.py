from rest_framework import serializers


class ForgotPasswordSerializer(serializers.Serializer):
    
    email = serializers.EmailField(
                    required = True)


class ResetPasswordSerializer(serializers.Serializer):
    
    email = serializers.EmailField(
                    required = True)
    resetCode = serializers.CharField(
                    required = True)
    newPassword = serializers.CharField(    
                    required = True)
