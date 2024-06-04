from django.urls import path, include
from rest_framework import routers
from api.v1.viewsets import (LoginViewSet,
                             RegisterViewSet,
                             RecoverViewSet)


auth_route = routers.DefaultRouter()


auth_route.register(r"login", LoginViewSet, "login")
auth_route.register(r"register", RegisterViewSet, "register")
auth_route.register(r"reset-password", RecoverViewSet, "reset-password")


urlpatterns = [
    path("auth/", include(auth_route.urls))
]
