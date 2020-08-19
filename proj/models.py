from django.conf import settings
from django.db import models

class Cidades(models.Model):
    idcidade = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
        
    class Meta:
        managed = False
        verbose_name = '01.Cad.Cidade'

class Doencas(models.Model):
    iddoenca = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
        
    class Meta:
        managed = False
        verbose_name = '01.Cad.Doenca'
        
class Hospitais(models.Model):
    idhospital = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey('Cidades', db_column='cidade', on_delete=models.CASCADE)
    nleitos = models.IntegerField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        managed = False
        verbose_name = '01.Cad.Hospital'
  
class Registros(models.Model):
    idregistro = models.AutoField(primary_key = True)
    hospital = models.ForeignKey('Hospitais', db_column='hospital', on_delete=models.CASCADE)
    doenca = models.ForeignKey('Doencas', db_column='doenca', on_delete=models.CASCADE)
    dtregistro = models.DateField()
    ncasos = models.IntegerField()
    ninternacoes = models.IntegerField()
    nmortes = models.IntegerField()
    
    def __str__(self):
        return '%s' % (self.idregistro)
    
    class Meta:
        managed = False
        verbose_name = '01.Cad.Registro'