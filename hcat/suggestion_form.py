from django import forms
from .models import SuggestedProjects


class ProjectSuggestion(forms.ModelForm):
    class Meta:
        model = SuggestedProjects
        fields = ['title', 'submitter_name', 'ip_address', 'links', 'summary']
        widgets = {'ip_address': forms.HiddenInput()}