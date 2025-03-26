# Generated by Django 5.1.7 on 2025-03-26 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('size', models.FloatField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='media/coffins')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('death_description', models.TextField()),
                ('body_weight', models.FloatField()),
                ('coffin_estimated_size', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('finished_order', models.BooleanField(default=False)),
                ('coffin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.coffin')),
            ],
        ),
    ]
