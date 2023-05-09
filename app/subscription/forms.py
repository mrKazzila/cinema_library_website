from django import forms
from .models import Subscription
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class SubscriptionForm(forms.ModelForm):
    """Form for email subscription"""

    captcha = ReCaptchaField()

    class Meta:
        model = Subscription
        fields = ('email', 'captcha')
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'editContent',
                'placeholder': 'Your Email...',
            }),
        }
        labels = {
            'email': '',
        }
