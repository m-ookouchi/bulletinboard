from django.urls import path

from . import views

app_name = 'CirculationBoard'
urlpatterns = [
    path('CirculationBoard/', views.AllCirculationBoard, name='AllCirculationBoard'),
]
