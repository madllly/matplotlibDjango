from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WorkerSerializer, QualitySerializer
from .models import Worker
from rest_framework import generics, viewsets
from .models import *
from django.views.generic.detail import DetailView
from .utils import *
from django.shortcuts import get_object_or_404


class WorkerCreate(generics.CreateAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class WorkerViewSet(generics.ListAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class QualityCreate(generics.CreateAPIView):
    serializer_class = QualitySerializer
    queryset = Quality.objects.all()


class QualityViewSet(generics.ListAPIView):
    serializer_class = QualitySerializer
    queryset = Quality.objects.all()


class QualityDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QualitySerializer
    queryset = Quality.objects.all()


def index(request):
    if request.method == 'GET':
        queryset_worker = Worker.objects.all()
        queryset_q = Quality.objects.all()
        data = {'queryset_worker': queryset_worker, 'queryset_q': queryset_q, }
        return render(request, 'main/index.html', data)


class qualityDetailView(DetailView):
    model = Quality
    queryset = Quality.objects.all()
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        x = ['prod.', 'feas.', 'inv.', 'int.', 'flex.', 'mult.']
        prod = Quality.objects.get(pk=pk).productivity
        feas = Quality.objects.get(pk=pk).feasibility
        inv = Quality.objects.get(pk=pk).involvement
        internal = Quality.objects.get(pk=pk).internal
        flex = Quality.objects.get(pk=pk).flexibility
        mult = Quality.objects.get(pk=pk).multitasking
        y = [prod, feas, inv, internal, flex, mult]
        chart = get_hist(x, y)
        sred = round((prod + feas + inv + internal + flex + mult) / 6, 2)
        context['sred'] = sred
        context['chart'] = chart
        return context
