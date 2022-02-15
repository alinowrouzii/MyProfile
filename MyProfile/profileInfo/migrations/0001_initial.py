# Generated by Django 4.0.1 on 2022-02-15 15:53

from django.db import migrations, models
import profileInfo.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(blank=True)),
                ('institute', models.CharField(max_length=500)),
                ('degree', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', tinymce.models.HTMLField(blank=True)),
                ('photo', models.ImageField(null=True, upload_to=profileInfo.models.get_portfolio_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('about', tinymce.models.HTMLField(blank=True)),
                ('profile_photo', models.ImageField(null=True, upload_to=profileInfo.models.get_upload_path)),
                ('email', models.CharField(max_length=500)),
                ('linkedIn', models.CharField(blank=True, max_length=500)),
                ('github', models.CharField(blank=True, max_length=500)),
                ('stackOverFlow', models.CharField(blank=True, max_length=500)),
                ('facebook', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
