from django import template

register = template.Library()

_TO_PERSIAN = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')


@register.filter
def persian(value):
    return str(value).translate(_TO_PERSIAN)
