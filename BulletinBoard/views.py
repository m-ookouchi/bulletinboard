from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from EventSchedule.models import EventSchedule
from CirculationBoard.models import Circulationboard
from Documents.models import Document

def index(request):
    # HTTP responce test
    #return HttpResponse("<h1>Hello world</h1>")

    # Get date & time.
    today = timezone.now()
    # Future date test
    #today = datetime.datetime(2022, 5, 1, timezone.utc)

    # Get event schedule (most recent 5)
    eventlist = EventSchedule.objects.filter(schedule_daytime__gt=today).order_by('schedule_daytime')[:5]

    # Get document list (most recent 5)
    documentlist = Document.objects.filter(upload_date__gt=today).order_by('upload_date')[:5]

    # Get circuration board (most recent 5)
    circulatinglist = Circulationboard.objects.filter(end_date__isnull=True).order_by('start_date')[:5]

    # Rendering page
    context = {
        'eventlist':eventlist,
        'documentlist':documentlist,
        'circulatinglist':circulatinglist,
    }
    return render(request, 'BulletinBoard/index.html', context)
