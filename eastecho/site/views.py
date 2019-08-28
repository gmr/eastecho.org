from django import shortcuts


def index(request):
    return shortcuts.render(request, 'index.html', {})
