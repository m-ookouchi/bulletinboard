from django.contrib import admin

from .models import CirculationBoard


class CirculationBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    fieldsets = (
        (None, {
            "fields": (
                'title', 'start_date', 'end_date'
            ),
        }),
    )

    def get_queryset(self, request):
        queryset = super(CirculationBoardAdmin, self).get_queryset(request)
        queryset = queryset.order_by('start_date', 'end_date')
        return queryset


admin.site.register(CirculationBoard, CirculationBoardAdmin)
