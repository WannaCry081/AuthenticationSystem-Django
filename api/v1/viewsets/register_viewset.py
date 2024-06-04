from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import (ParseError,
                                       AuthenticationFailed)
from rest_framework.throttling import AnonRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken
from api.v1.serializers import RegisterSerializer


class RegisterViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin):


    serializer_class = RegisterSerializer
    throttle_classes = [AnonRateThrottle]


    def create(self, request, *args, **kwargs):
        
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
