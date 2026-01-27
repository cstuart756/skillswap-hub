import pytest
from django.contrib.auth import get_user_model
from skills.models import Skill

User = get_user_model()

@pytest.fixture
def base_url(live_server):
    return live_server.url

@pytest.fixture
def seeded_data(db):
    owner = User.objects.create_user(username="owner", email="owner@example.com", password="pass12345")
    requester = User.objects.create_user(username="req", email="req@example.com", password="pass12345")
    skill = Skill.objects.create(owner=owner, title="Bootstrap Layouts", description="Responsive UI patterns.")
    return {"owner": owner, "requester": requester, "skill": skill}

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"headless": True}
