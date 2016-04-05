from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Spell(models.Model):
    """
    Spell is like a tweet but about
    magic.
    """
    content = models.CharField(max_length=140)
    created = models.DateTimeField(default=timezone.now())
    
    def __unicode__(self): return self.content
    
    class Meta:
        ordering = ('created',)