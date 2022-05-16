from django.urls import path

from . import views

app_name = 'EventSchedule'
urlpatterns = [
    path(
        "AllEventSchedule/",
        views.all_event_schedule,
        name="AllEventSchedule"
    ),
    path(
        "<int:pk>/",
        views.DetailView.as_view(),
        name="EventDetail"
    ),
]
