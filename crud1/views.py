# views.py
from django.shortcuts import render, redirect 
from .forms import UsuarioForm
from .models import Usuario

def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')

        # Buscar un usuario con el nombre de usuario proporcionado en tu modelo Usuario
        user = Usuario.objects.filter(nombre_usuario=username).first()

        # Verificar si se encontró un usuario y si la contraseña es correcta
        if user and user.contraseña == password:
            # Si las credenciales son correctas, verificar el tipo de usuario
            if user.tipo_usuario == 'taquillero':
                # Si el usuario es taquillero, redirigir a la interfaz_ta
                request.session['user_id'] = user.id  # Almacenar el ID del usuario en la sesión
                return redirect('interfaz_ta')
            else:
                # Si el usuario es otro tipo, redirigir a la interfaz_sa
                request.session['user_id'] = user.id  # Almacenar el ID del usuario en la sesión
                return redirect('interfaz_sa')
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # Si la solicitud no es POST, mostrar el formulario de inicio de sesión
        return render(request, 'login.html')


def interfaz_sa(request):
    usuarios = Usuario.objects.all()  # Obtener todos los usuarios de la base de datos
    return render(request, 'interfaz_sa.html', {'usuarios': usuarios})



def interfaz_ta(request):
    return render(request, 'interfaz_ta.html')
def guardar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interfaz_sa')  # Redirigir a la interfaz después de guardar el usuario
    else:
        form = UsuarioForm()
    return render(request, 'guardar_usuario.html', {'form': form})


def editar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    # Lógica para editar el usuario (puedes usar un formulario para esto)
    return render(request, 'editar_usuario.html', {'usuario': usuario})

def eliminar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    # Lógica para eliminar el usuario
    usuario.delete()
    return redirect('interfaz_sa')


