from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Circulationboard

def AllCirculationBoard(request):
    # HTTP responce test.
    #return HttpResponse('All Circuration Board')

    year_of_first_day = timezone.datetime(2022, 4, 1)
    year_of_last_day = timezone.datetime(2023, 3, 31)
    circulationlist = Circulationboard.objects.filter(start_date__gte=year_of_first_day, end_date__lte=year_of_last_day).order_by('start_date')
    context = {
        'circulationlist':circulationlist,
    }
    return render(request, 'CirculationBoard/CirculatedList.html', context)
    