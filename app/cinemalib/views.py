from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, View

from .forms import ReviewsForm
from .models import Actor, Genre, Movie


class GenreYearsMixin:
    """Mixin for getting movie genres and years"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(is_draft=False).values('year')


class MovieView(GenreYearsMixin, ListView):
    """List with movies"""

    model = Movie
    template_name = 'cinemalib/movies.html'
    queryset = Movie.objects.filter(is_draft=False)


class MovieDetailView(GenreYearsMixin, DetailView):
    """Full movie description"""

    model = Movie
    queryset = Movie.objects.filter(is_draft=False)
    slug_field = 'url'
    template_name = 'cinemalib/moviesingle.html'


class AddReviewView(View):
    """Reviews"""

    def post(self, request, pk):
        # TODO: transfer to services
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))

            form.movie = movie
            form.save()

        return redirect(movie.get_absolute_url())


class ActorView(DetailView):
    """Actor information"""

    model = Actor
    template_name = 'cinemalib/actor.html'
    slug_field = 'name'
