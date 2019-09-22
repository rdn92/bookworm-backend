import pytest
import allure
from django.urls import reverse
from rest_framework import status
from .models import Author


@pytest.mark.django_db
def test_get_author_list(client):
    url = reverse('author-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 0


@pytest.mark.django_db
def test_create_author(client):
    url = reverse('author-list')
    data = {'first_name': 'name', 'last_name': 'surname'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Author.objects.count() == 1
    assert Author.objects.get().first_name == 'name'
    assert Author.objects.get().last_name == 'surname'
