from django.test import TestCase

from .models import Spell


class SpellTestCase(TestCase):
    def setUp(self):
        self.valid_content = """
            May all good things come to you
            May nothing whatsoever harm you
            May your heart be light
            May your travels be safe
            May your health be good
            May your mind be sound
            May your friendships sustain you
            May you be blessed in every way
            """
        
        self.invalid_content = """
        Webtwo ipsum dolor sit amet,
        eskobo chumby doostang bebo. 
        Kazaa blippy sococo blyve bitly sococo meebo imeem zinch eduvant,
        heekya spotify kno zinch twitter trulia grockit kno oooj fleck,
        cuil kosmix wakoopa zinch greplin bitly xobni dogster eskobo. 
        Zillow kazaa quora groupon zanga cotweet sclipo blippy appjet groupon,
        divvyshot convore lala blekko kno divvyshot bubbli jiglu, 
        whrrl edmodo doostang grockit scribd ebay zillow octopart. 
        Voki palantir sifteo foodzie yoono imvu blekko revver plaxo dropio wufoo,
        insala dropio odeo zynga knewton sifteo trulia squidoo.
        Palantir zoho chartly vuvox hipmunk vuvox plugg zanga,
        vimeo tivo heekya foodzie disqus. 

        Webtwo ipsum dolor sit amet,
        eskobo chumby doostang bebo. 
        Kazaa blippy sococo blyve bitly sococo meebo imeem zinch eduvant,
        heekya spotify kno zinch twitter trulia grockit kno oooj fleck,
        cuil kosmix wakoopa zinch greplin bitly xobni dogster eskobo. 
        Zillow kazaa quora groupon zanga cotweet sclipo blippy appjet groupon,
        divvyshot convore lala blekko kno divvyshot bubbli jiglu, 
        whrrl edmodo doostang grockit scribd ebay zillow octopart. 
        Voki palantir sifteo foodzie yoono imvu blekko revver plaxo dropio wufoo,
        insala dropio odeo zynga knewton sifteo trulia squidoo.
        Palantir zoho chartly vuvox hipmunk vuvox plugg zanga,
        vimeo tivo heekya foodzie disqus. 
        """
        
            
        self.spell_one = Spell.objects.create(content=self.valid_content)
        self.spell_two = Spell.objects.create(content=self.invalid_content)


    def test_spell_one_content_is_less_or_equal_to_140_characters(self):
        self.assertTrue(len(self.spell_one.content) >= 140)
    
    
    def test_spell_two_content_is_more_than_140_characters(self):
        self.assertTrue(len(self.spell_two.content) > 140)


    def tearDown(self):
        self.spell_one.delete()