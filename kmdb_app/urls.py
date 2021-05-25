from django.urls import re_path
from .views import RegisterUserView, LoginView, MovieView

urlpatterns = [
    re_path(r'^accounts/?$', RegisterUserView.as_view()),
    re_path(r'^login/?$', LoginView.as_view()),
    re_path(r'^movies/?$', MovieView.as_view()),
]
