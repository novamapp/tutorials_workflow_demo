from django.test import TestCase
from django.urls import reverse
import pytest

from tutorials.models import Tutorial

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == '/'

# verifies that we are able to successfully create a Tutorial object in the database
# add marker @pytest.mark.django_db because pytest does not have access to the database in order to run this test
# @pytest.mark.django_db
# def test_create_tutorial():
#     tutorial = Tutorial.objects.create(
#         title='Pytest',
#         tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
#         description='Tutorial on how to apply pytest to a Django application',
#         published=True
#     )
#     assert tutorial.title == 'Pytest'

# turn this method into a fixture because there will be more
# integration tests that require creating a tutorial object
@pytest.fixture # the 'db' parameter is a built-in fixture provided by pytest-django
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()

def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk