from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView

from .models import CirculationBoard


def all_circulation_board(request):
    year_of_first_day = timezone.datetime(2022, 4, 1)
    year_of_last_day = timezone.datetime(2023, 3, 31)
    circulationlist = CirculationBoard.objects.filter(
            start_date__gte=year_of_first_day,
            end_date__lte=year_of_last_day
        ).order_by('start_date')
    context = {
        'circulationlist': circulationlist,
    }
    return render(request, 'CirculationBoard/CirculatedList.html', context)

class CirculationBoardDetailView(DetailView):
    model = CirculationBoard
    template_name = "CirculationBoard/CirculationBoardDetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        document_list = context.get("object")
        document_list = document_list.document_set.all()
        context["document_list"] = document_list
        return context
