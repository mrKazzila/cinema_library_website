from django.urls import path

from .views import AddReviewView, MovieDetailView, MovieView

urlpatterns = [
    path('', MovieView.as_view()),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReviewView.as_view(), name='add_review'),
]
