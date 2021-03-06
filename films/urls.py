from django.urls import path

from . import views



urlpatterns = [
    path("", views.AllMovieView.as_view()),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_detail'),
    # path("<int:pk>/", views.MovieView.as_view(), name='all_movies'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),
    path("actor/<slug:slug>/", views.ActorView.as_view(), name='actor_detail')
]