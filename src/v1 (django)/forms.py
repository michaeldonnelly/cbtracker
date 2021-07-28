from django import forms

from cbtracker.models import Issue, Trade

class IssueForm(forms.ModelForm):
	referrer = forms.URLField(required=False, widget=forms.HiddenInput)
	class Meta:
		model = Issue
		exclude = []
		
class TradeForm(forms.ModelForm):
	referrer = forms.URLField(required=False, widget=forms.HiddenInput)
	class Meta:
		model = Trade
		exclude = []
