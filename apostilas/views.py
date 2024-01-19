from django.shortcuts import render
from .models import Apostila
from django.contrib.messages import constants
from django.contrib import messages
from django.shortcuts import redirect

def adicionar_apostilas(request):
    if request.method == 'GET':
        apostilas = Apostila.objects.filter(user=request.user)
        return render(request, 'adicionar_apostilas.html', {'apostilas': apostilas})
    
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        arquivo = request.FILES['arquivo']

        apostila = Apostila(user=request.user, titulo=titulo, arquivo=arquivo)
        apostila.save()
        messages.add_message(
            request, constants.SUCCESS, 'Apostila adicionada com sucesso.'
        )
        return redirect('/apostilas/adicionar_apostilas/')
