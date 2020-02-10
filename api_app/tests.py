from django.test import TestCase
from lxml import etree
import sys
from .utils import onix_parser

class OnixParserTestCase(TestCase):

    def test_example_onix(self):
        #print(sys.path)
        result = onix_parser.process_onix("C:/Users/brooke.dobbins/Documents/SE5/test_bookstore_d2d/api_app/resources/large_example.xml")
        self.assertEqual(True, True)
        

