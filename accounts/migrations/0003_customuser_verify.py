# Generated by Django 4.1.4 on 2022-12-16 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_email_alter_customuser_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Verify',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
