from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
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
    
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


    @action(methods = ["GET"], detail = False) 
    def me(self, request, id = None):
        try:
            data = UserSerializer(request.user).data
            return Response(data, status = status.HTTP_200_OK)
        
        except:
            return Response({
                "detail": "Internal Server Error"
            }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
