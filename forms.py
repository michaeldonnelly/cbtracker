from django import forms

from cbtracker.models import Issue

class IssueForm(forms.ModelForm):
	class Meta:
		model = Issue
		exclude = []