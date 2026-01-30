import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from skills.models import Skill, Category
from exchanges.models import ExchangeRequest

User = get_user_model()


@pytest.mark.django_db
def test_request_lifecycle_permissions(client):
    owner = User.objects.create_user(
        username="owner",
        email="owner@example.com",
        password="pass12345",
    )
    requester = User.objects.create_user(
        username="req",
        email="req@example.com",
        password="pass12345",
    )

    cat = Category.objects.create(name="Design")
    skill = Skill.objects.create(
        owner=owner,
        category=cat,
        title="Figma Basics",
        description="Learn Figma.",
    )

    client.login(username="req", password="pass12345")
    resp = client.post(reverse("exchange_request_create", args=[skill.id]))
    assert resp.status_code in (302, 303)
    ex = ExchangeRequest.objects.get(skill=skill, requester=requester)
    assert ex.status == ExchangeRequest.Status.PENDING

    resp = client.post(reverse("exchange_request_accept", args=[ex.id]))
    assert resp.status_code == 404

    client.logout()
    client.login(username="owner", password="pass12345")
    resp = client.post(reverse("exchange_request_accept", args=[ex.id]))
    assert resp.status_code in (302, 303)
    ex.refresh_from_db()
    assert ex.status == ExchangeRequest.Status.ACCEPTED
