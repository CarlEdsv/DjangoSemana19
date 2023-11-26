from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

# Definición de un formulario personalizado basado en UserCreationForm
class NewUserForm(UserCreationForm):
    # Campo adicional para el correo electrónico
    email = forms.EmailField(required=True)
    # Campo para seleccionar el grupo al que pertenece el usuario
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label='Grupo')

    class Meta:
        model = User
        # Campos que se incluirán en el formulario
        fields = ("username", "email", "password1", "password2", "group")

    # Método para guardar el usuario
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            # Guardar el usuario en la base de datos
            user.save()
            user.groups.add(self.cleaned_data['group'])
        return user
