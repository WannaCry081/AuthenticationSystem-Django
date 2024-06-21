from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenBlacklistView,
                                            TokenRefreshView)
from api.v1.viewsets import (LoginViewSet,
                             RegisterViewSet,
                             RecoverViewSet,
                             UserViewSet)


auth_route = routers.DefaultRouter()
auth_route.register(r"login", LoginViewSet, "login")
auth_route.register(r"register", RegisterViewSet, "register")
auth_route.register(r"reset-password", RecoverViewSet, "reset-password")

route = routers.DefaultRouter()
route.register(r"users", UserViewSet, "users")

urlpatterns = [
    path("auth/", include([
        path("", include(auth_route.urls)),
        path("blacklist/", TokenBlacklistView.as_view(), 
             name = "token-blacklist"),
        path("refresh/", TokenRefreshView.as_view(), 
             name = "token-refresh")
    ])),
    
    path("", route.urls)
]
