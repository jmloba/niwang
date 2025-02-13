# Generated by Django 5.0.3 on 2024-04-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('date_birth', models.DateField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('thumb', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='bootstrap/images/')),
            ],
        ),
    ]
