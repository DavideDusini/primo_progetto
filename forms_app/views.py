from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormContatto
from .models import Contatto

from django.shortcuts  import get_object_or_404,redirect

from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.decorators import login_required

def contatti(request):
    if request.method == "POST":
        form = FormContatto(request.POST)
        if form.is_valid():
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)
            return HttpResponse("<h1>Grazie di averci contattato!</h1>")
    else:
        form=FormContatto()
    context = {"form":form}
    return render(request, "contatto.html", context)

def listaContatti(request):
    contatti = Contatto.objects.all()
    context = {'contatti':contatti}
    return (request, "listaContatti.html",context)

@login_required(login_url="/account/login")
def modifica_contatto (request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "GET":
        form = FormContatto(instance=contatto)
        if form.is_valid():
            form.save()
            return redirect('forms_app:listaContatti')
    context={'form': form, 'contatto':contatto}
    return render(request, 'modifica_contatto.html',context)

@staff_member_required(login_url="/account/login")
def elimina_contatto(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "POST":
        contatto.delete()
        return redirect('forms_app:listaContatti')
    context = {'contatto':contatto}
    return render(request, 'elimina_contatto.html', context)
