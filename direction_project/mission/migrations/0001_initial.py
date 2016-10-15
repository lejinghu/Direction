# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-15 05:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('min_member_count', models.IntegerField()),
                ('max_member_count', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_missions', to=settings.AUTH_USER_MODEL)),
                ('joineders', models.ManyToManyField(related_name='joined_missions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joining_mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joiners', to='mission.Mission')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('lng', models.DecimalField(decimal_places=12, max_digits=16)),
                ('lat', models.DecimalField(decimal_places=12, max_digits=16)),
                ('description', models.TextField()),
                ('finishers', models.ManyToManyField(related_name='finished_tasks', to=settings.AUTH_USER_MODEL)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mission.Mission')),
            ],
        ),
    ]
