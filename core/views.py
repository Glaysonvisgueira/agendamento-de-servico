from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bootstrap_datepicker_plus import DateTimePickerInput
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from montagem.models import Minuta, Zona, DataAux
from montagem.forms import MinutaForm, DataAuxForm

ITENS_POR_PAGINA = 5; #Quantidade de objetos(agendamentos) a serem exibidos por página.


def home(request):
	return render(request,'home.html')


def login(request):
	return render(request,'login.html')

def agendar(request):
    context = {}
    template_name = 'cadastrar-agendamento.html'
    if request.method == "POST":
        form = MinutaForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/cadastrar-agendamento')
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

def editarAgendamento(request, pk):
    agendamento = get_object_or_404(Minuta, pk=pk)
    if request.method == "POST":
        form = MinutaForm(request.POST, instance=agendamento)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.save()
            return redirect('/listar-agendamentos', pk=agendamento.pk)
    else:
        form = MinutaForm(instance=agendamento)
    return render(request, 'editar-agendamento.html', {'form': form})

def PostList(request):    
    contact_list = Minuta.objects.all()
    paginator = Paginator(contact_list, ITENS_POR_PAGINA) # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    form = DataAuxForm()
    context = {
        'form':form,
        'contacts':contacts,
    }
    return render(request, 'events.html', context)