# Generated by Django 5.0.3 on 2024-04-11 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailans',
            name='email_link',
        ),
    ]
