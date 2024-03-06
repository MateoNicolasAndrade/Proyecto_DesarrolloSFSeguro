from django.urls import path
from .views import EstudianteAPIviewSet, PrestamoAPIviewSet, AutorAPIviewSet, LibroAPIviewSet, DetallePrestamoAPIviewSet, LibroExtendAPIviewSet, DetallePrestamoExtendAPIviewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'estudiantes', EstudianteAPIviewSet, basename='estudiantes')
router.register(r'prestamos', PrestamoAPIviewSet, basename='prestamos')
router.register(r'autores', AutorAPIviewSet, basename='autores')
router.register(r'libros', LibroAPIviewSet, basename='libros')
router.register(r'libros_', LibroExtendAPIviewSet, basename='libros_')
router.register(r'detalles', DetallePrestamoAPIviewSet, basename='detalles')
router.register(r'detalles_', DetallePrestamoExtendAPIviewSet, basename='detalles_')


urlpatterns = []

urlpatterns += router.urls