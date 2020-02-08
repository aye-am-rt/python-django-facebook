from urllib.parse import quote, quote_plus
from django import template


# we are getting the django template  library and registring our custom template.
# then we are going to use it in post_detail.html in place of previous video we were useing share_string.
# at very top write {% load urlify %}
# now we will just use {{ instance.content|urlify }} -> better way to do it.(making share string by custom filter)

register=template.Library()


@register.filter
def urlify(value):
    return quote_plus(value)