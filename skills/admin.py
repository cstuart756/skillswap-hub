from django.contrib import admin
from .models import Category, Skill


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "category", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "description", "owner__username")
    autocomplete_fields = ("category", "owner")
