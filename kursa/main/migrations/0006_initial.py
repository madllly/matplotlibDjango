# Generated by Django 4.0.3 on 2022-10-31 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0005_delete_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Должности')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('job_title', models.ForeignKey(default='no', on_delete=django.db.models.deletion.CASCADE, to='main.jobtitle')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
