from django.shortcuts import render
from proj.models import cidade, doenca, hospital, registro
from django.db.models import Sum
from django.db import connection

def index(request):
    reg = registro.objects.all()
    doe = doenca.objects.all()
    cid = cidade.objects.all()
    
    def sql():
        cursor = connection.cursor()
        cursor.execute("SELECT d.nome,SUM(r.ncasos) FROM proj_doenca as D LEFT JOIN proj_registro as R ON d.iddoenca=r.doenca GRoUP BY d.nome ORDER BY d.iddoenca")
        row = cursor.fetchall()
        return row
    
    row = sql()
    
    def sql2():
        cursor = connection.cursor()
        cursor.execute("SELECT hospital,SUM(ncasos) FROM proj_registro GRoUP BY hospital;")
        row = cursor.fetchall()
        return row
    
    row2 = sql2()
    
    context={'doe':doe, 'reg':reg, 'row':row, 'row2':row2, 'cid':cid}

    return render(request,'index.html',context)