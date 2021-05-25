from django.urls import re_path
from .views import RegisterUserView, LoginView, MovieView, MovieSingleView, ReviewView, CommentView

urlpatterns = [
    re_path(r'^accounts/?$', RegisterUserView.as_view()),
    re_path(r'^login/?$', LoginView.as_view()),
    re_path(r'^movies/?$', MovieView.as_view()),
    re_path(r'^movies/(?P<movie_id>\w+)/?$', MovieSingleView.as_view()),
    re_path(r'^movies/(?P<movie_id>\w+)/review/?$', ReviewView.as_view()),
    re_path(r'^movies/(?P<movie_id>\w+)/comments/?$', CommentView.as_view()),
]
