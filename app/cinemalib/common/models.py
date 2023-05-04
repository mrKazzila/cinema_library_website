from django.db import models


class BaseFieldModel(models.Model):
    """Abstract model with common fields"""

    class Meta:
        abstract = True

    name = models.CharField(
        verbose_name='Name',
        max_length=200,
    )
    description = models.TextField(
        verbose_name='Description',
        max_length=3000,
    )
    url = models.SlugField(
        verbose_name='Url',
        max_length=160,
        unique=True,
    )

    def __str__(self):
        return self.name
