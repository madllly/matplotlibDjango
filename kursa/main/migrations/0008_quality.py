# Generated by Django 4.0.3 on 2022-11-01 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_jobtitle_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productivity', models.IntegerField(max_length=255, verbose_name='Продуктивность')),
                ('feasibility', models.IntegerField(max_length=255, verbose_name='Выполняемость задач')),
                ('responsibility', models.IntegerField(max_length=255, verbose_name='Отвественность')),
                ('involvement', models.IntegerField(max_length=255, verbose_name='Вовлеченность в процесс')),
                ('internal', models.IntegerField(max_length=255, verbose_name='Внутренне качество работы')),
                ('flexibility', models.IntegerField(max_length=255, verbose_name='Гибкость')),
                ('multitasking', models.IntegerField(max_length=255, verbose_name='Мультиадачность')),
                ('date', models.DateTimeField(verbose_name='Дата оценки')),
                ('worker', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='main.worker')),
            ],
        ),
    ]
