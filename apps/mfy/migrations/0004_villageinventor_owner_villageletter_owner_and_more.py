# Generated by Django 4.2 on 2024-03-26 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mfy', '0003_jobseeker_villagebusinnesmen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='villageinventor',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='villageletter',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='workerinfo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='workers_photo', verbose_name='Photo'),
        ),
        migrations.AddField(
            model_name='villagebusinnesmenproduct',
            name='village_businnesmen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mfy.villagebusinnesmen', verbose_name='Village Businnesmen'),
        ),
        migrations.AddField(
            model_name='villagebusinnesmen',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]