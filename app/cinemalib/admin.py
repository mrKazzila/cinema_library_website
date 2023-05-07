from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Actor, Category, Genre, Movie, MovieShorts, Rating, RatingStar, Reviews)

admin.site.site_title = 'CinemaLib'
admin.site.site_header = 'CinemaLib'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Register the Category model and settings fields for admin"""

    list_display = (
        'id',
        'name',
        'url',
    )
    list_display_links = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Register the Genre model and settings fields for admin"""

    list_display = ('name',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Register the Actor model and settings fields for admin"""

    list_display = (
        'name',
        'age',
        '_get_image',
    )
    readonly_fields = ('_get_image',)
    fieldsets = (
        (
            'Name & Age',
            {
                'fields': ((
                    'name',
                    'age',
                ),),
            },
        ),
        (
            'Description',
            {
                'classes': ('collapse',),
                'fields': (('description',),),
            },
        ),
        (
            'Image',
            {
                'classes': ('collapse',),
                'fields': ((*(
                    'image',
                    '_get_image',
                ),),),
            },
        ),
    )

    def _get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wight="50" height="60"')

    _get_image.short_description = 'Image'


class ReviewInline(admin.TabularInline):
    """Helper for viewing the Reviews fields for the Movie model in admin"""

    model = Reviews
    extra = 1
    readonly_fields = (
        'name',
        'email',
    )


class MovieShotsInline(admin.TabularInline):
    """Helper for viewing the MovieShots fields for the Movie model in admin"""

    model = MovieShorts
    extra = 1
    readonly_fields = ('_get_image',)

    def _get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wight="120" height="130"')

    _get_image.short_description = 'Movie Shots Helper'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Register the Movie model and settings fields for admin"""

    list_display = (
        'title',
        'category',
        'url',
        'is_draft',
    )
    list_filter = (
        'category',
        'year',
    )
    search_fields = (
        'title',
        'category__name',
    )

    inlines = [
        MovieShotsInline,
        ReviewInline,
    ]
    save_on_top = True
    save_as = True
    list_editable = ('is_draft',)
    readonly_fields = ('_get_image',)
    fieldsets = (
        (
            'Title & Tagline',
            {
                'fields': ((
                    'title',
                    'tagline',
                ),),
            },
        ),
        (
            'Description',
            {
                'classes': ('collapse',),
                'fields': (('description',),),
            },
        ),
        (
            'Country & years',
            {
                'classes': ('collapse',),
                'fields': ((
                    'country',
                    'year',
                    'world_premiere',
                ),),
            },
        ),
        (
            'Poster',
            {
                'classes': ('collapse',),
                'fields': ((*(
                    'poster',
                    '_get_image',
                ),),),
            },
        ),
        (
            'Actors & Directors',
            {
                'classes': ('collapse',),
                'fields': ((
                    'actors',
                    'directors',
                ),),
            },
        ),
        (
            'Category & Genre',
            {
                'classes': ('collapse',),
                'fields': ((
                    'genres',
                    'category',
                ),),
            },
        ),
        (
            'Finance',
            {
                'classes': ('collapse',),
                'fields': ((
                    'budget',
                    'fees_in_usa',
                    'fees_in_world',
                ),),
            },
        ),
        (
            'Options',
            {
                'classes': ('collapse',),
                'fields': ((
                    'url',
                    'is_draft',
                ),),
            },
        ),
    )

    def _get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} wight="120" height="130"')

    _get_image.short_description = 'Movie Poster'


@admin.register(MovieShorts)
class MovieShortsAdmin(admin.ModelAdmin):
    """Register the Movie Shorts model and settings fields for admin"""

    list_display = (
        'title',
        'movie',
        '_get_image',
    )
    readonly_fields = ('_get_image',)
    fieldsets = (
        (
            'Name & Age',
            {
                'fields': ((
                    'title',
                    'movie',
                ),),
            },
        ),
        (
            'Description',
            {
                'classes': ('collapse',),
                'fields': (('description',),),
            },
        ),
        (
            'Image',
            {
                'classes': ('collapse',),
                'fields': ((*(
                    'image',
                    '_get_image',
                ),),),
            },
        ),
    )

    def _get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wight="50" height="60"')

    _get_image.short_description = 'Movie Shorts'


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    """Register the Rating Star model and settings fields for admin"""

    list_display = ('value',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Register the Rating model and settings fields for admin"""

    list_display = (
        'star',
        'ip',
    )


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Register the Reviews model and settings fields for admin"""

    list_display = (
        'name',
        'email',
        'parent',
        'movie',
        'id',
    )
    readonly_fields = (
        'name',
        'email',
    )
    fieldsets = (
        (
            'Movie',
            {
                'fields': (('movie',),),
            },
        ),
        (
            'Name & Email',
            {
                'fields': ((
                    'name',
                    'email',
                ),),
            },
        ),
        (
            'Review text',
            {
                'classes': ('collapse',),
                'fields': ((
                    'parent',
                    'text',
                ),),
            },
        ),
    )
