from django.shortcuts import render
from proj.models import Cidades, Doencas, Hospitais, Registros
from django.db.models import Sum

def index(request):
    reg = Registros.objects.all()
    doe = Doencas.objects.all()
    
    res = Registros.objects.values('doenca').annotate(Sum('ncasos')).order_by('doenca')
    
    context={'doe':doe, 'reg':reg, 'res':res}

    return render(request,'index.html',context)