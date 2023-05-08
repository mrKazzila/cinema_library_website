from django import forms
from .models import Rating, RatingStar, Reviews
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ReviewsForm(forms.ModelForm):
    """Form for Reviews"""

    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = (
            'name',
            'email',
            'text',
            'captcha',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border'}),
            'text': forms.Textarea(attrs={'class': 'form-control border'}),
        }


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
