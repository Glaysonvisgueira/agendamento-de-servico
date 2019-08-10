from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bootstrap_datepicker_plus import DateTimePickerInput
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date, timedelta


from crp.models import Crp
from crp.forms import CrpForm, DataChegadaPecaForm, DataEnvioSetorEntregaForm, DataConclusaoForm, DataRecebimentoSetorEntregaForm, StatusForm


def is_valid_queryparam(param):
    return param != '' and param is not None 

def cadastrar_crp(request):
    context = {}    
    template_name = 'cadastro-crp.html'
    if request.method == "POST":
        form = CrpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://localhost:8000/crp/cadastrar-crp/')
    else:
        form = CrpForm()
    context['form'] = form
    return render(request, template_name, context)

def relatorio_de_crps_pendentes(request):    
    crps = Crp.objects.all().exclude(status='REALIZADO').exclude(status='CANCELADO').order_by('dataPrevisaoLimite')    
    data_atual = date.today()
    data_alerta = data_atual + timedelta(days=3)
    template_name = 'relatorio-de-crps.html' 
    tipo_crp = request.GET.get('tipo_crp')  
    if is_valid_queryparam(tipo_crp):
        crps = crps.filter(tipo=tipo_crp)
    context = {
        'crps': crps,
        'data_atual': data_atual,
        'data_alerta': data_alerta,  
    }

    return render(request, template_name, context)

#Form para cadastrar a data de chegada da peça
def editar_chegada_peca(request, pk):
    crp = get_object_or_404(Crp, pk=pk)
    if request.method == "POST":
        form = DataChegadaPecaForm(request.POST, instance=crp)        
        if form.is_valid():
            crp = form.save(commit=False)            
            crp.save()
            return redirect('http://localhost:8000/crp/relatorio-de-crps-pendentes/', pk=crp.pk)
    else:
        form = DataChegadaPecaForm(instance=crp)

    return render(request, 'editar-chegada-peca.html', {'form': form})

#Form para cadastrar a data de envio da CRP para o setor de entrega
def envio_setor_entrega(request, pk):
    crp = get_object_or_404(Crp, pk=pk)
    if request.method == "POST":
        form = DataEnvioSetorEntregaForm(request.POST, instance=crp)        
        if form.is_valid():
            crp = form.save(commit=False)            
            crp.save()
            return redirect('http://localhost:8000/crp/relatorio-de-crps-pendentes/', pk=crp.pk)
    else:
        form = DataEnvioSetorEntregaForm(instance=crp)

    return render(request, 'data-envio-setor-entrega.html', {'form': form})


#Form para cadastrar a data de recebimento da CRP do setor de entrega
def data_recebimento_entrega(request, pk):
    crp = get_object_or_404(Crp, pk=pk)
    if request.method == "POST":
        form = DataRecebimentoSetorEntregaForm(request.POST, instance=crp)        
        if form.is_valid():
            crp = form.save(commit=False)            
            crp.save()
            return redirect('http://localhost:8000/crp/relatorio-de-crps-pendentes/', pk=crp.pk)
    else:
        form = DataRecebimentoSetorEntregaForm(instance=crp)

    return render(request, 'data-recebimento-crp-entrega.html', {'form': form})


#Form para cadastrar a data de conclusão da CRP
def data_conclusao_crp(request, pk):
    crp = get_object_or_404(Crp, pk=pk)
    if request.method == "POST":
        form = DataConclusaoForm(request.POST, instance=crp)
        form1 = StatusForm(request.POST, instance=crp)        
        if form.is_valid():
            crp = form.save(commit=False)           
            crp.save()
            crp = form1.save(commit=False)           
            crp.save()
            
            return redirect('http://localhost:8000/crp/relatorio-de-crps-pendentes/', pk=crp.pk)
    else:
        form = DataConclusaoForm(instance=crp)
        form1 = StatusForm(instance=crp)


    return render(request, 'data-conclusao-crp.html', {'form': form,'form1':form1})

