from django.db import models
from django.core.validators import FileExtensionValidator

class Document(models.Model):
    # 文書名
    document_name = models.CharField('Document Name', max_length=200)
    # 掲載日
    upload_date = models.DateField('Upload Date')
    # 文書ファイル(PDF)
    document_file = models.FileField('Document File', upload_to='documents/%Y', validators=[FileExtensionValidator('pdf', )], null=True, blank=True)