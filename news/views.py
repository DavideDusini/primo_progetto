from django.shortcuts import HttpResponse, render, get_object_or_404
from .models import *
# Create your views here.
def home(request):
  """  a = ""
    g = ""
    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")

    for gio in Giornalista.objects.all():
        g+= (gio.nome + "<br>")
    response ="Articolo:<br>"+ a + "<br>Giornalisti:<br>"+ g"""
  
  #---------------
  """
  a = []
  g = []
  for art in Articolo.objects.all():
      a.append(art.titolo)
  for gio in Giornalista.objects.all():
      g.append(gio.name)

  response = str(a) + "<br>" + str(g)
  """
  articoli = Articolo.objects.all()
  giornalisti = Giornalista.objects.all()
  context = {"articoli": articoli, "giornalisti": giornalisti}
  print(context)
  

  return render(request, "homepage_articoli.html", context)

def articoloDetailView(request, pk):
  articolo=get_object_or_404(Articolo, pk=pk)
  context = {"articolo": articolo}
  return render(request, "articolo_detail.html", context)

def listaArticoli(request, pk):
  articoli = Articolo.objects.filter(giornalista_id=pk)
  context = {
    'articoli': articoli,
  }
  return render(request, 'lista_articoli.html', context)


def listaArticolo(request, pk=None):
  articoli = Articolo.objects.all()
  context = {
    'articoli': articoli,
  }
  return render(request, 'lista_articoli.html', context)

def queryBase(request):
  #1. Tutti gli articoli scritti da giornalisti di un certo cognome:
  articoli_cognome = Articolo.objects.filter(giornalista_cognome='Rossi')
  #2. Totale
  numero_totale_articoli = Articolo.objects.count()

  #3.Contare il numero di articoli scritti da un giornalista specifico:
  giornalista_3 = Giornalista.objects.get(id=3)
  numero_articoli_giornalista_3 = Articolo.objects.filter(giornalista = giornalista_3).count()

  #4. Ordinare gli articoli per numero di visualizzazioni in ordine decrescente:
  articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')

  #5. tutti gli articoli che non hanno visualizzazioni:
  articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)

  #6. articolo più visualizzato
  articolo_piu_visualizzato = Articolo.objects.filter('-visualizzazioni').first()