from django import template
from cinemalib.models import Category, Movie

register = template.Library()


@register.simple_tag()
def get_categories():
    """View all categories"""
    return Category.objects.all()


@register.inclusion_tag(filename='cinemalib/tags/last_movie.html')
def get_last_movies(count: int = 5):
    """View at sidebar 'count' last added movies"""
    movies = Movie.objects.filter(is_draft=False).order_by('id')[:count]
    return {'last_movies': movies}
