# Generated by Django 4.0.4 on 2022-04-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0002_alter_document_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='remarks_text',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Remarks'),
        ),
    ]
