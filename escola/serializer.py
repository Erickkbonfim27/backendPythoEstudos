from curses.ascii import isalpha

from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula


class EstudanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudante
        fields = "__all__"


#validators individuais
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve ter 11 digitos") #aqui é a mensagem de erro do  validator personalizado, da pra mandar um objeto tmb
        return cpf
    # o nome do metodo deve seguir esse padrao validate_nomedocampo
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("O nome não deve ter caracteres especiais!")
        return nome

    def validate_numero_celular(self, numero_celular):
        if len(numero_celular) != 13:
            raise serializers.ValidationError("O celular precisa ter 13 digitos")
        return numero_celular

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