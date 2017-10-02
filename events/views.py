from django.shortcuts import render, get_object_or_404
import pytz
from datetime import datetime
from django.views import generic

# Create your views here.
from django.http import HttpResponse

from .models import Event

def index(request):
    now = datetime.now(pytz.timezone('US/Eastern'))
    events_row1 = Event.objects.filter(end_date__gte=now).order_by('start_date')[:2]
    events_row2 = Event.objects.filter(end_date__gte=now).order_by('start_date')[2:4]
    events_row3 = Event.objects.filter(end_date__gte=now).order_by('start_date')[4:6]
    context = {
        'events_row1': events_row1,
        'events_row2': events_row2,
        'events_row3': events_row3,
        }
    return render(request, 'index.html', context)

class DetailView(generic.DetailView):
    model = Event
    template_name = 'detail.html'

def contact(request):
    return render(request, 'contact.html')

def recurring(request):
    # now = datetime.now(pytz.timezone('US/Eastern'))
    # elist = Event.objects.filter(end_date__gte=now).order_by('start_date')
    # context = {'event_list': elist}
    return render(request,'recurring.html')