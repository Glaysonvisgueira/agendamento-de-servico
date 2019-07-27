from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from montagem.models import Minuta, Zona, DataAux


LOJAS = (
		('----','----'),
        ('TES', 'TES'),
        ('TEU', 'TEU'),
        ('TMA', 'TMA'),
        ('TPI', 'TPI'),
        ('TMO', 'TMO'),
        ('TEZ', 'TEZ'),
        ('TED', 'TED'),
        ('TPP', 'TPP'),
        ('TIM', 'TIM'),
        ('TEC', 'TEC'),
        ('RTT', 'RTT'),
        ('TSJ', 'TSJ'),
    )

ZONAS = (
		('----','----'),
        ('SUL', 'SUL'),
        ('DIRCEU', 'DIRCEU'),
        ('NORTE', 'NORTE'),
        ('LESTE', 'LESTE'),
        ('TIMON', 'TIMON'),
        ('R.LESTE', 'R.LESTE'),
        ('R.NORTE', 'R.NORTE'),
        ('R.SUL', 'R.SUL'),
        ('R.DIRCEU', 'R.DIRCEU'),
        ('R.TIMON', 'R.TIMON'),
    )

TURNO_DISPONIVEL = (
		('----','----'),
        ('MANHA', 'MANHA'),
        ('TARDE', 'TARDE'),
        ('DURANTE DIA', 'DURANTE DIA'),
    )

STATUS = (
        ('REALIZADO', 'REALIZADO'),
        ('AGENDADO', 'AGENDADO'),
        ('CANCELADO', 'CANCELADO'),        
    )

class MinutaForm(forms.ModelForm):
    loja = forms.CharField(widget=forms.Select(choices=LOJAS,attrs={'class':'form-control'}))
    numMinuta = forms.CharField(max_length=7,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Número da minuta'}))
    cliente = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o nome do cliente'}))
    zona = forms.CharField(widget=forms.Select(choices=ZONAS,attrs={'class':'form-control'}))
    dataAgendamento = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'DD/MM/AAAA'}))
    turnoAgendamento = forms.CharField(widget=forms.Select(choices=TURNO_DISPONIVEL,attrs={'class':'form-control'}))
    status = forms.CharField(widget=forms.Select(choices=STATUS,attrs={'class':'form-control'}))    

    class Meta:
	    model = Minuta
	    fields = ['loja','numMinuta','cliente','zona','dataAgendamento','turnoAgendamento','status']

class DataAuxForm(forms.ModelForm):
    dataInicio = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'Início'}))
    dataFim = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'Fim'}))
    class Meta:
        model = DataAux
        fields = ['dataInicio','dataFim']
