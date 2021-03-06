# Generated by Django 4.0.3 on 2022-04-09 06:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=200, verbose_name='Document Name')),
                ('upload_date', models.DateField(verbose_name='Upload Date')),
                ('document_file', models.FileField(upload_to='documents/%Y', validators=[django.core.validators.FileExtensionValidator('pdf')], verbose_name='Document File')),
            ],
        ),
    ]
