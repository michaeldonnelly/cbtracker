from django import forms

from comicbooks.models import Issue

class IssueForm(forms.ModelForm):
	class Meta:
		model = Issue
		exclude = []