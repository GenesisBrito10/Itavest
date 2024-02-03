# bordados/views.py

from django.shortcuts import render, redirect
from .models import Bordado
from .forms import BordadoForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import BordadoSerializer


@login_required()
def lista_bordados(request):
    bordados_na_loja = Bordado.objects.filter(status='Na Loja')
    bordados_bordando = Bordado.objects.filter(status='Bordando')
    bordados_concluidos = Bordado.objects.filter(status='Concluído')

    context = {
        'bordados_na_loja': bordados_na_loja,
        'bordados_bordando': bordados_bordando,
        'bordados_concluidos': bordados_concluidos,
    }

    return render(request, 'bordados/lista_bordados.html', context)

# bordados/views.py

login_required()
def novo_bordado(request):
    if request.method == 'POST':
        form = BordadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_bordados')
    else:
        form = BordadoForm()
    return render(request, 'bordados/novo_bordado.html', {'form': form})

login_required()
def editar_status(request, bordado_id):
    bordado = Bordado.objects.get(pk=bordado_id)
    if request.method == 'POST':
        status = request.POST['status']
        bordado.status = status
        bordado.save()
        return redirect('lista_bordados')
    return render(request, 'bordados/editar_status.html', {'bordado': bordado})


class BordadoListCreateView(generics.ListCreateAPIView):
    queryset = Bordado.objects.all()
    serializer_class = BordadoSerializer

class BordadoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bordado.objects.all()
    serializer_class = BordadoSerializer