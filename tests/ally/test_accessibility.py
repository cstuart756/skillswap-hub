import pytest
from playwright.sync_api import sync_playwright
from django.urls import reverse
from .axe_utils import run_axe

pytestmark = pytest.mark.django_db

def login(page, base_url, identifier, password):
    page.goto(base_url + reverse("login"))
    page.fill('input[name="username"]', identifier)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"]')
    page.wait_for_load_state("networkidle")

def assert_no_serious_violations(page):
    violations = run_axe(page, included_impacts={"critical", "serious"})
    assert violations == [], f"Axe violations found: {violations}"

def test_a11y_skill_list(base_url, seeded_data):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(base_url + reverse("skill_list"))
        assert_no_serious_violations(page)
        browser.close()

def test_a11y_skill_detail(base_url, seeded_data):
    skill = seeded_data["skill"]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(base_url + reverse("skill_detail", args=[skill.id]))
        assert_no_serious_violations(page)
        browser.close()

def test_a11y_login_page(base_url, seeded_data):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(base_url + reverse("login"))
        assert_no_serious_violations(page)
        browser.close()

def test_a11y_dashboard_authenticated(base_url, seeded_data):
    requester = seeded_data["requester"]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login(page, base_url, requester.email, "pass12345")
        page.goto(base_url + reverse("exchange_dashboard"))
        page.wait_for_load_state("networkidle")
        assert_no_serious_violations(page)
        browser.close()
