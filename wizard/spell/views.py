from django.views.generic.list import ListView

from .models import Spell


class SpellListView(ListView):
    model = Spell