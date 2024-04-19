from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormContatto

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
