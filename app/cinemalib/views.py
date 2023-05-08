from django.shortcuts import HttpResponse, redirect
from django.views.generic import DetailView, ListView, View
from django.db.models import Q

from .forms import RatingForm, ReviewsForm
from .models import Actor, Genre, Movie, Rating


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        return context


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


class ActorView(GenreYearsMixin, DetailView):
    """Actor information"""

    model = Actor
    template_name = 'cinemalib/actor.html'
    slug_field = 'name'


class FilterMovieView(GenreYearsMixin, ListView):
    """Movie Filter"""

    template_name = 'cinemalib/movies.html'

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) | Q(genres__in=self.request.GET.getlist('genres')),
        ).distinct()
        return queryset


class AddStarRatingView(View):
    """Add star rating for movie"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get('movie')),
                defaults={'star_id': int(request.POST.get('star'))},
            )
            return HttpResponse(status=201)
        return HttpResponse(status=400)
