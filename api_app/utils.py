from .models import OnixFile
from lxml import etree

class OnixParser():

    def get_root(self, xmlFile):
        """
        Get XML Root
        """
        with open(xmlFile) as fobj:
            xml = fobj.read()

        root = etree.fromstring(xml)
        return root

    def getSenderName(self, root):
        result = root.xpath("//SenderName")
        for element in result:
            return element.text

    def process_product(self, product_root):
        return True

    # TODO
    def process_onix(self, file_path):
        root = OnixParser.get_root(self, file_path)
        return OnixParser.getSenderName(self, root)