from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns.extend(
    i18n_patterns(
        path('accounts/', include('allauth.urls')),
        path('pages/', include('django.contrib.flatpages.urls')),
        path('subscription/', include('subscription.urls')),
        path('', include('cinemalib.urls')),
    ),
)

if settings.DEBUG:
    urlpatterns.extend(static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    ))
