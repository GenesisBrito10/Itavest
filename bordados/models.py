from django.db import models
from django.utils import timezone


class Bordado(models.Model):
    Nome = models.CharField(max_length=100)
    Tamanho = models.CharField(max_length=2, choices=[
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
        ('XG', 'XG'),
    ])
    
    Quantidade = models.PositiveIntegerField(default=0)
    Status = models.CharField(max_length=20, choices=[
        ('Na Loja', 'Na Loja'),
        ('Bordando', 'Bordando'),
        ('Pronto', 'Pronto'),
    ])

    Data = models.DateTimeField(default=timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M'), editable=False)
    Telefone = models.CharField(max_length=15, blank=True, null=False,verbose_name='WhatsApp',help_text='<span style="font-size: larger;">Não coloque o 9 no inicio</span>')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, verbose_name='Registrado Por',null=True, editable=False)


    def __str__(self):
        return f"{self.Nome} | Tamanho: {self.Tamanho} | Quantidade: {self.Quantidade} | Status: {self.Status}"
