# Generated by Django 4.0.3 on 2022-10-31 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobtitle',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
    ]