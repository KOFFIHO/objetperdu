from django.db import models

# Create your models here.

type_list=(
			('Carte Nationale d\'Identité (CNI)','Carte Nationale d\'Identité (CNI)'),
			('Passeport','Passeport'),
			('Attestation d\'Identité','Attestation d\'Identité'),
			('Carte scolaire','Carte scolaire'),
			('Carte bancaire','Carte bancaire/Carte magnétique'),
			('Diplome','Diplome'),
			('Livre/Cours/Cahier','Livre/Cours/Cahier'),
			('Autres','Autres')

		)

class Ville(models.Model) :
	nom = models.CharField(max_length=100)

	def __str__(self) :
		return f"{self.nom}"

	@staticmethod
	def get_all_villes():
		return Ville.objects.all()


class Document(models.Model) :
	type_de_document = models.CharField(max_length=50, choices=type_list)
	nom_du_proprietaire = models.CharField(max_length=50)
	ville = models.CharField(max_length=50)
	# ville = models.ForeignKey(Ville, on_delete = models.CASCADE)
	contact = models.CharField(max_length=10)
	photo = models.ImageField(upload_to='images/')
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def register(self) :
		self.save()


	def __str__(self) :
		return f"{self.nom_du_proprietaire}"

	@staticmethod
	def get_all_documents():
		return Document.objects.all()


