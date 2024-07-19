# Generated by Django 5.0.4 on 2024-05-12 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_booking', '0002_booking_confirmation_alter_room_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('YAC', 'AC'), ('NAC', 'NON-AC')], max_length=3),
        ),
    ]
