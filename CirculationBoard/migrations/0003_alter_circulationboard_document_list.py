# Generated by Django 4.0.3 on 2022-04-11 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0002_alter_document_document_file'),
        ('CirculationBoard', '0002_rename_cirsulationboard_circulationboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circulationboard',
            name='document_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Documents.document'),
        ),
    ]
