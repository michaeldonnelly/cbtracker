from django import template
register = template.Library()

from cbtracker.models import Favorite

@register.inclusion_tag('cbtracker/favorite_dropdown.html', takes_context=False)
def show_favorites():
	favorites = Favorite.objects.all()
	return {'favorites': favorites}
	
