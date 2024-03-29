import arrow
from django import http, shortcuts
from django.conf import settings
from django.db import models as django_models
from django.utils import timezone
from django.views.decorators import cache

from . import instagram, models


def get_navbar_items():
    return {
        'categories': models.Category.objects.all(),
        'clubs': models.Club.objects.all()
    }


@cache.cache_page(3600)
def index(request):
    return shortcuts.render(
        request, 'index.html',
        {
            'navbar': get_navbar_items(),
            'instagram': instagram.get_photos('east.echo')
        }
    )


def club(request, club_slug):
    value = shortcuts.get_object_or_404(models.Club, slug=club_slug)
    return shortcuts.render(
        request, 'club.html',
        {
            'navbar': get_navbar_items(),
            'club': value,
            'events': models.Event.objects.filter(
                club=value,
                start_at__gte=timezone.now())
        }
    )


def clubs(request):
    return shortcuts.render(
        request, 'clubs.html',
        {
            'navbar': get_navbar_items(),
            'clubs': models.Club.objects.all()
        }
    )


def events(request):
    return shortcuts.render(
        request, 'events.html',
        {
            'navbar': get_navbar_items(),
            'events': models.Event.objects.filter()
        }
    )


def this_week(request):
    today = arrow.get(timezone.now())
    event_types = models.EventType.objects.all()

    start_at = today.shift(
        days=-today.weekday()).replace(
            hour=0, minute=0, second=0)

    values = {
        'navbar': get_navbar_items(),
        'start_at': start_at,
        'end_at': start_at.shift(days=6).replace(
            hour=23, minute=59, second=59),
        'event_types': event_types,
        'events': {}
    }
    for event_type in event_types:
        values['events'][event_type.name] = models.Event.objects.filter(
            django_models.Q(
                event_type=event_type,
                start_at__gte=values['start_at'].datetime,
                end_at__lte=values['end_at'].datetime) |
            django_models.Q(
                event_type=event_type,
                start_at__gte=values['start_at'].datetime,
                end_at=None))

    return shortcuts.render(request, 'this-week.html', values)


def auth(request):
    args = {'err': False}
    if request.method == 'POST':
        data = request.POST.copy()
        if data['password'] == settings.SITE_PASSWORD:
            response = http.HttpResponseRedirect('/')
            response.set_cookie('auth', data['password'])
            return response
        args['err'] = True
    return shortcuts.render(request, 'auth.html', args)
