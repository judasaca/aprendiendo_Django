from django.urls import path
from . import views
urlpatterns = [
	path('',views.hola, name = 'hola'),
	path('putos/',views.putos, name = 'putos'),
	#path('<str:parametro>/', views.saludar, name= 'saludo'),
	path('moneda/', views.moneda, name= 'moneda')
]