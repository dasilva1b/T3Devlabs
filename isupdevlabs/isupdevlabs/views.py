"""Views donde estan las funciones que procesan la solicitud del usuario
Autor: Carlos Da Silva(10-10175)

"""



from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
import urllib2


def home(request):
  """Simplemente retorna el request para abrir la pagina de inicio o index.
  
  """
  return render (request,'index.html')
  
def consultar_pagina(request):
  """Dada una pagina y el protocolo, revisa si dicha pagina esta funcionante
     a traves del uso de las funciones del modulo urllib2 y la captura de
     excepcines   
     
  """
  #Obtenemos lo solicitado en el formulario
  pagina=request.POST['pagina'];
  protocolo=request.POST['protocol'];
  
  if (not('http://' in pagina)):
    #Le agregamos el protocolo
    pagina=protocolo+pagina;
    
  try:
    estado=urllib2.urlopen(pagina,timeout=8).getcode()
    if (estado == 200):
      return render (request, 'exitopagina.html')
  except IOError:
    return render (request, 'error.html')
    