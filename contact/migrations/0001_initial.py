# Generated by Django 5.1.4 on 2024-12-27 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
