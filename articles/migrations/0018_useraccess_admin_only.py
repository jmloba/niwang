# Generated by Django 4.2.14 on 2024-07-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_alter_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccess',
            name='admin_only',
            field=models.BooleanField(default=False),
        ),
    ]
