from django.db import models


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome
    

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    prioridade = models.CharField(max_length=20)
    data_limite = models.DateTimeField(null=True, blank=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')


    def __str__(self):
        return self.titulo