from django.shortcuts import render, redirect, get_object_or_404
from.models import Producto
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

import cv2 
import os

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()      #Creando una instancia
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Conctacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')

@permission_required('app.add_producto')
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            #messages.success(request, "Producto registrado")
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'app/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
    product = Producto.objects.all()

    data = {
        'product': product
    }

    return render(request, 'app/producto/listar.html', data)

@permission_required('app.delete_producto')
def modificar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_producto")
        data["form"] = formulario

    return render(request, 'app/producto/modificar.html', data)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_producto")

def registro(request):
    data = {
        "form": CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario        
    return render(request, 'registration/registro.html', data)

def facial(request):
    dataPath = 'C:/Users/Cristian/tienda/app/Guardar' # Ruta de la carpeta
    imagePaths = os.listdir(dataPath)
    #print('imagePaths=', imagePaths)

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    face_recognizer.read('modeloLBPHFace.xml') 

    cap = cv2.VideoCapture(0) #Video para estraer rostro
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read() 
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()   

        faces = faceClassif.detectMultiScale(gray,1.3,5) 

        for (x,y,w,h) in faces:  
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)


            cv2.putText(frame,'{}' .format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

# EigenFaces
            if result[1] < 70:
                login(request)
                messages.success(request, "te has registrado correctamente")
                cv2.putText(frame,'Cris'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2) 
      
        cv2.imshow('frame',frame)
 
        k = cv2.waitKey(1)
        if k == 27:
            break

        cap.release() 
        cv2.destroyAllWindows()
    return render(request, 'registration/registro.html') 