# Generated by Django 4.1.7 on 2024-04-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccess',
            name='todo_access_all',
            field=models.BooleanField(default=False),
        ),
    ]
