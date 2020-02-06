from .models import OnixFile
from lxml import etree
from test_bookstore_app.models import Book

class OnixParser():

    def get_root(xmlFile):
        """
        Get XML Root
        """
        with open(xmlFile) as fobj:
            xml = fobj.read()

        root = etree.fromstring(xml)
        return root

    def get_sender_name(root):
        result = root.xpath("//SenderName")
        for element in result:
            return element.text

    def get_product_isbn_13(product_root):
        productId = product_root.xpath("ProductIdentifier")
        for singleID in productId:
            idType = elem.xpath("ProductIDType")
            idValue = elem.xpath("IDValue")
            if(idType == "15"):
                return idValue

    def process_products(root):
        result = root.xpath("//Product") 
        for element in result:
            book = Book()
            book.isbn = get_product_isbn_13(element)     
        return True

    # TODO
    def process_onix(self, file_path):
        root = OnixParser.get_root(file_path)
        return OnixParser.getSenderName(root)