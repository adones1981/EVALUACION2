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


from django.shortcuts import render, get_object_or_404
from .models import Question

def question_list(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'miportafolio/question_list.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'miportafolio/question_detail.html', {'question': question})
