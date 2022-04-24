from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Document

def AllDocumentList(request):
    # HTTP responce test.
    #return HttpResponse('All Circuration Board')

    year_of_first_day = timezone.datetime(2022, 4, 1)
    year_of_last_day = timezone.datetime(2023, 3, 31)
    document_list = Document.objects.filter(upload_date__gte=year_of_first_day, upload_date__lte=year_of_last_day).order_by('upload_date')
    context = {
        'documentlist':document_list,
    }
    return render(request, 'Documents/AllDocuments.html', context)
    