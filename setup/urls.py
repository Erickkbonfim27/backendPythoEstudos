from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudanteViewSet,ListaMatriculaCursoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudanteViewSet.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculaCursoViewSet.as_view())
]

#As requisições precisam ter a / depois pra funcionar tanto get quanto as outras, exemplo
# POST http://127.0.0.1:8000/estudates -> vai falhar
# POST http://127.0.0.1:8000/estudates/ -> vai funcionar perfeitamente
# essa merda de / depois é bem importante, comentário adicionado
# meia hora de tomação de cu pra descobrir sabosta de erro
