from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from skills.models import Skill
from .models import ExchangeRequest

@login_required
def dashboard(request):
    received = (
        ExchangeRequest.objects.select_related("skill", "skill__owner", "requester")
        .filter(skill__owner=request.user)
        .order_by("-created_at")
    )
    sent = (
        ExchangeRequest.objects.select_related("skill", "skill__owner", "requester")
        .filter(requester=request.user)
        .order_by("-created_at")
    )
    return render(request, "exchanges/dashboard.html", {"received": received, "sent": sent})

@require_POST
@login_required
def request_create(request, skill_id: int):
    skill = get_object_or_404(Skill, pk=skill_id)

    if skill.owner_id == request.user.id:
        messages.error(request, "You cannot request an exchange on your own skill listing.")
        return redirect(skill.get_absolute_url())

    try:
        ExchangeRequest.objects.create(skill=skill, requester=request.user)
    except IntegrityError:
        messages.info(request, "You already have a pending request for this skill.")
    else:
        messages.success(request, "Exchange request sent.")
    return redirect("exchange_dashboard")

@require_POST
@login_required
def request_accept(request, request_id: int):
    ex = get_object_or_404(ExchangeRequest.objects.select_related("skill"), pk=request_id)
    if ex.skill.owner_id != request.user.id:
        messages.error(request, "Only the skill owner may accept this request.")
        raise Http404("Not found")

    if ex.status != ExchangeRequest.STATUS_PENDING:
        messages.info(request, "Only pending requests can be accepted.")
        return redirect("exchange_dashboard")

    ex.status = ExchangeRequest.STATUS_ACCEPTED
    ex.save(update_fields=["status"])
    messages.success(request, "Request accepted.")
    return redirect("exchange_dashboard")

@require_POST
@login_required
def request_reject(request, request_id: int):
    ex = get_object_or_404(ExchangeRequest.objects.select_related("skill"), pk=request_id)
    if ex.skill.owner_id != request.user.id:
        messages.error(request, "Only the skill owner may reject this request.")
        raise Http404("Not found")

    if ex.status != ExchangeRequest.STATUS_PENDING:
        messages.info(request, "Only pending requests can be rejected.")
        return redirect("exchange_dashboard")

    ex.status = ExchangeRequest.STATUS_REJECTED
    ex.save(update_fields=["status"])
    messages.success(request, "Request rejected.")
    return redirect("exchange_dashboard")

@require_POST
@login_required
def request_cancel(request, request_id: int):
    ex = get_object_or_404(ExchangeRequest.objects.select_related("skill"), pk=request_id)
    if ex.requester_id != request.user.id:
        messages.error(request, "Only the requester may cancel this request.")
        raise Http404("Not found")

    if ex.status != ExchangeRequest.STATUS_PENDING:
        messages.info(request, "Only pending requests can be cancelled.")
        return redirect("exchange_dashboard")

    ex.status = ExchangeRequest.STATUS_CANCELLED
    ex.save(update_fields=["status"])
    messages.success(request, "Request cancelled.")
    return redirect("exchange_dashboard")
