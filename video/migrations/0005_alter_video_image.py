# Generated by Django 4.1.13 on 2024-01-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_alter_video_image_alter_video_subtitles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.TextField(),
        ),
    ]