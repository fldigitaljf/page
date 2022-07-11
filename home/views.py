
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . models import Contato, Inscribe


def index(request):
    contatos = Contato.objects.all().values()
    inscrever = Inscribe.objects.all().values()
    template_home = loader.get_template('index.html')
    context = {
        'contatos': contatos,
        'inscrever': inscrever,
    }
    return HttpResponse(template_home.render(context, request)) 


def gravar(request):
    
    
    k = request.POST['nome1']
    m = request.POST['mail']
    n = request.POST['fone']
    o = request.POST['sobre']
    p = request.POST['text']
    contato = Contato(nome=k, email=m, telefone=n, assunto=o, texto=p)
    contato.save()
   
    #return render(request, 'index.html', {'show_modal': show_modal})
    
    return HttpResponseRedirect(reverse('index'))

# Create your views here.
def inscrever(request): 
    
    mi = request.POST['inscrib_mail']
    inscreve = Inscribe(mail_inscrito=mi)
    inscreve.save()
    return HttpResponseRedirect(reverse('index'))
    