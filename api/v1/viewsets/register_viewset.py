from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import (ParseError,
                                       AuthenticationFailed)
from rest_framework.throttling import AnonRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from api.v1.serializers import RegisterSerializer


class RegisterViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin):
    """
    A viewset for creating a new user. This viewset returns access and refresh tokens for newly registered users.
    """

    serializer_class = RegisterSerializer
    throttle_classes = [AnonRateThrottle]


    @swagger_auto_schema(
        operation_summary = "Creates a new user.",
        operation_description = "This endpoint returns the access and refresh token for newly registered users.",
        responses = {
            status.HTTP_201_CREATED : openapi.Response("Ok"),
            status.HTTP_400_BAD_REQUEST : openapi.Response("Bad Request"),
            status.HTTP_403_FORBIDDEN : openapi.Response("Forbidden"),
            status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Internal Server Error")
        }
    )
    def create(self, request, *args, **kwargs):
        """
        This endpoint creates a new user and returns the JWT Token.

        Args:
            request: The HTTP request containing the user data.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Response object containing the JWT tokens or an error message.
        """
        try:
            serializer = self.get_serializer(data = request.data)
            serializer.is_valid(raise_exception = True)

            user = serializer.save()
            token = RefreshToken.for_user(user)

            return Response({
                "access" : str(token.access_token),
                "refresh" : str(token)
            }, status = status.HTTP_201_CREATED)

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
