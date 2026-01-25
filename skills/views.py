from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import SkillForm
from .models import Skill, Category


class SkillListView(ListView):
    model = Skill
    template_name = "skills/skill_list.html"
    context_object_name = "skills"
    paginate_by = 9

    def get_queryset(self):
        qs = Skill.objects.select_related("owner", "category").all()

        q = (self.request.GET.get("q") or "").strip()
        cat = (self.request.GET.get("category") or "").strip()
        sort = (self.request.GET.get("sort") or "new").strip()

        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(owner__username__icontains=q))

        if cat:
            if cat.isdigit():
                qs = qs.filter(category_id=int(cat))
            else:
                qs = qs.filter(category__slug=cat)

        if sort == "old":
            qs = qs.order_by("created_at")
        elif sort == "title":
            qs = qs.order_by("title", "-created_at")
        else:
            qs = qs.order_by("-created_at")

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = Category.objects.all()
        ctx["q"] = (self.request.GET.get("q") or "").strip()
        ctx["category"] = (self.request.GET.get("category") or "").strip()
        ctx["sort"] = (self.request.GET.get("sort") or "new").strip()
        return ctx


class SkillDetailView(DetailView):
    model = Skill
    template_name = "skills/skill_detail.html"
    context_object_name = "skill"

    def get_queryset(self):
        return Skill.objects.select_related("owner", "category")


class OwnerRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner_id != request.user.id:
            messages.error(request, "You do not have permission to access that resource.")
            raise Http404("Not found")
        return super().dispatch(request, *args, **kwargs)


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = "skills/skill_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Skill created successfully.")
        return super().form_valid(form)


class SkillUpdateView(OwnerRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = "skills/skill_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Skill updated successfully.")
        return super().form_valid(form)


class SkillDeleteView(OwnerRequiredMixin, DeleteView):
    model = Skill
    template_name = "skills/skill_confirm_delete.html"
    success_url = reverse_lazy("skill_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Skill deleted successfully.")
        return super().delete(request, *args, **kwargs)
