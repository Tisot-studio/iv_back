# Generated by Django 4.0.2 on 2022-02-13 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('podId', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='podcast_covers')),
                ('header', models.CharField(blank=True, max_length=100, null=True)),
                ('episode', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('tracklist', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to='audio')),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='track_covers')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotify', models.URLField(null=True)),
                ('beatport', models.URLField(null=True)),
                ('itunes', models.URLField(null=True)),
                ('soundcloud', models.URLField(null=True)),
                ('release', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.release')),
            ],
        ),
    ]
