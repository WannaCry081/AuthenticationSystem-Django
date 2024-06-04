from bleach import clean
from rest_framework import serializers
from rest_framework.exceptions import (ParseError,
                                       AuthenticationFailed)
from api.v1.models import User


class RegisterSerializer(serializers.ModelSerializer):

    firstName = serializers.CharField(
                        required = True,
                        source = "first_name")    
    lastName = serializers.CharField(
                        required = True,
                        source = "last_name")    
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
                  "firstName",
                  "lastName",
                  "email",
                  "password",
                  "rePassword"]
        extra_kwargs = {
            "id" : { "read_only" : True }
        }

    
    def validate(self, attrs):
        
        fields = ["username", "first_name", "last_name",
                  "email", "password", "rePassword"]
        
        if not all(field in attrs for field in fields):
            raise ParseError(
                    detail = "Invalid request. Please try again.")
        
        if attrs["password"] != attrs["rePassword"]:
            raise AuthenticationFailed(
                detail = "Credentials does not match. Please try again.")
        
        attrs["username"] = clean(attrs.get("username"))
        attrs["first_name"] = clean(attrs.get("first_name"))
        attrs["last_name"] = clean(attrs.get("last_name"))
        attrs["password"] = clean(attrs.get("password"))
        
        attrs.pop("rePassword")
        return attrs
