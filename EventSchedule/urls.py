from django.urls import path

from . import views

app_name = 'EventSchedule'
urlpatterns = [
    path("AllEventSchedule/", views.AllEventSchedule, name="AllEventSchedule"),
    path("<int:pk>/", views.DetailView.as_view(), name="EventDetail"),
]
