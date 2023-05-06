from django.urls import path

from .views import MovieDetailView, MovieView

urlpatterns = [
    path('', MovieView.as_view()),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
]
