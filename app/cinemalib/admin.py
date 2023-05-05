from django.contrib import admin

from app.cinemalib.models import Category, Movie, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'url',
    )
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = (
        'name',
        'email',
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'is_draft')
    list_filter = (
        'category',
        'year',
    )
    search_fields = (
        'title',
        'category__name',
    )
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('is_draft',)
    fieldsets = (
        (
            None,
            {
                'fields': ((
                    'title',
                    'tagline',
                ),),
            },
        ),
        (
            None,
            {
                'fields': ((
                    'description',
                    'poster',
                ),),
            },
        ),
        (
            None,
            {
                'fields': ((
                    'country',
                    'year',
                    'world_premiere',
                ),),
            },
        ),
        (
            'Actors',
            {
                'classes': ('collapse',),
                'fields': ((
                    'actor',
                    'directors',
                    'genre',
                    'category',
                ),),
            },
        ),
        (
            'Finance',
            {
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
                'fields': ((
                    'url',
                    'is_draft',
                ),),
            },
        ),
    )


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
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
