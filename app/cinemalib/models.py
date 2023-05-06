from datetime import date

from django.db import models
from django.urls import reverse

from .common.models import BaseFieldModel


class Category(BaseFieldModel):
    """Movies category"""

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Genre(BaseFieldModel):
    """Cinema genre"""

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Actor(models.Model):
    """Actors & Directors"""

    class Meta:
        verbose_name = 'Actors & Directors'
        verbose_name_plural = 'Actors & Directors'

    name = models.CharField(
        verbose_name='Name',
        max_length=100,
    )
    description = models.TextField(verbose_name='Description')
    age = models.PositiveSmallIntegerField(
        verbose_name='Human age',
        default=0,
    )
    image = models.ImageField(
        verbose_name='Image',
        upload_to='actors/',
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Movie"""

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    title = models.CharField(
        verbose_name='Movie',
        max_length=100,
    )
    tagline = models.CharField(
        verbose_name='Tagline',
        max_length=100,
        default='',
    )
    description = models.TextField(
        verbose_name='Description',
        max_length=3000,
    )
    poster = models.ImageField(
        verbose_name='Poster',
        upload_to='movies/',
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Year',
        default=2023,
    )
    country = models.CharField(
        verbose_name='Country',
        max_length=30,
    )
    directors = models.ManyToManyField(
        verbose_name='Directors',
        to=Actor,
        related_name='film_director',
    )
    actors = models.ManyToManyField(
        verbose_name='Actors',
        to=Actor,
        related_name='film_actor',
    )
    genres = models.ManyToManyField(
        verbose_name='Genre',
        to=Genre,
    )
    world_premiere = models.DateField(
        verbose_name='World premiere date',
        default=date.today,
    )
    budget = models.PositiveIntegerField(
        verbose_name='Budget',
        default=0,
        help_text='by dollar USA',
    )
    fees_in_usa = models.PositiveIntegerField(
        verbose_name='Fees in USA',
        default=0,
        help_text='by dollar USA',
    )
    fees_in_world = models.PositiveIntegerField(
        verbose_name='Fees in World',
        default=0,
        help_text='by dollar USA',
    )
    category = models.ForeignKey(
        verbose_name='Category',
        to=Category,
        on_delete=models.CASCADE,
        null=True,
    )
    url = models.SlugField(
        verbose_name='Url',
        max_length=150,
        unique=True,
    )
    is_draft = models.BooleanField(
        verbose_name='Is it draft',
        default=False,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})


class MovieShorts(models.Model):
    """Shorts from movie"""

    class Meta:
        verbose_name = 'Movie Short'
        verbose_name_plural = 'Movie Shorts'

    title = models.CharField(
        verbose_name='Title',
        max_length=100,
    )
    description = models.TextField(
        verbose_name='Description',
        max_length=3000,
    )
    image = models.ImageField(
        verbose_name='Shorts',
        upload_to='movie_shorts/',
    )
    movie = models.ForeignKey(
        verbose_name='Movie',
        to=Movie,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class RatingStar(models.Model):
    """Rating star for movie"""

    class Meta:
        verbose_name = 'Movie Short'
        verbose_name_plural = 'Movie Shorts'

    value = models.PositiveSmallIntegerField(
        verbose_name='Value',
        default=0,
    )

    def __str__(self):
        return self.value


class Rating(models.Model):
    """Movie rating"""

    class Meta:
        verbose_name = 'Movie rating'
        verbose_name_plural = 'Movie ratings'

    ip = models.CharField(
        verbose_name='IP address',
        max_length=15,
    )
    star = models.ForeignKey(
        verbose_name='Star',
        to=RatingStar,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(
        verbose_name='Movie',
        to=Movie,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.star} - {self.movie}'


class Reviews(models.Model):
    """Reviews for movie"""

    class Meta:
        verbose_name = 'Review for movie'
        verbose_name_plural = 'Reviews for movie'

    email = models.EmailField(
        verbose_name='Email',
        max_length=100,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
    )
    text = models.TextField(
        verbose_name='Review text',
        max_length=5000,
    )
    parent = models.ForeignKey(
        verbose_name='Parent review',
        to='self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    movie = models.ForeignKey(
        verbose_name='Movie',
        to=Movie,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} - {self.movie}'
