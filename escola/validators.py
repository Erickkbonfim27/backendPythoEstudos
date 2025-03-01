import re

def cpf_invalido(cpf):
    return len(cpf) != 11

def nome_invalido(nome):
    return not nome.isalpha()

def numero_celular_invalido(numero_celular):
    modelo = r'\b\d{2} \d{5}-\d{4}\b'
    is_num_valid = re.findall(modelo, numero_celular)
    print(is_num_valid)
    return not is_num_valid


"""
#validator geral do serializer.py

def validate(self, dados):
        if len(dados['cpf']) != 11:
            raise serializers.ValidationError({'cpf':"O CPF deve ter 11 digitos"}) #aqui informamos qual o campo no formato tupla ({'campo':"mensagem"}) as aspas precisam ser esse formato
        if not dados['nome'].isalpha():
            raise serializers.ValidationError({'nome':"O nome não deve ter caracteres especiais!"})
        if len(dados['numero_celular']) != 13:
            raise serializers.ValidationError({'numero_celular':"O celular precisa ter 13 digitos"})
        return dados
        
        
#validators individuais que vão no serializer.py


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
"""