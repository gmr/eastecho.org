"""
Intercept requests without the cookie set

"""
from django import shortcuts
from django.conf import settings


class AuthCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.COOKIES.get('auth') != settings.SITE_PASSWORD \
                and request.path != '/auth':
            return shortcuts.render(request, 'auth.html', {'err': False})
        return self.get_response(request)
