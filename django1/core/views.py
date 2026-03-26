from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "curso" : "Programação web com django !",
        "outro": "Django é massa para um caralho !"
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')