from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import ExchangeDetail
from exchanges.models import ExchangeRequest


@method_decorator(login_required, name="dispatch")
class ExchangeDetailsView(View):
    def get(self, request):
        # Only allow users who have requested a SkillSwap
        has_requested = ExchangeRequest.objects.filter(
            requester=request.user
        ).exists()
        if not has_requested:
            return render(
                request,
                "exchange_details.html",
                {"not_allowed": True},
            )
        user_details = ExchangeDetail.objects.filter(user=request.user)
        context = {"user_details": user_details}
        return render(request, "exchange_details.html", context)

    def post(self, request):
        # Only allow users who have requested a SkillSwap
        has_requested = ExchangeRequest.objects.filter(
            requester=request.user
        ).exists()
        if not has_requested:
            return render(
                request,
                "exchange_details.html",
                {"not_allowed": True},
            )
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone", "")
        notes = request.POST.get("notes", "")
        ExchangeDetail.objects.create(
            user=request.user,
            full_name=full_name,
            email=email,
            phone=phone,
            notes=notes,
        )
        # After saving, show all the user's details and success message
        user_details = ExchangeDetail.objects.filter(user=request.user)
        context = {"success": True, "user_details": user_details}
        return render(request, "exchange_details.html", context)
