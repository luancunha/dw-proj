from django.conf import settings
from django.db import models

class cidade(models.Model):
    idcidade = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class doenca(models.Model):
    iddoenca = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
        
class hospital(models.Model):
    idhospital = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey('cidade', db_column='cidade', on_delete=models.CASCADE)
    nleitos = models.IntegerField()
    
    def __str__(self):
        return self.nome
  
class registro(models.Model):
    idregistro = models.AutoField(primary_key = True)
    hospital = models.ForeignKey('hospital', db_column='hospital', on_delete=models.CASCADE)
    doenca = models.ForeignKey('doenca', db_column='doenca', on_delete=models.CASCADE)
    dtregistro = models.DateField()
    ncasos = models.IntegerField()
    ninternacoes = models.IntegerField()
    nmortes = models.IntegerField()
    
    def __str__(self):
        return '%s' % (self.idregistro)