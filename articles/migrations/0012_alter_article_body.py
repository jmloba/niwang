# Generated by Django 5.0.3 on 2024-04-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_article_body_alter_article_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(max_length=2000),
        ),
    ]
