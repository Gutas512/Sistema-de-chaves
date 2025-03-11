from django import forms
from .models import *

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['numero_sala', 'tipo_de_sala']


class ChaveForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = ['salas']


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome_funcionario', 'telefone_funcionario', 'endereco_funcionario',
                  'funcao_funcionario', 'cpf_funcionario', 'senha', 'tipo_funcionario']


class RegistroSaidaForm(forms.ModelForm):
    class Meta:
        model = RegistroSaida
        fields = ['id_registro', 'chave', 'funcionario', 'registro_saida_horario']


class RegistroEntradaForm(forms.ModelForm):
    class Meta:
        model = RegistroEntrada
        fields = ['registro_saida', 'chave', 'funcionario', 'registro_entrada_horario']
