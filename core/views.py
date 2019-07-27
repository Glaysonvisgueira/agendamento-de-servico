from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bootstrap_datepicker_plus import DateTimePickerInput
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from montagem.models import Minuta, Zona, DataAux
from montagem.forms import MinutaForm, DataAuxForm

'''Verificar se o campos datepicker são válidos'''
def is_valid_queryparam(param):
    return param != '' and param is not None 


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
    agendamentos = Minuta.objects.all().order_by('dataAgendamento')
    agendamentos_norte = Minuta.objects.filter(zona='NORTE')    
    agendamentos_sul = Minuta.objects.filter(zona='SUL')
    agendamentos_dirceu = Minuta.objects.filter(zona='DIRCEU')
    agendamentos_leste = Minuta.objects.filter(zona='LESTE')
    agendamentos_timon = Minuta.objects.filter(zona='TIMON')
    qtdNorte = Minuta.objects.filter(zona='NORTE').count()
    contadorAgendamentos = Minuta.objects.all().count()
    qtdDirceu = Minuta.objects.filter(zona='DIRCEU').count()
    qtdTimon = Minuta.objects.filter(zona='TIMON').count()
    qtdLeste = Minuta.objects.filter(zona='LESTE').count()  
    template_name = 'listar-agendamentos.html'
    data_inicio_query = request.GET.get('date_min')
    data_final_query = request.GET.get('date_max')
    zona_escolhida = request.GET.get('zona_escolhida')

    if is_valid_queryparam(data_inicio_query):
        if zona_escolhida == '' or zona_escolhida == None:
            agendamentos = agendamentos.filter(dataAgendamento__gte=data_inicio_query)
            contadorAgendamentos = Minuta.objects.filter(dataAgendamento__gte=data_inicio_query).count() #To fix: Só se baseia na data inicial.           
        else:
            agendamentos = agendamentos.filter(dataAgendamento__gte=data_inicio_query).filter(zona=zona_escolhida)
            contadorAgendamentos = Minuta.objects.filter(dataAgendamento__gte=data_inicio_query).filter(zona=zona_escolhida).count()
    if is_valid_queryparam(data_final_query): 
        agendamentos = agendamentos.filter(dataAgendamento__lte=data_final_query)
    context = {
        'agendamentos': agendamentos,
        'agendamentos_norte' :agendamentos_norte,
        'agendamentos_sul' :agendamentos_sul,
        'agendamentos_dirceu' :agendamentos_dirceu,
        'agendamentos_leste' :agendamentos_leste,
        'agendamentos_timon' :agendamentos_timon,
        'qtdNorte': qtdNorte,
        'contadorAgendamentos':contadorAgendamentos,
        'qtdDirceu': qtdDirceu,
        'qtdTimon': qtdTimon,
        'qtdLeste': qtdLeste,
    }    
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