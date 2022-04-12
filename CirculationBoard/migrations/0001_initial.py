# Generated by Django 4.0.3 on 2022-04-09 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cirsulationboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('document_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Documents.document')),
            ],
        ),
    ]
