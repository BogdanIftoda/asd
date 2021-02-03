from .models import Task
from .serializers import TaskSerializer
from rest_framework import mixins
from rest_framework import generics
from django.shortcuts import render
from rest_framework import viewsets

class TaskList(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def homepage(request):
    return render(request, 'task/index.html')

