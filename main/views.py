from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Car, Caracteristicas, Destacados
from .forms import CreateNewCar
from django.contrib.auth.decorators import login_required

# Create your views here.

def loguear(req): 

    if req.method == 'POST': 
        user = authenticate(req, username=req.POST['username'], password=req.POST['password']) # verificamos si el usuario y pw son válidos

        if not user: 
            return HttpResponse('Usuario o contraseña inválido.')

        login(req, user) # <- guardamos sesión

        return redirect('modelos') 

    return render(req, 'login.html', {
        "name": "Ingresar", 
        "form": AuthenticationForm
    })

@login_required
def desloguear(req): 
    logout(req)
    return redirect('modelos')   


def modelos(req): 
    return render(req, 'modelos.html', {
        "name": "Modelos", 
        "modelos": list(Car.objects.values())
    })

@login_required
def add_car(req): 
        
    if req.method == 'POST': 
        try: 
            Car.objects.create(
                name=req.POST['name'], 
                title=req.POST['title'],
                category=req.POST['category'], 
                description=req.POST['description'],
                year=req.POST['year'], 
                price=req.POST['price'], 
                image=req.FILES['image']
            ).save()
        except: 
            return HttpResponse('No se pudo guardar el vehículo')
        else: 
            return redirect('modelos')
 
    return render(req, 'add_car.html', {
        "name": "Agregar vehículo", 
        "form": CreateNewCar
    })

@login_required
def edit_car(req, id_veh): 

    car = Car.objects.get(pk=id_veh) # se obtiene el set de datos que pertenece a la pk que le pasamos
    form = CreateNewCar(instance=car) # se setean esos datos en un nuevo formulario para editarlos

    if req.method == 'POST': 
        form = CreateNewCar(req.POST, instance=car)
        try:
            form.save()
        except: 
            return HttpResponse('Error')
        else: 
            return redirect('modelos') 
            

    return render(req, 'edit_car.html', {
        "name": "Editar vehículo", 
        "form": form
    })

@login_required
def delete_car(req, id_veh): 
    
    try: 
        car = Car.objects.get(pk=id_veh)
    except: 
        return HttpResponse('El vehículo no existe.')
    else: 
        car.delete()
        return redirect('modelos')
    
 
def filtro_autos(req, id): 
    
    autos = Car.objects.filter(category=id)
    name = ['Autos', 'Pickups y Comerciales', 'SUVs y Crossovers']

    return render(req, 'modelos.html', {
        "name": name[id - 1],
        "modelos": list(autos),
    })

def menor_precio(req): 
    
    autos = Car.objects.order_by('price').values()

    return render(req, 'modelos.html', {
        "name": 'Modelos',
        "modelos": list(autos)
    })

def menor_precio_x_categoria(req, id): 

    autos = Car.objects.filter(category=id).order_by('price')
    name = ['Modelos', 'Autos', 'Pickups y Comerciales', 'SUVs y Crossovers']

    return render(req, 'modelos.html', {
        "name": name[id],
        "modelos": list(autos),
    })



def mayor_precio(req): 
    
    autos = Car.objects.order_by('-price')

    return render(req, 'modelos.html', {
        "name": 'Modelos',
        "modelos": list(autos)
    })

def mayor_precio_x_categoria(req, id): 

    autos = Car.objects.filter(category=id).order_by('-price')
    name = ['Modelos', 'Autos', 'Pickups y Comerciales', 'SUVs y Crossovers']

    return render(req, 'modelos.html', {
        "name": name[id],
        "modelos": list(autos),
    })


def mas_viejo(req): 
    
    autos = Car.objects.order_by('-year')

    return render(req, 'modelos.html', {
        "modelos": list(autos)
    })

def mas_viejo_x_categoria(req, id): 

    autos = Car.objects.filter(category=id).order_by('-year')
    name = ['Modelos', 'Autos', 'Pickups y Comerciales', 'SUVs y Crossovers']

    return render(req, 'modelos.html', {
        "name": name[id],
        "modelos": list(autos),
    })


def mas_nuevo(req): 
    
    autos = Car.objects.order_by('year')

    return render(req, 'modelos.html', {
        "modelos": list(autos)
    })

def mas_nuevo_x_categoria(req, id): 

    autos = Car.objects.filter(category=id).order_by('year')
    name = ['Modelos', 'Autos', 'Pickups y Comerciales', 'SUVs y Crossovers']

    return render(req, 'modelos.html', {
        "name": name[id],
        "modelos": list(autos),
    })

def ficha_modelo(req, name_car): 

    auto = Car.objects.filter(name=name_car)
    auto = list(auto)[0]

    items_caract = Caracteristicas.objects.filter(car_id=auto.id)
    items_destac = Destacados.objects.filter(car_id=auto.id)

    return render(req, 'ficha_modelo.html', {
        "name": name_car, 
        "db_car": auto, 
        "caracteristicas": items_caract, 
        "destacados": items_destac,
    })
