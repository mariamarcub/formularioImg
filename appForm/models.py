from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/') #Indicamos aquí que es de tipo ImageField
    #upload_to='images/': Especifica la subcarpeta dentro de tu directorio de medios (MEDIA_ROOT) donde se almacenarán las imágenes.
    def __str__(self):
        return self.image.name #Para que me indique el nombre de la img
