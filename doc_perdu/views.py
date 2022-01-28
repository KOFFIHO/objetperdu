from django.shortcuts import render, redirect
from .models import Document, Ville
from .forms import DocumentCreateForm, DocumentSearchForm
from django.core.paginator import Paginator #,EmptyPage, PageNotAnInteger

# Create your views here.
def index(request) :
	
	# context = {
	# 		'title': 'Bienvenue sur DOCUMENT PERDU.COM',
			
	# }

	return render(request, 'index.html')



def documents_liste(request) :
	# title = 'Liste des documents perdus'
	# documents_liste = Document.objects.all()
	documents = None

	villes = Ville.get_all_villes()
	villeID = request.GET.get('ville')
	
	if villeID:
		page_obj = Document.objects.filter(ville=villeID)
		paginator = Paginator(page_obj, 8) # Show 25 contacts per page.
		page_number = request.GET.get('page')
		documents = paginator.get_page(page_number)
		documents = Document.objects.filter(ville=villeID)
		
	else:
		page_obj = Document.objects.all()
		paginator = Paginator(page_obj, 8) # Show 25 contacts per page.
		page_number = request.GET.get('page')
		documents = paginator.get_page(page_number)




	form = DocumentSearchForm(request.POST or None)
	
	context = {
			'page_obj': page_obj,
			'documents':documents,
			'form':form,
	}

	
		

	return render(request, 'liste_documents.html', context)



def recherche_forms(request) :
	#documents_liste = Document.objects.all()
	villes = Ville.get_all_villes()
	message = ""
	query = request.GET.get('query')
	#ville = request.GET.get("ville")
	if not query:
		documents = Document.objects.all() 
	else:
		documents = Document.objects.filter(ville__icontains=query)
		if not documents:
			documents = Document.objects.filter(nom_du_proprietaire__icontains=query)

		if not documents :
			message = 'Aucun résultat trouvé pour %s'%query

	# if not query:
	# 	if ville !="0":
	# 		documents_liste = Document.objects.filter(ville_id=ville)
	# 	else:
	# 		 documents = Document.objects.all()

	# else:
	# 	if ville =="0" :
	# 		documents_liste = Document.objects.filter(nom_du_proprietaire__icontains=query)

	# 	elif not documents_liste.exist() :

	# 		message = 'Aucun résultat trouvé pour %s'%query

	
	context = {
				'documents':documents,
				'message':message,
				'villes':villes,
			}

	return render(request, 'liste_documents.html', context)


def deposer_documents(request) :
	villes = Ville.objects.all()
	form = DocumentCreateForm()

	if request.method == "POST" :
		ville = request.POST.get("ville")
		form = DocumentCreateForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			#form.ville.id = ville
			form.save()
			return redirect('documents_liste')
		else:
			print(form.errors)
			error = 'ok'
			form = DocumentCreateForm()

	context = {
		'form':form,
		'villes':villes,
	}



	return render(request, 'deposer_documents.html', context)


def points_depot(request) :
	
	# context = {
	# 		'title': 'Bienvenue sur DOCUMENT PERDU.COM',
			
	# }

	return render(request, 'point.html')