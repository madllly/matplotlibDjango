# Generated by Django 4.0.3 on 2022-10-31 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_job_title_worker_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='job_title',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='main.job_title'),
        ),
    ]
