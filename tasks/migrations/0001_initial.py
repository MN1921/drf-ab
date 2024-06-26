# Generated by Django 5.0.4 on 2024-04-30 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=512, verbose_name='Описание')),
                ('task_type', models.CharField(choices=[('call', 'Звонок'), ('appointment', 'Встреча')], max_length=100, verbose_name='Тип задачи')),
            ],
            options={
                'verbose_name': 'Задачи',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='CallState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('successful', 'успешный'), ('unsuccessful', 'неуспешный')], max_length=100, verbose_name='Результат звонка')),
                ('reason', models.CharField(blank=True, choices=[('reason_1', 'причина_1'), ('reason_2', 'причина_2'), ('reason_3', 'причина_3')], max_length=100, null=True, verbose_name='Причина')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.task', verbose_name='Задача')),
            ],
            options={
                'verbose_name': 'Состояние вызова',
                'verbose_name_plural': 'Состояние вызова',
            },
        ),
    ]
