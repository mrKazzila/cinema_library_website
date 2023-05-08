from .models import Subscription
from .forms import SubscriptionForm
from django.views.generic import CreateView


class SubscriptionView(CreateView):
    """Email subscription"""

    model = Subscription
    form_class = SubscriptionForm
    success_url = '/'
