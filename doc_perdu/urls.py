from django.urls import path, include
from .views import index, documents_liste, deposer_documents, recherche_forms, points_depot
# documents_liste, deposer_documents, depot_succes,
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', index, name='index'),
    path('liste_documents/', documents_liste, name='documents_liste'),
    path('deposer_documents/', deposer_documents, name='deposer_documents'),
    path('recherche_forms/', recherche_forms, name='recherche_forms'),
    path('points_depot/', points_depot, name='points_depot'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

