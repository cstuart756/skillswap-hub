# exchanges/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Skills
    path("skills/", views.skill_list, name="skill_list"),
    path("skills/<int:pk>/", views.skill_detail, name="skill_detail"),

    # Auth
    path("accounts/login/", views.login_view, name="login"),

    path("skills/create/", views.skill_create, name="skill_create"),

    # Exchange requests
    path(
        "skills/<int:skill_id>/request/",
        views.exchange_request_create,
        name="exchange_request_create",
    ),

    path(
        "exchange/requests/<int:request_id>/accept/",
        views.exchange_request_accept,
        name="exchange_request_accept",
    ),

    path(
        "exchange/requests/<int:request_id>/accept/",
        views.exchange_request_accept,
        name="exchange_request_accept",
    ),

    path(
        "exchange/requests/<int:request_id>/accept/",
        views.exchange_request_accept,
        name="exchange_request_accept",
    ),

    # (Optional) Dashboard if you have one; tests mention it but fail earlier on login reverse.
    path("dashboard/", views.dashboard, name="exchange_dashboard"),
]
