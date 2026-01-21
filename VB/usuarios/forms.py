from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["cpf", "tipo"]

class CadastroForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput)
    cpf = forms.CharField(label="CPF", max_length=11)
    tipo = forms.ChoiceField(label="Tipo", choices=Perfil.TIPO_CHOICES)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            self.add_error("password2", "As senhas não conferem.")
        return cleaned

    def clean_cpf(self):
        cpf = self.cleaned_data["cpf"]
        if Perfil.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está cadastrado.")
        return cpf
