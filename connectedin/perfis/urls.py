from django.urls import path
from .views import *
urlpatterns = [
    path('', index ,name='index'),
    path('perfil/<int:post_id>/excluir', deletar_post ,name='deletar_post'),
    path('perfil/<int:post_id>/excluido', excluir ,name='confirmar_exclusao'),
    path('perfil/<int:perfil_id>', exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar' , convidar, name='convidar'),
    path('convite/<int:convite_id>/aceitar' , aceitar, name='aceitar'),
    path('convite/<int:convite_id>/recusar' , recusar, name='recusar'),
    path('perfil/<int:perfil_id>/desfazer' , desfazer, name='desfazer'),
]
