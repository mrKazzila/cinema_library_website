from django.shortcuts import render  # noqa
from django.views.generic.base import View
from .models import Movie


class MovieView(View):

    def get(self, request):
        movies = Movie.objects.all()
        return render(request=request, template_name='cinemalib/movies.html', context={'movies_list': movies})
