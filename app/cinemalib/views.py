from django.views.generic import DetailView, ListView

from .models import Movie


class MovieView(ListView):
    """List with movies"""

    model = Movie
    template_name = 'cinemalib/movies.html'
    queryset = Movie.objects.filter(is_draft=False)


class MovieDetailView(DetailView):
    """Full movie description"""

    model = Movie
    slug_field = 'url'
    template_name = 'cinemalib/moviesingle.html'
