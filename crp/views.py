from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bootstrap_datepicker_plus import DateTimePickerInput
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date


from crp.models import Crp
from crp.forms import CrpForm



def is_valid_queryparam(param, param2):
    return param != '' and param is not None 

def cadastrar_crp(request):
    context = {}
    data_atual = date.today()
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
    crps = Crp.objects.all().exclude(status='REALIZADO').exclude(status='CANCELADO')  
    data_atual = date.today()
    template_name = 'relatorio-de-crps.html'         
    context = {
        'crps': crps,
        'data_atual':data_atual,
    }    
    return render(request, template_name, context)