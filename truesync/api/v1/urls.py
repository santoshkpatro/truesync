from django.urls import path
from .auth.views import login_view, registration_view, ProfileView


urlpatterns = [
    path('auth/login/', login_view),
    path('auth/register/', registration_view),
    path('auth/profile/', ProfileView.as_view()),
]