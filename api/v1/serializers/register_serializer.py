from rest_framework import serializers
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
                  "password"
                  "rePassword"]
        extra_kwargs = {
            "id" : { "read_only" : True }
        }
