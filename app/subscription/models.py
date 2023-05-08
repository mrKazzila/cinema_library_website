from django.db import models


class Subscription(models.Model):
    """Email subscription"""

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    email = models.EmailField(verbose_name='Email')
    date = models.DateTimeField(
        verbose_name='Subscription date',
        auto_now_add=True,
    )

    def __str__(self):
        return self.email
