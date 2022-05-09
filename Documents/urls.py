from django.urls import path

from . import views

app_name = 'Documents'
urlpatterns = [
    path('AllDocumentList/', views.all_document_list, name='AllDocumentList'),
]
