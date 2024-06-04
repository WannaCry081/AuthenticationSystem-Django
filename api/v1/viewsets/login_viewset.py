from rest_framework import viewsets, mixins
from rest_framework.response import Response
from api.v1.serializers import LoginSerializer


class LoginViewSet(viewsets.GenericViewSet, 
                   mixins.CreateModelMixin):


    serializer_class = LoginSerializer


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
