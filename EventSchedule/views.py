import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import EventSchedule

def AllEventSchedule(request):
    # HTTP respoce test.
    #return HttpResponse("All Event Schedule")
    next_year_first_day = datetime.datetime(2023,4,1, tzinfo=timezone.utc)
    eventlist = EventSchedule.objects.filter(schedule_daytime__lt=next_year_first_day).order_by('schedule_daytime')
    context = {
        "eventlist": eventlist,
    }
    return render(request, "EventSchedule/AllEventSchedule.html", context)
