# Generated by Django 4.1.7 on 2024-04-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mail', '0011_alter_emailans_email_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailans',
            name='email_to',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
