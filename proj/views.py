from django.shortcuts import render
from proj.models import cidade, doenca, hospital, registro
from django.db.models import Sum
from django.db import connection

def index(request):
    reg = registro.objects.all()
    doe = doenca.objects.all()
    
    def sql():
        cursor = connection.cursor()
        cursor.execute("SELECT d.nome,r.ncasos FROM proj_doenca as D LEFT JOIN proj_registro as R ON d.iddoenca=r.doenca")
        row = cursor.fetchall()
        return row
    
    row = sql()
    
    res = registro.objects.values('doenca').annotate(Sum('ncasos')).order_by('doenca')
    
    context={'doe':doe, 'reg':reg, 'res':res, 'row':row}

    return render(request,'index.html',context)