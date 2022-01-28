from django import forms
from django.forms import TextInput
from .models import Document

type_list=(
			('CNI','Carte Nationale d\'Identité (CNI)'),
			('Passeport','Passeport'),
			('Attest','Attestation d\'Identité'),
			('Carte scolaire','Carte scolaire'),
			('Carte bancaire','Carte bancaire/Carte magnétique'),
			('Diplome','Diplome'),
			('Livre','Livre/Cours/Cahier'),
			('Autres','Autres')

		)


class DocumentCreateForm(forms.ModelForm) :
	class Meta :
		model = Document
		fields = ['type_de_document', 'nom_du_proprietaire', 'contact', 'photo','ville']
		widgets = {
			'ville': TextInput(attrs={'placeholder':'Dans quelle ville avez-vous trouvé le Document?', 'class':'form-control'}),
			'nom_du_proprietaire': TextInput(attrs={'placeholder':'Nom du proprietaire','class':'form-control'}),
			'contact': TextInput(attrs={'placeholder':'225 XX XX XX XX XX (Votre numéro de téléphone)','class':'form-control'}),

		}

	
class DocumentSearchForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ['nom_du_proprietaire']
