from django.views.generic.list import ListView

from .models import Movie


class MovieView(ListView):
    """List with movies"""

    model = Movie
    template_name = 'cinemalib/movies.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['movies_list'] = Movie.objects.all()
        return context
