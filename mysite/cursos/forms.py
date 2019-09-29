from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContatoCurso(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvidas', widget=forms.Textarea

    )
    question = forms.BooleanField(label='Receber Email', required=False)

    def send_mail(self, curso):
        subject = 'Curso: %s Contato' % curso
        message = 'Nome: %(name)s; E-mail: %(email)s; %(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        message = message % context
        send_mail(
            subject, message, settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL]
        )