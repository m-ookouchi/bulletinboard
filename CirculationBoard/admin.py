from django.contrib import admin

from .models import Circulationboard

class CirculationboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')

    def get_queryset(self, request):
        queryset = super(CirculationboardAdmin, self).get_queryset(request)
        queryset = queryset.order_by('start_date', 'end_date')
        return queryset

admin.site.register(Circulationboard, CirculationboardAdmin)
