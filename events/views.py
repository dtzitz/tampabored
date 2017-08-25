from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic

# Create your views here.
from django.http import HttpResponse

from .models import Event

def index(request):
    now = timezone.now()
    events_row1 = Event.objects.filter(end_date__gte=now).order_by('start_date')[:2]
    events_row2 = Event.objects.filter(end_date__gte=now).order_by('start_date')[2:3]
    events_row3 = Event.objects.filter(end_date__gte=now).order_by('start_date')[3:4]
    context = {
        'events_row1': events_row1,
        'events_row2': events_row2,
        'events_row3': events_row3,
        }
    return render(request, 'index.html', context)

class DetailView(generic.DetailView):
    model = Event
    template_name = 'detail.html'