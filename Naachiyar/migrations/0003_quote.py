# Generated by Django 5.0.1 on 2024-02-22 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Naachiyar', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=250)),
                ('budget', models.CharField(max_length=10)),
                ('s_date', models.CharField(max_length=10)),
                ('e_date', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
