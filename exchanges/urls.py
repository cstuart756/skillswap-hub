# exchanges/urls.py
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from skills.views import SkillListView, SkillDetailView, SkillCreateView, SkillUpdateView, SkillDeleteView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("skill_list"))),
    # Skills
    path("skills/", SkillListView.as_view(), name="skill_list"),
    path("skills/<int:pk>/", SkillDetailView.as_view(), name="skill_detail"),

    # Auth
    path("accounts/login/", views.login_view, name="login"),

    path("skills/create/", SkillCreateView.as_view(), name="skill_create"),
    path("skills/<int:pk>/update/", SkillUpdateView.as_view(), name="skill_update"),
    path("skills/<int:pk>/delete/", SkillDeleteView.as_view(), name="skill_delete"),

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

    # (Optional) Dashboard if you have one; tests mention it but fail earlier on login reverse.
    path("dashboard/", views.dashboard, name="exchange_dashboard"),
]
