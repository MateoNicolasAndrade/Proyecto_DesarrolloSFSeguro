from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Estudiante, Prestamo  # Asegúrate de importar los modelos necesarios

class EstudianteAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='mateo', password='mateo123')
        self.client = APIClient()
        self.url = reverse('estudiantes-list')
        self.estudiante_data = {'estudiante_nombre': 'Juan', 'estudiante_correo': 'juan@example.com'}

    def test_list_estudiantes(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_estudiante(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, self.estudiante_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Estudiante.objects.count(), 1)

    def test_retrieve_estudiante(self):
        estudiante = Estudiante.objects.create(estudiante_nombre='Juan', estudiante_correo='juan@example.com')
        url = reverse('estudiantes-detail', args=[estudiante.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['estudiante_nombre'], 'Juan')

    # Puedes agregar más pruebas para actualizar, eliminar, etc.

class PrestamoAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='mateo', password='mateo123')
        self.client = APIClient()
        self.url = reverse('prestamos-list')
        self.estudiante = Estudiante.objects.create(estudiante_nombre='Juan', estudiante_correo='juan@example.com')
        self.prestamo_data = {'estudiante': self.estudiante.id, 'prestamo_fechaEnt': '2024-03-08', 'prestamo_fechaDev': '2024-03-15'}

    def test_list_prestamos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_prestamo(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, self.prestamo_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Prestamo.objects.count(), 1)

    def test_retrieve_prestamo(self):
        prestamo = Prestamo.objects.create(estudiante=self.estudiante, prestamo_fechaEnt='2024-03-08', prestamo_fechaDev='2024-03-15')
        url = reverse('prestamos-detail', args=[prestamo.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['estudiante'], self.estudiante.id)

    # Puedes agregar más pruebas para actualizar, eliminar, etc.
