from django.urls import include, path
from . import views


urlpatterns = [
    path(r"login", views.LoginView.as_view()),
    path(r"profile", views.UserProfileView.as_view()),
    # path('rest-auth/', include('rest_auth.urls')),
]
