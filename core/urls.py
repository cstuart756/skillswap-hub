from django.contrib import admin
from django.urls import path, include

from skills.views import SkillListView
from .views import ExchangeDetailsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SkillListView.as_view(), name="skill_list"),

    path("exchange-details/", ExchangeDetailsView.as_view(), name="exchange_details"),

    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),

    path("skills/", include("skills.urls")),
    path("exchanges/", include("exchanges.urls")),
]

