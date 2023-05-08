from django import template
from subscription.forms import SubscriptionForm

register = template.Library()


@register.inclusion_tag(filename='subscription/tags/form.html')
def subscription_form():
    """Tag for subscription form"""
    return {'subscription_form': SubscriptionForm()}
