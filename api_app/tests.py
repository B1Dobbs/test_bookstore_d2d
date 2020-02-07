from django.test import TestCase
from .utils import OnixParser
from lxml import etree

class OnixParserTestCase(TestCase):

    def test_example_onix(self):
        
        result = OnixParser.process_onix("C:/Users/BrookeDobbins/Development/Environments/D2D/test_bookstore/api_app/resources/onix3_example.xml")
        self.assertEqual(result, True)
        

