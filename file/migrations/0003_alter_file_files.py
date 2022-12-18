# Generated by Django 4.1.4 on 2022-12-17 22:54

import django.core.validators
from django.db import migrations, models
import file.models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_file_verify_file_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='files',
            field=models.FileField(upload_to='', validators=[file.models.file_size, django.core.validators.FileExtensionValidator(allowed_extensions=['docx', 'xls', 'pdf', 'pptx', 'ppt', 'pptm', 'png', 'jpeg', 'jpg', 'xlsx'])]),
        ),
    ]