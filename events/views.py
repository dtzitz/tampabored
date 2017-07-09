from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import Event

def index(request):
    upcoming_event_list = Event.objects.order_by('event_start_date')[:10]
    context = {'upcoming_event_list': upcoming_event_list}
    return render(request, 'index.html', context)