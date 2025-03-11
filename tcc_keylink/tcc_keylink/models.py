from django.db import models

class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    numero_sala = models.IntegerField()
    tipo_de_sala = models.CharField(max_length=255)

    class Meta:
        db_table = 'salas'

    def __str__(self):
        return f"Sala {self.numero_sala} - {self.tipo_de_sala}"


class Chave(models.Model):
    id_chaves = models.AutoField(primary_key=True)
    salas = models.ForeignKey(Sala, on_delete=models.CASCADE)

    class Meta:
        db_table = 'chaves'

    def __str__(self):
        return f"Chave {self.id_chaves} - Sala {self.salas.numero_sala}"


class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=255)
    telefone_funcionario = models.CharField(max_length=20, null=True, blank=True)
    endereco_funcionario = models.CharField(max_length=255, null=True, blank=True)
    funcao_funcionario = models.CharField(max_length=255)
    cpf_funcionario = models.CharField(max_length=14)
    senha = models.CharField(max_length=100)
    tipo_funcionario = models.CharField(
        max_length=20, choices=[('Quadro', 'Quadro'), ('Extra Quadro', 'Extra Quadro')]
    )

    class Meta:
        db_table = 'funcionarios'

    def __str__(self):
        return self.nome_funcionario


class RegistroSaida(models.Model):
    id_registro = models.CharField(max_length=45, primary_key=True)
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    registro_saida_horario = models.DateTimeField()

    def __str__(self):
        return f"Registro {self.id_registro} - {self.funcionario.nome_funcionario}"


class RegistroEntrada(models.Model):
    id_registro_entrada = models.AutoField(primary_key=True)
    registro_saida = models.ForeignKey(RegistroSaida, on_delete=models.CASCADE)
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    registro_entrada_horario = models.DateTimeField()

    def __str__(self):
        return f"Entrada Registro {self.id_registro_entrada}"
