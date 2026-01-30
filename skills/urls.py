from django.urls import path

from .views import (
    SkillListView,
    SkillDetailView,
    SkillCreateView,
    SkillUpdateView,
    SkillDeleteView,
)

urlpatterns = [
    path("", SkillListView.as_view(), name="skill_list"),
    path("new/", SkillCreateView.as_view(), name="skill_create"),
    path("<int:pk>/", SkillDetailView.as_view(), name="skill_detail"),
    path("<int:pk>/edit/", SkillUpdateView.as_view(), name="skill_update"),
    path("<int:pk>/delete/", SkillDeleteView.as_view(), name="skill_delete"),
]
