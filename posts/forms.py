from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('published','slug', 'user')

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