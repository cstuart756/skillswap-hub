from django import template
from exchanges.models import ExchangeRequest

register = template.Library()

@register.filter
def get_user_request(requests, user):
    """
    Given a queryset of ExchangeRequest and a user, return the user's pending/latest request for the skill, or None.
    """
    if not user.is_authenticated:
        return None
    try:
        return requests.get(requester=user, status=ExchangeRequest.Status.PENDING)
    except ExchangeRequest.DoesNotExist:
        return None
