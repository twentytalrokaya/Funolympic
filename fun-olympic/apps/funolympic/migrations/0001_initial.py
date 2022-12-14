# Generated by Django 4.1.1 on 2022-09-19 03:33

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Title')),
                ('image', models.ImageField(upload_to='category-img', verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('cat_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Upadated at')),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OlympicGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Title')),
                ('thumbnail_image', models.ImageField(upload_to='category-img', verbose_name='Thumbnail Image')),
                ('video_url', models.URLField(verbose_name='Video URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Slug')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End date')),
                ('created_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Upadated at')),
                ('is_deleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_category', to='funolympic.category')),
            ],
        ),
    ]
