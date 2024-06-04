from django.conf import settings
from django.core.mail import send_mail
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import (ParseError,
                                       AuthenticationFailed)
from api.v1.serializers import (ResetPasswordSerializer,
                                ForgotPasswordSerializer)


class RecoverViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin):


    serializer_class = ForgotPasswordSerializer

    
    def get_serializer_class(self):
        if self.action == "verify":
            return ResetPasswordSerializer
        
        return super().get_serializer_class()


    def create(self, request, *args, **kwargs): 
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
        
        except AuthenticationFailed as e:
            return Response({
                "detail" : str(e)
            }, status = status.HTTP_403_FORBIDDEN)
        
        except:
            return Response({
                "detail" : "Internal Server Error"
            }, status = status.HTTP_500_INTERNAL_SERVER_ERROR )
