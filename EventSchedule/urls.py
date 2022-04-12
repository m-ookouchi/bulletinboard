from django.urls import path

from . import views

app_name = 'EventSchedule'
urlpatterns = [
    path("AllEventSchedule/", views.AllEventSchedule, name="AllEventSchedule"),
]
