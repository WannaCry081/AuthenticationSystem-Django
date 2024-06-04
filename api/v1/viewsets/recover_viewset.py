from django.conf import settings
from django.core.mail import send_mail
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.exceptions import (ParseError,
                                       AuthenticationFailed,
                                       NotFound)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from api.v1.serializers import (ResetPasswordSerializer,
                                ForgotPasswordSerializer)


class RecoverViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin):
    """
    A viewset for handling password recovery and reset. This viewset provides
    endpoints for initiating password recovery by sending a reset code and for
    verifying the reset code to update the password.
    """

    serializer_class = ForgotPasswordSerializer
    throttle_classes = [AnonRateThrottle]

    
    def get_serializer_class(self):
        if self.action == "verify":
            return ResetPasswordSerializer
        
        return super().get_serializer_class()

    @swagger_auto_schema(
        operation_summary = "Initiates password recovery.",
        operation_description = "This endpoint sends a password reset code to the user's email.",
        responses = {
            status.HTTP_200_OK: openapi.Response("Successfully sent code."),
            status.HTTP_400_BAD_REQUEST: openapi.Response("Bad Request"),
            status.HTTP_403_FORBIDDEN: openapi.Response("Forbidden"),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response("Internal Server Error")
        }
    )
    def create(self, request, *args, **kwargs):
        """
        This endpoint sends a password reset code to the user's email.

        Args:
            request: The HTTP request containing the user's email.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Response object indicating the result of the email sending process.
        """
        try:
            serializer = self.get_serializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            
            user = serializer.validated_data.get("user")
            
            send_mail(
                "Reset Password",
                f"Code: {user.reset_code}",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently = True,
            )
            return Response({
                "detail" : f"Successfully send code to {request.data['email']}."
            }, status = status.HTTP_200_OK)

        except ParseError as e:
            return Response({
                "detail" : str(e)
            }, status = status.HTTP_400_BAD_REQUEST)
        
        except NotFound as e:
            return Response({
                "detail" : str(e)
            }, status = status.HTTP_403_FORBIDDEN)
        
        except:
            return Response({
                "detail" : "Internal Server Error"
            }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


    @swagger_auto_schema(
        method="post",
        operation_summary="Verifies the password reset code.",
        operation_description="This endpoint verifies the password reset code and updates the user's password.",
        responses={
            status.HTTP_200_OK: openapi.Response("Password successfully updated."),
            status.HTTP_400_BAD_REQUEST: openapi.Response("Bad Request"),
            status.HTTP_403_FORBIDDEN: openapi.Response("Forbidden"),
            status.HTTP_404_NOT_FOUND: openapi.Response("Not Found"),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response("Internal Server Error")
        }
    )
    @action(methods = ["POST"], detail = False)
    def verify(self, request, pk = None):
        """
        This endpoint verifies the password reset code and updates the user's password.

        Args:
            request: The HTTP request containing the reset code and new password.
            pk: Primary key, not used in this action.

        Returns:
            Response: A Response object indicating the result of the password reset process.
        """
        try:
            serializer = self.get_serializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            
            return Response({
                "detail" : "Password successfully updated."
            }, status = status.HTTP_200_OK)

        except ParseError as e:
            return Response({
                "detail" : str(e)
            }, status = status.HTTP_400_BAD_REQUEST)
        
        except AuthenticationFailed as e:
            return Response({
                "detail" : str(e)
            }, status = status.HTTP_403_FORBIDDEN)
        
        except NotFound as e:
            return Response({
                "detail" : str(e)
            }, status = status.HTTP_404_NOT_FOUND)

        except:
            return Response({
                "detail" : "Internal Server Error"
            }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
