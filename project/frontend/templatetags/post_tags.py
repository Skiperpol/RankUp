from django import template
from backend.models import Powiadomienia

register=template.Library()

@register.simple_tag(takes_context=True)
def notification(context):
    user = context['user']
    if user.is_authenticated:
        powiadomienia = Powiadomienia.objects.filter(user=user)
        return powiadomienia.count()
    else:
        return "0"

@register.simple_tag(takes_context=True)
def notification_class(context):
    user = context['user']
    if user.is_authenticated:
        powiadomienia = Powiadomienia.objects.filter(user=user)
        if powiadomienia.count() > 0:
            return "redcolor"
        else: 
            return ""
    else:
        return ""