from django.shortcuts import render

def index(request):
	saludo = "Hola, me llamo Ramon Salazar"
	usuarios = [
		{'nombre':'Diego', 'edad':21, 'apellidos':'Barriga', 'escolaridad':'Doctorado'},
		{'nombre':'Ramon', 'edad':45, 'apellidos':'Salazar'},
		{'nombre':'Eréndira', 'edad':23, 'apellidos':'Suazo'},
		{'nombre':'Maximo', 'edad':19, 'apellidos':'Largo', 'escolaridad':'Secundaria'}
	]
	return render(request, 'landing/index.html', {
		'greeting':saludo,
		'users':usuarios
		})

def agregar(request):
	return render(request, "landing/agregar.html")