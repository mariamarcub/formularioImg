from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('imagenes/', views.imagenes, name='imagenes'),
    path('delete/<int:image_id>/', views.borrarImg, name='borrarImg'),

]

#Para poder trabajar con imágenes la necesito
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
