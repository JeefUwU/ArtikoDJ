from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request,'Usuario/index.html')

def screen1(request):
    Productos = Producto.objects.all()
    data ={
        'Productos': Productos
    }
    return render(request, 'Usuario/screen1.html', data)

def user(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = user.objects.get(username=username)
        #post = user.post.all()
    else:
       # post = current_user.posts.all()
        user= current_user
    return render(request, 'Usuario/user.html', {'user':user})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect('screen1')
        else:
            messages.error(request, "Has tenido un error al iniciar sesión")
            return redirect('login_user')
    else:
        return render(request, 'Usuario/login.html')

def SignUp(request):
    if request.method != "POST":
        return render(request, 'Usuario/registro.html')
    else:
        nombre = request.POST.get('nombre')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Crea un nuevo objeto de usuario y establece los valores
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = nombre
        user.save()

        messages.success(request, "Cuenta creada exitosamente")

        return redirect('login_user')

    return render(request, 'Usuario/registro.html')

def SignOut(request):
    pass

def post(request):
    current_user = get_object_or_404 (User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'post enviado')
            return redirect('user')
    else:
        form =PostForm()
    return render(request, 'Usuario/post.html', {'form': form})


def shop(request):
    return render(request, 'Usuario/shop.html')

def crud(request):
    Usuario = Usuario,object.all()
    context = {'Usuario': Usuario}
    return render(request,'Usuario/Usuarios_list.hmtl', context)

def carrito(request):
    return render(request,'Usuario/carrito.html')