from django import template

register = template.Library()

@register.filter
def currency_usd(value):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return value

    return f'$ {value:,.2f}'
