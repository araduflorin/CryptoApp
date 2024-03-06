from django import template
register = template.Library()


@register.filter
def format_large_number(value):
    try:
        value = float(value)
    except (TypeError, ValueError):
        return value

    if value >= 1000000000000.00:  # Trillions
        return f"{value / 1000000000000.00:.2f}t"
    elif value >= 1000000000.00:  # Billions
        return f"{value / 1000000000.00:.2f}b"
    elif value >= 1000000.00:  # Millions
        return f"{value / 1000000.00:.2f}m"
    else:
        return str(value)