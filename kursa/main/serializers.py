from .models import Worker, Quality
from rest_framework import serializers


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quality
        fields = '__all__'
