# Generated by Django 4.1.4 on 2022-12-17 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_remove_catalog_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='title',
        ),
    ]