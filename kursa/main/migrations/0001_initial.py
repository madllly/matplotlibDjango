# Generated by Django 4.0.3 on 2022-10-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]