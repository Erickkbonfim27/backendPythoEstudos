from dns.e164 import query

from escola.models import Estudante, Curso, Matricula
from escola.serializer import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class EstudanteViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

class CursoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudanteViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #o self.kwargs pega os dados da url passada
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCursoViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer