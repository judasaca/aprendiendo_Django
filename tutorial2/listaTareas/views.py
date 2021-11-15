from django.shortcuts import render, redirect
from .forms import AgragarTarea
# Create your views here.

tareas= []
def home(request):
	context = {'tareas': tareas} #manda el archivo a html
	return render(request, "listaTareas/home.html", context)
def add(request):
	if request.method == 'POST':
		form = AgragarTarea(request.POST) # lee la informacion
		if form.is_valid():
			tarea = form.cleaned_data["tarea"]
			tareas.append(tarea)
			return redirect('home') #redirecciona a home
	else:
		form = AgragarTarea()

	context={'form':form}

	return render(request, "listaTareas/add.html", context)

