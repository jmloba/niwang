# Generated by Django 5.0.3 on 2024-04-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_useraccess_article_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccess',
            name='programmer_access',
            field=models.BooleanField(default=False),
        ),
    ]
