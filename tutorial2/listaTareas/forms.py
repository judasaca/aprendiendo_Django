from django import forms

class AgragarTarea(forms.Form):
	tarea = forms.CharField() #tiene la etiqueda con el nombre de la propiedad
