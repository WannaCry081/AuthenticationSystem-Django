from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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
    throttle_classes = [UserRateThrottle]
    
    
    def check_object_permissions(self, request, obj):
        if request.user.id != obj.id:
            raise AuthenticationFailed(
                detail = "Unauthorized access.")

        return super().check_object_permissions(request, obj)
    
    @swagger_auto_schema(
        operation_summary = "Retrieve authenticated user profile.",
        operation_description = "This endpoint return the user profile of a authenticated user base on the path parameter.",
        responses = {
            status.HTTP_200_OK : openapi.Response("Ok"),
            status.HTTP_403_FORBIDDEN : openapi.Response("Authentication Failed"),
            status.HTTP_404_NOT_FOUND : openapi.Response("Not Found"),
            status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Internal Server Error"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve the authenticated user profile.

        Args:
            request (Request): The request object containing user information.

        Returns:
            Response: The response object containing the user profile data or error message.
        """
        return super().retrieve(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_summary = "Updates the user profile.",
        operation_description = "This endpoint updates the authenticated user profile.",
        responses = {
            status.HTTP_200_OK : openapi.Response("Ok"),
            status.HTTP_400_BAD_REQUEST : openapi.Response("Bad Request"),
            status.HTTP_403_FORBIDDEN : openapi.Response("Authentication Failed"),
            status.HTTP_404_NOT_FOUND : openapi.Response("Not Found"),
            status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Internal Server Error"),
        }
    )
    def update(self, request, *args, **kwargs):
        """
        Update the authenticated user profile.

        Args:
            request (Request): The request object containing user information.

        Returns:
            Response: The response object containing the update status or error message.
        """
        return super().update(request, *args, **kwargs)


    @swagger_auto_schema(
        operation_summary = "Removes an authenticated user.",
        operation_description = "This endpoint remove the authenticated user data.",
        responses = {
            status.HTTP_200_OK : openapi.Response("Ok"),
            status.HTTP_403_FORBIDDEN : openapi.Response("Authentication Failed"),
            status.HTTP_404_NOT_FOUND : openapi.Response("Not Found"),
            status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Internal Server Error"),
        }
    )
    def delete(self, request, *args, **kwargs):
        """
        Remove the authenticated user data.

        Args:
            request (Request): The request object containing user information.

        Returns:
            Response: The response object containing the deletion status or error message.
        """
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
