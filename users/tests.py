from django.test import TestCase
from django.urls import reverse
import pytest

@pytest.fixture 
# django_user_model is a built-in fixture
# - it acts as a shortcut to accessing the User model for this project
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username='test_username', password='test_password'
    )
    return 'test_username', 'test_password'

# Create your tests here.

# test that logging into the app works
# client: fixture that is a built-in dummy web client provided by Django
# - as a part of its testing tools
def test_login_user(client, test_user):
    test_username, test_password = test_user
    login_result = client.login(username=test_username, password=test_password)
    assert login_result