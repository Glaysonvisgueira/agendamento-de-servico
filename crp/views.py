from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bootstrap_datepicker_plus import DateTimePickerInput
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from crp.models import Crp
from crp.forms import CrpForm

# Create your views here.
def relatorio_de_crps(request):
	return render(request,'relatorio-de-crps.html')

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