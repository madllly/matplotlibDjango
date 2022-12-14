# Generated by Django 4.0.3 on 2022-11-01 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_quality_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quality',
            name='feasibility',
            field=models.IntegerField(verbose_name='Выполняемость задач'),
        ),
        migrations.AlterField(
            model_name='quality',
            name='flexibility',
            field=models.IntegerField(verbose_name='Гибкость'),
        ),
        migrations.AlterField(
            model_name='quality',
            name='internal',
            field=models.IntegerField(verbose_name='Внутренне качество работы'),
        ),
        migrations.AlterField(
            model_name='quality',
            name='involvement',
            field=models.IntegerField(verbose_name='Вовлеченность в процесс'),
        ),
        migrations.AlterField(
            model_name='quality',
            name='multitasking',
            field=models.IntegerField(verbose_name='Мультиадачность'),
        ),
        migrations.AlterField(
            model_name='quality',
            name='productivity',
            field=models.IntegerField(verbose_name='Продуктивность'),
        ),
        migrations.AlterField(
            model_name='quality',
            name='responsibility',
            field=models.IntegerField(verbose_name='Отвественность'),
        ),
        migrations.AlterField(
            model_name='quality',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.worker'),
        ),
    ]
