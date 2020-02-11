from .models import OnixFile
from lxml import etree
from test_bookstore_app.models import Book
import os

class OnixParser():

    @staticmethod
    def get_root(xmlFile):
        """
        Get XML Root
        """
        with open(xmlFile) as fobj:
            xml = fobj.read()

        root = etree.fromstring(xml)
        return root

    @staticmethod
    def get_product_isbn_13(product_root):
        productId = product_root.xpath("ProductIdentifier")
        for singleID in productId:
            idType = singleID.xpath("ProductIDType")
            print("idType: " + idType)
            idValue = singleID.xpath("IDValue")
            print("idValue: " + idValue)
            if(idType == "15"):
                return idValue
        return 0

    @staticmethod
    def process_products(root):
        result = root.xpath("//Product") 
        for element in result:
            book = Book()
            book.isbn = OnixParser.get_product_isbn_13(element)  
            print(OnixParser.get_product_isbn_13(element))   
        return True

    @staticmethod
    def process_onix(file_path):
        root = OnixParser.get_root(file_path)
        #OnixParser.process_products(root)
        print(OnixFile.load("1"))
        print(os.path.exists("api_app/resources/onix3_example.xml"))
        return True
    
