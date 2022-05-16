import datetime

from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import DetailView

from .models import EventSchedule


def all_event_schedule(request):
    next_year_first_day = datetime.datetime(2023, 4, 1, tzinfo=timezone.utc)
    eventlist = EventSchedule.objects.filter(
        schedule_daytime__lt=next_year_first_day).order_by('schedule_daytime')
    context = {
        "eventlist": eventlist,
    }
    return render(request, "EventSchedule/AllEventSchedule.html", context)


class DetailView(DetailView):
    model = EventSchedule
    template_name = 'EventSchedule/EventDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detail_data = context.get("object")
        detail_data = str(detail_data.detail_info).splitlines()
        context["detail_info"] = detail_data
        return context
