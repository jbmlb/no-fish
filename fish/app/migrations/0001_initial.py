# Generated by Django 3.2.6 on 2021-09-02 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', models.CharField(max_length=255, verbose_name='content')),
            ],
            options={
                'verbose_name': 'detail',
                'verbose_name_plural': 'details',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', models.ImageField(upload_to='static/uploads/images/photos/', verbose_name='image')),
                ('url', models.URLField(verbose_name='url')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'sliders',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('cover', models.ImageField(upload_to='static/uploads/images/photos/', verbose_name='cover')),
                ('show_home', models.BooleanField(default=True, verbose_name='show home')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('picture', models.ManyToManyField(blank=True, to='app.Detail', verbose_name='pictures')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
            },
        ),
        migrations.CreateModel(
            name='DetailImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='static/uploads/images/')),
                ('detail', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.detail')),
            ],
        ),
    ]