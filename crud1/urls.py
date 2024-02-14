from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login/', views.login, name='login'),
    path('interfaz_sa', views.interfaz_sa, name='interfaz_sa'),
    path('interfaz_ta/', views.interfaz_ta, name='interfaz_ta'),
    path('guardar_usuario/', views.guardar_usuario, name='guardar_usuario'),
    path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)