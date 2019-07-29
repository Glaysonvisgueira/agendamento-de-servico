from django.contrib import admin

from montagem.models import Minuta, Zona
from crp.models import Crp

class MinutaAdmin(admin.ModelAdmin):

	list_display = ['id','loja','numMinuta','cliente','dataAgendamento','zona','turnoAgendamento','status']
	search_fields =['loja','numMinuta','cliente','dataAgendamento','zona','turnoAgendamento','status']	

admin.site.register(Minuta, MinutaAdmin)

class CrpAdmin(admin.ModelAdmin):	
	list_display = ['loja','numMinuta','numCrp','tipo','zona','dataPrevisaoLimite','recolhimento','recolhida','status']
	search_fields =['loja','numMinuta','numCrp','tipo','zona','dataPrevisaoLimite','recolhimento','recolhida','status']	

admin.site.register(Crp, CrpAdmin)