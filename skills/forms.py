from django import forms
from .models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["title", "category", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
        }

    def clean_title(self):
        title = (self.cleaned_data.get("title") or "").strip()
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
