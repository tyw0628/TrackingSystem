# Generated by Django 2.2.6 on 2019-10-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KumoGT', '0006_auto_20191028_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deg_plan_doc',
            name='notes',
            field=models.CharField(blank=True, max_length=511),
        ),
        migrations.AlterField(
            model_name='fin_exam_doc',
            name='notes',
            field=models.CharField(blank=True, max_length=511),
        ),
        migrations.AlterField(
            model_name='pre_exam_doc',
            name='notes',
            field=models.CharField(blank=True, max_length=511),
        ),
        migrations.AlterField(
            model_name='t_d_doc',
            name='notes',
            field=models.CharField(blank=True, max_length=511),
        ),
        migrations.AlterField(
            model_name='t_d_prop_doc',
            name='notes',
            field=models.CharField(blank=True, max_length=511),
        ),
    ]
