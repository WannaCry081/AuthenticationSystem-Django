from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import (ParseError,
                                       AuthenticationFailed)
from rest_framework.throttling import AnonRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken
from api.v1.serializers import LoginSerializer


class LoginViewSet(viewsets.GenericViewSet, 
                   mixins.CreateModelMixin):
    """
    A viewset for logging in a user. This viewset returns access and refresh tokens for authenticated users.
    """


    serializer_class = LoginSerializer
    throttle_classes = [AnonRateThrottle]


    @swagger_auto_schema(
        operation_summary = "Logs in a user.",
        operation_description = "This endpoint returns the access and refresh token for authenticated users.",
        responses = {
            status.HTTP_200_OK: openapi.Response("Ok"),
            status.HTTP_400_BAD_REQUEST: openapi.Response("Bad Request"),
            status.HTTP_403_FORBIDDEN: openapi.Response("Forbidden"),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response("Internal Server Error")
        }
    )
    def create(self, request, *args, **kwargs):
        """
        This endpoint logs in a user and returns the JWT Token.

        Args:
            request: The HTTP request containing the user credentials.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Response object containing the JWT tokens or an error message.
        """
        try:
            serializer = self.get_serializer(data = request.data)
            serializer.is_valid(raise_exception = True)

            user = serializer.validated_data.get("user")
            token = RefreshToken.for_user(user)

            return Response({
                "access" : str(token.access_token),
                "refresh" : str(token)
            }, status = status.HTTP_200_OK)

        except ParseError as e:
            return Response({
                "detail" : str(e)
            }, status = status.HTTP_400_BAD_REQUEST)
        
        except AuthenticationFailed as e:
            return Response({
                "detail" : str(e)
            }, status = status.HTTP_403_FORBIDDEN)
            
        except:
            return Response({
                "detail" : "Internal Server Error"
            }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
