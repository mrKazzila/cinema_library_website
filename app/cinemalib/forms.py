from django import forms
from .models import Rating, RatingStar, Reviews


class ReviewsForm(forms.ModelForm):
    """Form for Reviews"""

    class Meta:
        model = Reviews
        fields = (
            'name',
            'email',
            'text',
        )


class RatingForm(forms.ModelForm):
    """Form for Rating"""

    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(),
        widget=forms.RadioSelect(),
        empty_label=None,
    )

    class Meta:
        model = Rating
        fields = ('star',)
