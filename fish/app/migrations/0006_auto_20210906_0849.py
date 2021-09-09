# Generated by Django 3.2.6 on 2021-09-06 08:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_photo_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('cover', models.ImageField(upload_to='static/uploads/images/photos/', verbose_name='cover')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('views', models.BigIntegerField(default=0)),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='created')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.RemoveField(
            model_name='photo',
            name='created',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='views',
        ),
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.ManyToManyField(to='app.Category'),
        ),
    ]