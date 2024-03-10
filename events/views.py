from django.shortcuts import render, get_object_or_404
from .models import Category, Event

def events_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    events = Event.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        events = events.filter(category=category)
    return render(request, 'events/event/list.html',
                            {'category': category,
                            'categories': categories,
                            'events': events})


def event_detail(request, id, slug):
    event = get_object_or_404(Event, id=id, slug=slug, available=True)
    return render(request, 'events/event/detail.html',
                            {'event': event})