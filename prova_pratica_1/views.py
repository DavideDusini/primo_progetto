from django.shortcuts import render
import random as r
# Create your views here.
def index(request):
    return render(request, "index_prova.html")

def somma(request):
    var1=r.randrange(1,10,1)
    var2=r.randrange(1,10,1)
    somma=var1+var2
    context={
        'var1':var1,
        'var2':var2,
        'somma': somma
    }
    return render(request,'maxmin.html',context)

def media(request):
    list=[]
    somma=0
    for i in range(30):
        list.append(r.randrange(1,10,1))
        somma+=list[i]
    media=somma/len(list)
    context={
        'list':list,
        'media':media
    }
    return render(request, 'media.html',context)

def voti(request):

    context={
        'voti': {'studente1': 8, 'studente2':7, 'studente3':5, 'studente4': 3, 'studente5': 8}
    }
    return render(request,'voti.html',context)