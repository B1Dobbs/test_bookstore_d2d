#!/usr/bin/env python
#from .models import OnixFile
from lxml import etree
from test_bookstore_app.models import Book
import os
import datetime 
from django.utils.html import strip_tags

"""Modified from reference to accomidate for namespaces.
Reference: https://stackoverflow.com/questions/5572247/how-to-find-xml-elements-via-xpath-in-python-in-a-namespace-agnostic-way 
"""
def xpath_ns(tree, expr):
    relative = False
    if expr[0] == ".":
        relative = True
        expr = expr[1:]

    "Parse a simple expression and prepend namespace wildcards where unspecified."
    qual = lambda n: n if not n or ':' in n else '*[local-name() = "%s"]' % n
    expr = '/'.join(qual(n) for n in expr.split('/')) 
    nsmap = dict((k, v) for k, v in tree.nsmap.items() if k)

    if relative:
        expr = "." + expr
    return tree.xpath(expr, namespaces=nsmap)

def get_root(xmlFile):
    with open(xmlFile) as fobj:
        encoding = fobj.readline()
        fobj.seek(0)
        xml = fobj.read()

    if "utf-8" in encoding:
        root = etree.fromstring(xml.encode('utf-8'))
    elif "utf-16" in encoding:
        root = etree.fromstring(xml.encode('utf-16'))
    else:
        root = etree.fromstring(xml)
    return root

def get_isbn_13(product_root):
    productId = xpath_ns(product_root,"ProductIdentifier")
    for singleID in productId:
        idType = xpath_ns(singleID,"ProductIDType")
        idValue = xpath_ns(singleID,"IDValue")
        if(idType[0].text == "15"):
            return idValue[0].text
    return 0

def get_collection(product_root):
    collection = {}
    title = xpath_ns(product_root, ".//Collection//TitleText")
    num = xpath_ns(product_root, ".//Collection//PartNumber")

    if len(title) != 0:
        collection['title'] = title[0].text

    if len(num) != 0:
        collection['num'] = num[0].text

    return collection

def get_title(product_root):
    result = xpath_ns(product_root, ".//TitleDetail")
    for titleDetail in result:
        level = xpath_ns(titleDetail, ".//TitleElementLevel")
        title = xpath_ns(titleDetail, ".//TitleText")
        if(level[0].text == "01"):
            return title[0].text
    return 0

def get_contributors(product_root):
    authors = []
    result = xpath_ns(product_root, ".//Contributor")
    for contributor in result:
        role = xpath_ns(contributor,".//ContributorRole")
        name = xpath_ns(contributor, ".//PersonName")
        if role[0].text == "A01":
            authors.append(name[0].text)
    return authors

def get_language(product_root):
    language = xpath_ns(product_root, ".//LanguageCode")
    return language[0].text

def get_detail(product_root):
    result = xpath_ns(product_root, ".//CollateralDetail//TextContent")
    for detail in result:
        text_type = xpath_ns(detail, ".//TextType")
        text = xpath_ns(detail, ".//Text")
        if text_type[0].text == "03":
            return strip_tags(text[0].text)
    return 0

def get_availability(product_root):
    result = xpath_ns(product_root, ".//PublishingStatus")
   # print(result[0].text)
    if result[0].text == "04":
        return True
    elif result[0].text == "07":
        return False
    
    return -1

def get_publish_date(product_root):
    result = xpath_ns(product_root, ".//PublishingDate")
    for publishingDate in result:
        role = xpath_ns(publishingDate, "./PublishingDateRole")
        date = xpath_ns(publishingDate, "./Date")
        if role[0].text == "01":
            date_string = date[0].text
            year = int(date_string[0:4])
            month = int(date_string[4:6])
            day = int(date_string[6:8])
            return datetime.date(year, month, day)
    return 0

def get_price(product_root):
    result = xpath_ns(product_root, ".//Price")
    for price in result:
        price_type = xpath_ns(price, "./PriceType")
        amount = xpath_ns(price, "./PriceAmount")
        if price_type[0].text == "01":
            return amount[0].text
    return 0

def process_products(root):
    result = xpath_ns(root,"//Product") 
    for product in result:

        book = Book()

        try: 
            book.isbn = get_isbn_13(product)   
        except:
            print("ERROR: Could not get product ISBN.")  

        try:
            collection = get_collection(product)
            if 'title' in collection.keys():
                book.series = collection['title']
            if 'num' in collection.keys():
                book.vol_num = collection['num']
        except:
            print("INFO: Could not process collection for ISBN: %s." % book.isbn)

        try:
            book.title = get_title(product)
        except:
            print("INFO: Could not process title for ISBN: %s." % book.isbn)

        try:
            authors = get_contributors(product)
            authors_str = authors[0]
            for x in range(1, len(authors)):
                authors_str += ", " + authors[x]
            book.authors = authors_str
        except:
            print("INFO: Could not process contributors for ISBN: %s." % book.isbn)

        try:
            book.language = get_language(product)
        except:
            print("INFO: Could not process language for ISBN: %s." % book.isbn)

        try:
            book.description = get_detail(product)
        except:
            print("INFO: Could not process description for ISBN: %s." % book.isbn)

        try:
            isAvailable = get_availability(product)
            if isAvailable != -1:
                book.availability = isAvailable
        except:
            print("INFO: Could not process availability for ISBN: %s." % book.isbn)

        try:
            book.release_date = get_publish_date(product)
        except:
            print("INFO: Could not process release date for ISBN: %s." % book.isbn)

        try:
            book.price = get_price(product)
        except:
            print("INFO: Could not process price for ISBN: %s." % book.isbn)

        book.save()

def process_onix(file_path):
    try:
        root = get_root(file_path)
    except:
        print("ERROR: Could not open file.")

    process_products(root)

if __name__ == "__main__":
    process_onix("../resources/example.xml")
