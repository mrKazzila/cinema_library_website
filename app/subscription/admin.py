from django.contrib import admin
from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Register the Subscription model and settings fields for admin"""

    list_display = (
        'email',
        'date',
    )
