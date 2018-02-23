from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from perfis.models import Perfil, Convite, Post
from django.shortcuts import redirect


# Create your views here.


def index(request):
    posts = timeline(request, get_perfil_logado(request))

    return render(request, 'index.html', {'perfis': Perfil.objects.all(),
                                          'perfil_logado': get_perfil_logado(request),
                                          'timeline':posts, 'tamanho':posts.count()})


def exibir_perfil(request, perfil_id):
    # perfil = get(perfil_id)
    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html',
                  {'perfil': perfil,
                   'perfil_logado': get_perfil_logado(request)})


def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)

    if (perfil_logado.pode_convidar(perfil_a_convidar)):
        perfil_logado.convidar(perfil_a_convidar)

    return redirect('index')



def get_perfil_logado(request):
    perfil = Perfil.objects.get(pk=1)
    return perfil


def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


def recusar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.recusar()
    return redirect('index')


def desfazer(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil.desfazer(get_perfil_logado(request))
    return redirect('index')

def deletar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    template_name = 'excluir.html'
    return render(request, template_name, {'post':post})

def excluir(request, post_id):
    Post.objects.filter(pk=post_id).delete()
    return redirect('index')

def timeline(request, perfil_logado):
    contatos = perfil_logado.contatos.all()
    my_posts = perfil_logado.meus_posts.all()
    all_posts = Post.objects.filter(criador_do_post__in=contatos)
    all_posts=all_posts.union(all_posts,my_posts)

    return all_posts.order_by('-pk')
    #
    # posts = []
    # all_posts = Post.objects.all()
    # meus_posts = perfil_logado.meus_posts.all()
    # for i in perfil_logado