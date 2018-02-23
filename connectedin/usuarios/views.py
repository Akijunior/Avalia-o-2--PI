from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

from django.views.generic.base import View

from perfis.models import Perfil
from usuarios.forms import RegistrarUsuarioForm


class RegistrarUsuarioView(View):

    template_name = 'usuarios/registro_usuario.html'
    context = {}

    def post(self, request):

        form = RegistrarUsuarioForm(request.POST or None)
        if form.is_valid():
            usuario = form.save()
            usuario = authenticate(username=form.email, password=form.cleaned_data['password1'])
            usuario.save()
            login(request, usuario)
            self.context['form'] = form
            # dados_form = form.cleaned_data
            # usuario = User.objects.create(username=dados_form['nome'], email = dados_form['email'],
            #                               password=dados_form['senha'])
            # perfil = Perfil(nome=dados_form['nome'], telefone=dados_form['telefone'],
            #                 nome_empresa=dados_form['nome_empresa'], usuario=usuario)
            # perfil.save()


        return render(request, self.template_name, self.context)

    def get(self, request):
        return render(request, self.template_name, self.context)


def login(request):
    return redirect('index')