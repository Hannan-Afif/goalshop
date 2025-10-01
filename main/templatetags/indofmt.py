# shop/templatetags/indofmt.py
from django import template

register = template.Library()

@register.filter
def rupiah(value):
    return f"{value:,}".replace(",", ".")
