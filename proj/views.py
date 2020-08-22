from django.shortcuts import render
from proj.models import cidade, doenca, hospital, registro
from django.db.models import Sum
from django.db import connection

def index(request):
    reg = registro.objects.all()
    doe = doenca.objects.all()
    cid = cidade.objects.all()
    hos = hospital.objects.all()
    
    def sql():
        cursor = connection.cursor()
        cursor.execute("SELECT d.nome,SUM(r.ncasos) FROM proj_doenca as D LEFT JOIN proj_registro as R ON d.iddoenca=r.doenca GRoUP BY d.nome ORDER BY d.iddoenca")
        row = cursor.fetchall()
        return row
    
    row = sql()
    
    def sql2():
        cursor = connection.cursor()
        cursor.execute("SELECT c.nome,SUM(r.ncasos) FROM proj_registro as R INNER JOIN  proj_hospital as H ON r.hospital=h.idhospital INNER JOIN proj_cidade as C ON h.cidade=c.idcidade GRoUP BY c.nome ORDER BY c.idcidade")
        row = cursor.fetchall()
        return row
    
    row2 = sql2()
    
    context={'doe':doe, 'reg':reg, 'row':row, 'row2':row2, 'cid':cid, 'hos':hos}

    return render(request,'index.html',context)