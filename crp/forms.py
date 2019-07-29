from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from crp.models import Crp


TIPO_CRP = (
		('----','----'),
        ('T', 'Estético'),
        ('E', 'Estrutural'),
        ('R', 'Revisão'),        
    )

RECOLHER_PECA = (
		('----','----'),
        ('1', 'Sim'),
        ('2', 'Não'),        
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

STATUS = (
		('----','----'),
        ('REALIZADO', 'REALIZADO'),
        ('CANCELADO', 'CANCELADO'),        
    )

LOJAS = (
		('----','----'),
        ('TDC', 'TDC'),
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

class CrpForm(forms.ModelForm):
    loja = forms.CharField(widget=forms.Select(choices=LOJAS,attrs={'class':'form-control form-control-sm'}))
    numMinuta = forms.CharField(max_length=7,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    numCrp = forms.CharField(max_length=5,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    tipo = forms.CharField(widget=forms.Select(choices=TIPO_CRP,attrs={'class':'form-control form-control-sm'}))
    zona = forms.CharField(widget=forms.Select(choices=ZONAS,attrs={'class':'form-control form-control-sm'}))
    dataPrevisaoLimite = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'dd/mm/aaaa','class':'form-control form-control-sm'}))
    recolhimento = forms.CharField(widget=forms.Select(choices=RECOLHER_PECA,attrs={'class':'form-control form-control-sm'}))
    

    class Meta:
	    model = Crp
	    fields = ['loja','numMinuta','numCrp','tipo','zona','dataPrevisaoLimite','recolhimento']