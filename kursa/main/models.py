from django.db import models
from django.urls import reverse


class JobTitle(models.Model):
    title = models.CharField('Должности', max_length=255)

    def __str__(self):
        return "Должность: {}".format(self.title)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Worker(models.Model):
    first_name = models.CharField('Имя', max_length=255)
    patronymic = models.CharField('Отчество', blank=True, max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE, default='no')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Quality(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    productivity = models.IntegerField('Продуктивность')
    feasibility = models.IntegerField('Выполняемость задач')
    responsibility = models.IntegerField('Отвественность')
    involvement = models.IntegerField('Вовлеченность в процесс')
    internal = models.IntegerField('Внутренне качество работы')
    flexibility = models.IntegerField('Гибкость')
    multitasking = models.IntegerField('Мультиадачность')
    date = models.DateField('Дата оценки')


    def get_absolute_url(self):
        return reverse('myurl', kwargs={'date': self.date, })

    class Meta:
        verbose_name = 'Оценка качества'
        verbose_name_plural = 'Оценка качества'
