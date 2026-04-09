from django import forms
from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=120)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        content = f'Nome: {name}\nE-mail: {email}\nAssunto: {subject}\nMessage: {message}'
        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django 2',
            body=content,
            from_email='contato@meudominio.com.br',
            to=['contato@meudominio.com.br',],
            headers={'Reply-To': email},
        )
        mail.send()
