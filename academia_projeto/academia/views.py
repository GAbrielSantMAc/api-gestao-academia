from django.shortcuts import render

from rest_framework import viewsets

from .models import Aluno, Matricula
from .serializers import AlunoSerializer, MatriculaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer