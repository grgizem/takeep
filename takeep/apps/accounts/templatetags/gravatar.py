import urllib, hashlib
from django import template

register = template.Library()

@register.inclusion_tag('accounts/gravatar.html')
def show_gravatar(email, size=48):
    default = "/static/images/default_avatar.png"

    url = "http://www.gravatar.com/avatar.php?"
    url += urllib.urlencode({
        'gravatar_id': hashlib.md5(email).hexdigest(),
        'default': default,
        'size': str(size)
    })

    return {'gravatar': {'url': url, 'size': size}}