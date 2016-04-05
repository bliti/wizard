from django.conf.urls import url

from .views import SpellListView

urlpatterns = [
    url(r'^$', SpellListView.as_view(), name='spell-list'),
]