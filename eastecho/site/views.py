from django import shortcuts

from . import models


def get_navbar_items():
    return {
        'categories': models.Category.objects.all(),
        'clubs': models.Club.objects.all()
    }


def index(request):
    return shortcuts.render(
        request, 'index.html',
        {
            'navbar': get_navbar_items()
        }
    )


def club(request, club_slug):
    obj = shortcuts.get_object_or_404(models.Club, slug=club_slug)
    return shortcuts.render(
        request, 'club.html',
        {
            'navbar': get_navbar_items(),
            'club': obj
        }
    )
