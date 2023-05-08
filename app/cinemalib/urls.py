from django.urls import path

from .views import ActorView, AddReviewView, AddStarRatingView, FilterMovieView, MovieDetailView, MovieView

urlpatterns = [
    path('', MovieView.as_view()),
    path('filter/', FilterMovieView.as_view(), name='filter'),
    path('add_rating/', AddStarRatingView.as_view(), name='add_rating'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReviewView.as_view(), name='add_review'),
    path('actor/<str:slug>/', ActorView.as_view(), name='actor_detail'),
]
