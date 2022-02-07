import pytest
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Task


# class TaskApiTestCase(APITestCase):
#     def test_get(self):
#         task_1 = Task.objects.create(title="Task One", task="text of task")
#         task_2 = Task.objects.create(title="Task Two", task="text of task")
#         url = reverse('create')
#         print(url)
#         response = self.client.get(url)
#         print("response", response.body)


@pytest.mark.django_db
def test_user_create():
    Task.objects.create(title="Task One", task="text of task")
    count = Task.objects.all().count()
    print(count)
    assert Task.objects.count() == 1
