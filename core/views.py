from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import ExchangeDetail

@method_decorator(login_required, name='dispatch')
class ExchangeDetailsView(View):
    def get(self, request):
        return render(request, "exchange_details.html")

    def post(self, request):
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
        context = {"success": True}
        return render(request, "exchange_details.html", context)
