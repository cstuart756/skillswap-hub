from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="exchange_dashboard"),
    path("request/<int:skill_id>/create/", views.request_create, name="exchange_request_create"),
    path("request/<int:request_id>/accept/", views.request_accept, name="exchange_request_accept"),
    path("request/<int:request_id>/reject/", views.request_reject, name="exchange_request_reject"),
    path("request/<int:request_id>/cancel/", views.request_cancel, name="exchange_request_cancel"),
]
