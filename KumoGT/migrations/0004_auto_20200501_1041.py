# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-05-01 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KumoGT', '0003_auto_20200403_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to=b'documents/')),
            ],
        ),
        migrations.AddField(
            model_name='degree',
            name='note',
            field=models.TextField(blank=True, verbose_name=b'Degree Note'),
        ),
        migrations.AlterField(
            model_name='degree',
            name=b'stu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='degrees', to='KumoGT.Student', verbose_name=b'Student'),
        ),
    ]
