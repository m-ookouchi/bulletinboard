from django.contrib import admin

from .models import EventSchedule

class EventScheduleAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'target_person', 'place', 'schedule_daytime')

    def get_queryset(self, request):
        queryset = super(EventScheduleAdmin, self).get_queryset(request)
        queryset = queryset.order_by('schedule_daytime')
        return queryset

admin.site.register(EventSchedule, EventScheduleAdmin)
