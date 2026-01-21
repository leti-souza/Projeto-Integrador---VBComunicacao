from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Perfil
from .forms import CadastroForm, UserUpdateForm, PerfilUpdateForm


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('home')
        return render(request, 'usuarios/login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'usuarios/login.html')


def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            # cria o Perfil com cpf e tipo (obrigatórios)
            Perfil.objects.create(
                user=user,
                cpf=form.cleaned_data["cpf"],
                tipo=form.cleaned_data["tipo"]
            )

            return redirect('/login/')
    else:
        form = CadastroForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})


@login_required
def perfil(request):
    perfil_obj = get_object_or_404(Perfil, user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = PerfilUpdateForm(request.POST, instance=perfil_obj)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect("perfil")
    else:
        user_form = UserUpdateForm(instance=request.user)
        perfil_form = PerfilUpdateForm(instance=perfil_obj)

    return render(request, "usuarios/perfil.html", {
        "user_form": user_form,
        "perfil_form": perfil_form,
    })