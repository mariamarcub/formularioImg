from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreaFormularioImgForm
from .models import ImageModel

def index(request):
    return render(request, 'appForm/index.html', {})

def imagenes(request):
    # Si se ha enviado el formulario
    formulario_form = CreaFormularioImgForm()

    if request.method == 'POST':
        formulario_form = CreaFormularioImgForm(request.POST, request.FILES)

        # Ejecutamos la validacion
        if formulario_form.is_valid():
            formulario_form.save() # se utiliza para guardar los datos del formulario en la base de datos
            return redirect('imagenes')

    else:
        formulario_form = CreaFormularioImgForm()

    image_objects = ImageModel.objects.all() #para obtener todas las imágenes de la BD

    return render(request, 'appForm/imagenes.html', {'form': formulario_form, 'image_objects': image_objects})

def borrarImg(request, image_id):
    image = get_object_or_404(ImageModel, id=image_id) #
    # get_object_or_404 sirve para recuperar un objeto de un modelo de base de datos o
    # devolver una página de error 404 si el objeto no se encuentra.
    image.delete()
    return redirect('imagenes')


