from django.db import models

LOJAS = (        
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

TURNO_DISPONIVEL = (
        ('MANHA', 'MANHA'),
        ('TARDE', 'TARDE'),
        ('DURANTE DIA', 'DURANTE DIA'),
    )

ZONAS = (
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
        ('REALIZADO', 'REALIZADO'),
        ('AGENDADO', 'AGENDADO'),
        ('CANCELADO', 'CANCELADO'),        
    )

TIPO = (
        ('T', 'T'),
        ('E', 'E'),
        ('CANCELADO', 'CANCELADO'),        
    )

class Minuta(models.Model):
	id = models.AutoField(primary_key=True)
	loja = models.CharField('Loja:', choices=LOJAS,max_length = 3, blank=False)
	numMinuta = models.CharField('Minuta:', max_length = 7, blank=False)
	cliente = models.CharField('Cliente:', max_length = 150, blank = False)
	created_at = models.DateTimeField('Criado em',auto_now_add = True)
	updated_at = models.DateTimeField('Atualizado em',auto_now = True)
	zona = models.CharField('Zona:', choices=ZONAS,max_length = 8, blank=False)
	dataAgendamento = models.DateField('Data de agendamento:', blank=False)
	turnoAgendamento = models.CharField('Turno de agendamento:', choices=TURNO_DISPONIVEL,max_length = 11, blank=False,default='DURANTE DIA')
	status = models.CharField('Status de montagem:', choices=STATUS,max_length = 9, blank=True)
    
	def __str__(self):
		return self.loja 
		
	class Meta:
		verbose_name = "Minuta"
		verbose_name_plural = "Minutas"
		ordering = ['id','loja','numMinuta','cliente']	


class Zona(models.Model):	

	id = models.AutoField(primary_key=True)
	zona = models.CharField('Zona:', choices=ZONAS,max_length = 8)
	 
	def __str__(self):
		return self.zona

	class Meta:
		verbose_name = "Zona"
		verbose_name_plural = "Zonas"
		ordering = ['id','zona']

class DataAux(models.Model):
    dataInicio = models.DateField(blank = True)
    dataFim = models.DateField(blank = True)
