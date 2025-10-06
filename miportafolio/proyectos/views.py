from django.shortcuts import render

def inicio(request):
    return render(request, "proyectos/inicio.html")

def lista_proyectos(request):
    proyectos = [
        {"titulo": "Proyecto 1", "descripcion": "Descripción del proyecto 1"},
        {"titulo": "Proyecto 2", "descripcion": "Descripción del proyecto 2"},
        {"titulo": "Proyecto 3", "descripcion": "Descripción del proyecto 3"},
    ]
    return render(request, "proyectos/lista_proyectos.html", {"proyectos": proyectos})

