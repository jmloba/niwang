# Generated by Django 5.0.4 on 2024-05-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mail', '0013_alter_emailans_email_body_alter_emailans_email_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailans',
            name='email_to',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
