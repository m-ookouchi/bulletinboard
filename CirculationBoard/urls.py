from django.urls import path

from . import views

app_name = 'CirculationBoard'
urlpatterns = [
    path(
        'CirculationBoard/',
        views.all_circulation_board,
        name='AllCirculationBoard'
    ),
    path(
        '<int:pk>/',
        views.CirculationBoardDetailView.as_view(),
        name="CirculationBoardDetail"
    ),
]
