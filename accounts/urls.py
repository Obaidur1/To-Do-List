from django.urls import path, include
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserBankAccountUpdateView,
    Profile_View,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", UserBankAccountUpdateView.as_view(), name="profile"),
    path("photos/", Profile_View, name="photos"),
]
