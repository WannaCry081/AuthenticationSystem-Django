from rest_framework import viewsets, mixins
from api.v1.models import User
from api.v1.serializers import UserSerializer

class UserViewSet(viewsets.GenericViewSet, 
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin):
  
  queryset = User.objects.all()
  serializer_class = UserSerializer