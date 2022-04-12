from django.contrib import admin

from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'upload_date', 'document_file')

    def get_queryset(self, request):
        queryset = super(DocumentAdmin, self).get_queryset(request)
        queryset = queryset.order_by('upload_date')
        return queryset

admin.site.register(Document, DocumentAdmin)
