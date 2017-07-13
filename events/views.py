from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse

from .models import Event

def index(request):
    now = timezone.now()
    events_row1 = Event.objects.filter(end_date__gte=now).order_by('start_date')[:2]
    events_row2 = Event.objects.filter(end_date__gte=now).order_by('start_date')[2:3]
    context = {
        'events_row1': events_row1,
        'events_row2': events_row2,
        }
    return render(request, 'index.html', context)