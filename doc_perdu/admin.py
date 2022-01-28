from django.contrib import admin
from .models import *
#from .forms import DocumentCreateForm
# Register your models here.

class DocumentCreateAdmin(admin.ModelAdmin) : 
	list_display = ['type_de_document', 'nom_du_proprietaire', 
				'contact', 'photo']

	# form = DocumentCreateForm
	# list_filter = ['type_de_document']
	# search_fields = ['type_de_document', 'nom_du_proprietaire' 
	# 			]

admin.site.register(Document, DocumentCreateAdmin)
admin.site.register(Ville)
