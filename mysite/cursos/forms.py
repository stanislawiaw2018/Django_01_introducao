from django import forms

class ContatoCurso(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvidas', widget=forms.Textarea

    )
    question = forms.BooleanField(label='Receber Email', required=False)