from .models import OnixFile
from lxml import etree

class OnixParser():

    def get_root(xmlFile):
        """
        Get XML Root
        """
        with open(xmlFile) as fobj:
            xml = fobj.read()

        root = etree.fromstring(xml)
        return root

    def getSenderName(root):
        result = root.xpath("//SenderName")
        for element in result:
            return element.text

    def process_product(product_root):
        return True

    # TODO
    def process_onix(file_path):
        root = OnixParser.get_root(file_path)
        return OnixParser.getSenderName(root)