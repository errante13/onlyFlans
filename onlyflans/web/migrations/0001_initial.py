# Generated by Django 5.0.6 on 2024-06-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flan_uuid', models.UUIDField()),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('slug', models.SlugField()),
                ('is_private', models.BooleanField()),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
