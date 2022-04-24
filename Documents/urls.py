from django.urls import path

from . import views

app_name = 'Documents'
urlpatterns = [
    path('AllDocumentList/', views.AllDocumentList, name='AllDocumentList'),
]
