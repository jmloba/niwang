# Generated by Django 5.0.3 on 2024-04-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_useraccess_programmer_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images/'),
        ),
    ]
