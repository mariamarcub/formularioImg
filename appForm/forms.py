from django import forms
from .models import ImageModel
from django.core.exceptions import ValidationError
from django import forms
import os



class CreaFormularioImgForm(forms.ModelForm):


    def validate_image_extension(value):
        MAX_SIZE_MB = 0.05  # 50 KB en megabytes
        valid_extensions = ['.jpg','.png']
        ext = os.path.splitext(value.name)[1] # La función splitext de la biblioteca os.path divide el nombre de un archivo
                                              # en una tupla que contiene la raíz del nombre del archivo y su extensión
        if not ext.lower() in valid_extensions: #ext.lower(): Convierte la extensión del archivo a minúsculas
            raise ValidationError('Solo se permiten imágenes con extensiones .jpg o .png.')

        if value.size > MAX_SIZE_MB * 1024 * 1024:  # Convertir a bytes
            raise ValidationError('La imagen no puede tener más de 50 KB.')

    class Meta: #proporcionar metadatos adicionales sobre el formulario
        model = ImageModel #Especifica el modelo asociado con este formulario.
        fields = ['image'] #Indica qué campos del modelo se deben incluir en el formulario.
                        # Aquí, el único campo incluido es image, que corresponde al campo ImageField del modelo.

    image = forms.ImageField(validators=[validate_image_extension])





