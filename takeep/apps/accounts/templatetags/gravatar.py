# -*- coding:utf-8 -*-

import urllib, hashlib
from django import template

register = template.Library()

@register.inclusion_tag('accounts/gravatar.html')
def show_gravatar(email, size=48):
	"""
	Gravatar 'APIs' require no authentication, and are all based around simple HTTP GET requests.
	Gravatar images may be requested just like a normal image, using an IMG tag.

	The most basic image request URL looks like this:
	http://www.gravatar.com/avatar.php?gravatar_id=HASH

	All that is required to display a user’s Gravatar is their e-mail address.
	The URL to the Gravatar image simply takes a hashed e-mail address to identify the user,
	- and a few other optional parameters to control the size
	- and what to do if there us no Gravatar associated with their e-mail address.
	"""
	default = "/static/images/default_avatar.png"
	"""
	Default avatar image, that is going to be use if the user does not have an account on gravatar.
	"""
	url = "http://www.gravatar.com/avatar.php?"
	url += urllib.urlencode({
        'gravatar_id': hashlib.md5(email).hexdigest(),
        'default': default,
        'size': str(size)
    })

	return {'gravatar': {'url': url, 'size': size}}