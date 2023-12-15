from django.shortcuts import render

def index_voti(request):
  return render(request,"home_voti.html")
def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]

    context = {
        'materie':materie
    }
    return render(request, "lista_materie.html", context)

def view_b(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    context = {
        'voti':voti
    }
   
    return render(request,"voti_studenti.html",context)

def view_c(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
            'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
            'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    media_spina=(voti["Nicola Spina"][0][1]+voti["Nicola Spina"][1][1]+voti["Nicola Spina"][2][1]+voti["Nicola Spina"][3][1]+voti["Nicola Spina"][4][1])/5
    media_gullo=(voti["Giuseppe Gullo"][0][1]+voti["Giuseppe Gullo"][1][1]+voti["Giuseppe Gullo"][2][1]+voti["Giuseppe Gullo"][3][1]+voti["Giuseppe Gullo"][4][1])/5
    media_barbera=(voti["Antonio Barbera"][0][1]+voti["Antonio Barbera"][1][1]+voti["Antonio Barbera"][2][1]+voti["Antonio Barbera"][3][1]+voti["Antonio Barbera"][4][1])/5
    context = {
        'media_spina':media_spina,
        'media_gullo':media_gullo,
        'media_barbera':media_barbera
    }
    return render(request,"media_studenti.html",context)

def view_d(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
            'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
            'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    max=0
    pos=0
    materie_max=[]
    studenti_max=[]
    for chiave in voti.keys():
        for i in range(len(voti[chiave])):
            if max<=voti[chiave][i][1]:
                max=voti[chiave][i][1]
                pos=voti[chiave][i][1]
                materie_max.append(voti[chiave][i][0])
                studenti_max.append(chiave)
    

    min=voti["Giuseppe Gullo"][0][1]
    posMin=0
    materie_min=[]
    studenti_min=[]
    for chiave in voti.keys():
        for i in range(len(voti[chiave])):
            if min>voti[chiave][i][1]:
                min=voti[chiave][i][1]
                posMin=voti[chiave][i][1]
                materie_min.append(voti[chiave][i][0])
                studenti_min.append(chiave)
    context = {
       'voto_max':pos,
       'materie_voto_max':materie_max,
       'studenti_max':studenti_max,
       'voto_min':posMin,
       'materie_voto_min':materie_min,
       'studenti_min':studenti_min
    }
    return render(request,"maxMin_voti.html",context)

