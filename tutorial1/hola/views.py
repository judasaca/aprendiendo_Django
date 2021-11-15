from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hola(request):
	return render(request, 'hola/index.html')
def putos(request):
	return HttpResponse("hola putos \n aoksmdoijqowie")

def saludar(request, parametro):
	context = {'name': parametro}
	return render(request,'hola/saludo.html',context)

def moneda(request):
	num = 1
	context = {'num': num}
	return render(request, 'hola/moneda.html', context)