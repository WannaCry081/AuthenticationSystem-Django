from rest_framework import viewsets, mixins
from rest_framework.response import Response
from api.v1.serializers import RegisterSerializer


class RegisterViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin):


    serializer_class = RegisterSerializer


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
