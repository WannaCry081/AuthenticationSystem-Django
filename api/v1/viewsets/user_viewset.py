from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.v1.models import User
from api.v1.serializers import UserSerializer

class UserViewSet(viewsets.GenericViewSet, 
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin):
  
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def check_object_permissions(self, request, obj):
        if request.user.id != obj.id:
            raise AuthenticationFailed(
                detail = "Unauthorized access.")

        return super().check_object_permissions(request, obj)


    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
     