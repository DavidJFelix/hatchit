from .views.suggestion import my_suggestions
from .views.events import my_events, my_events_json
from .views.base import home
from .views.api import api_get

__all__ = [
	'my_suggestions',
	'my_events',
	'my_events_json',
	'home',
	'api_get',
]
