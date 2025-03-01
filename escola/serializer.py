from curses.ascii import isalpha

from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, numero_celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudante
        fields = "__all__"

    #validator geral com os dados d validator.py
    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve ter 11 digitos!"})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':"O Nome deve ter somente caracteres alfa numericos!"})
        if numero_celular_invalido(dados['numero_celular']):
            raise serializers.ValidationError({'numero_celular':"O numero de celular precisa ter 13 digitos"})
        return dados


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"


class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='Curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model =  Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='Estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_nome',]