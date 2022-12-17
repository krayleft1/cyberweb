# Generated by Django 4.1.4 on 2022-12-17 00:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0010_alter_file_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(7)]),
        ),
    ]