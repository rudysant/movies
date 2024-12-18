# Generated by Django 5.1.3 on 2024-12-17 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=150)),
                ('release_year', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
                ('movie_poster', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('movie_plot', models.TextField()),
            ],
        ),
    ]