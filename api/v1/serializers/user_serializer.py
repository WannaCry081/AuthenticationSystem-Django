from rest_framework import serializers
from api.v1.models import User

class UserSerializer(serializers.ModelSerializer):
  
  firstName = serializers.CharField(source = "first_name")
  lastName = serializers.CharField(source = "last_name")
  
  class Meta:
    
    model = User
    fields = ["id",
              "username",
              "email",
              "firstName",
              "lastName"]
