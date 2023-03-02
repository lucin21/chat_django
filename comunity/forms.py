from django import forms
from .models import Community

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = '__all__'
        exclude = ('verify','slug', 'user')

        widgets = {
            'name':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese nombre de la comunidad',
                }
            ),
            'description':forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                }
            ),
            'slug':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese su mensaje',
                }
            ),
        }