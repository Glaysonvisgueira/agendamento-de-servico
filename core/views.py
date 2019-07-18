from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bootstrap_datepicker_plus import DateTimePickerInput
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from montagem.models import Minuta, Zona
from montagem.forms import MinutaForm, DataAuxForm


def home(request):
	return render(request,'home.html')


def login(request):
	return render(request,'login.html')

'''def listarAgendamentos(request):
	return render(request,'listar-agendamentos.html')'''

def agendar(request):
    context = {}
    template_name = 'cadastrar-agendamento.html'
    if request.method == "POST":
        form = MinutaForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://localhost:8000/')
    else:
        form = MinutaForm()
    context['form'] = form
    return render(request, template_name, context)

def listarAgendamentos(request):
    agendamentos = Minuta.objects.all()
    agendamentos_norte = Minuta.objects.filter(zona='NORTE')    
    agendamentos_sul = Minuta.objects.filter(zona='SUL')
    agendamentos_dirceu = Minuta.objects.filter(zona='DIRCEU')
    agendamentos_leste = Minuta.objects.filter(zona='LESTE')
    agendamentos_timon = Minuta.objects.filter(zona='TIMON')
    qtdNorte = Minuta.objects.filter(zona='NORTE').count()
    qtdSul = Minuta.objects.filter(zona='SUL').count()
    qtdDirceu = Minuta.objects.filter(zona='DIRCEU').count()
    qtdTimon = Minuta.objects.filter(zona='TIMON').count()
    qtdLeste = Minuta.objects.filter(zona='LESTE').count()
    template_name = 'listar-agendamentos.html'
    context = {
        'agendamentos': agendamentos,
        'agendamentos_norte' :agendamentos_norte,
        'agendamentos_sul' :agendamentos_sul,
        'agendamentos_dirceu' :agendamentos_dirceu,
        'agendamentos_leste' :agendamentos_leste,
        'agendamentos_timon' :agendamentos_timon,
        'qtdNorte': qtdNorte,
        'qtdSul': qtdSul,
        'qtdDirceu': qtdDirceu,
        'qtdTimon': qtdTimon,
        'qtdLeste': qtdLeste,
    }
    form = DataAuxForm()
    context['form'] = form
    return render(request, template_name, context)

def PostList(request):
    object_list = Minuta.objects.all()
    paginator = Paginator(object_list, 10)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'events.html',
                  {'page': page,
                   'post_list': post_list})