from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('workers/', WorkerViewSet.as_view()),
    path('workers/create/', WorkerCreate.as_view()),
    path('workers/<int:pk>', WorkerDetail.as_view()),
    path('quality/',QualityViewSet.as_view()),
    path('quality/create/', QualityCreate.as_view()),
    path('quality/<int:pk>', QualityDetail.as_view()),
    path('test/', index),
    path('test/<int:pk>',qualityDetailView.as_view()),
]
