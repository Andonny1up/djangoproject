# Generated by Django 4.1.5 on 2023-01-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.TextField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(verbose_name=200)),
            ],
        ),
    ]
