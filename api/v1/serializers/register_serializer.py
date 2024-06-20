from bleach import clean
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from api.v1.models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
                        required = True,
                        write_only = True)
    rePassword = serializers.CharField(
                        required = True,
                        write_only = True)
    
    class Meta:
        
        model = User
        fields = ["id",
                  "username",
                  "email",
                  "password",
                  "rePassword"]
        extra_kwargs = {
            "id" : { "read_only" : True }
        }

    
    def validate(self, attrs):

        if attrs["password"] != attrs["rePassword"]:
            raise AuthenticationFailed(
                detail = "Credentials does not match. Please try again.")
        
        attrs["username"] = clean(attrs.get("username"))
        attrs["email"] = clean(attrs.get("email"))
        attrs["password"] = clean(attrs.get("password"))
        
        attrs.pop("rePassword")
        return attrs


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
