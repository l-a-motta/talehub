# Generated by Django 3.2.5 on 2021-07-03 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_chapter_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chapter',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
