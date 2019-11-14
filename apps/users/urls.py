from django.urls import include, path
from . import views


urlpatterns = [
    path(r"register", views.RegisterView.as_view()),
    path(r"login", views.LoginView.as_view()),
    path(r"profile", views.ProfileView.as_view()),
    path(r"logout", views.LogoutView.as_view()),
    path(r"password-reset", views.PasswordResetView.as_view()),
]
