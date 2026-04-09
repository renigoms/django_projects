from django.contrib import messages
from django.shortcuts import render

from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    # Colocamos 'request.POST or None' pois o request pode ter dados ou não
    # Vai ter dados quando o botão de submit for acionado
    # Não vai ter dados quando abrir a página
    form = ContactForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            # Isso é o que vai fazer o {% bootstrap_messages %} funcionar
            messages.success(request, 'E-mail enviado com sucesso!')
            # form = ContactForm(request.POST or None)
            form = ContactForm()
        else:
            messages.error(request, 'Erro ao enviar a mensagem!')
    return render(request,
                  'core/contact.html',
                  {'form':form})

def product(request):
    return render(request, 'core/product.html')