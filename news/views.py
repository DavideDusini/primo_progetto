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
  

  return render(request, "homepage.html", context)

def articoloDetailView(request, pk):
  articolo=get_object_or_404(Articolo, pk=pk)
  context = {"articolo": articolo}
  return render(request, "articolo_detail.html", context)