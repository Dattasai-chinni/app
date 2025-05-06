from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student

class StudentAPITestCase(APITestCase):

    def setUp(self):
        self.student1 = Student.objects.create(name="Alice", age=20, grade="A")
        self.student2 = Student.objects.create(name="Bob", age=21, grade="B")

    def test_create_student(self):
        url = reverse('create_student')
        data = {"name": "Charlie", "age": 22, "grade": "A"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 3)

    def test_list_students(self):
        url = reverse('list_students')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_student(self):
        url = reverse('get_student', kwargs={'pk': self.student1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Alice')

    def test_update_student(self):
        url = reverse('update_student', kwargs={'pk': self.student1.pk})
        data = {"name": "Alice Updated", "age": 23, "grade": "A+"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student1.refresh_from_db()
        self.assertEqual(self.student1.name, "Alice Updated")

    def test_delete_student(self):
        url = reverse('delete_student', kwargs={'pk': self.student2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(pk=self.student2.pk).exists())

    def test_total_student_count(self):
        url = reverse('total-student-count')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_students'], 2)

    def test_get_student_names(self):
        url = reverse('student-names')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Alice', response.data['student_names'])

    def test_search_students_by_name(self):
        url = reverse('search_students_by_name') + '?name=Ali'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Alice')

