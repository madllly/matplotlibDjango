from django.contrib import admin
from .models import *


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'patronymic', 'last_name', 'job_title',)


class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)


class QualityAdmin(admin.ModelAdmin):
    list_display = (
        'worker', 'productivity', 'feasibility', 'responsibility', 'involvement', 'internal', 'flexibility',
        'multitasking',
        'date',)


admin.site.register(Worker, WorkerAdmin)
admin.site.register(JobTitle, JobTitleAdmin)
admin.site.register(Quality,QualityAdmin)