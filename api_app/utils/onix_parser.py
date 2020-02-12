#!/usr/bin/env python
#from .models import OnixFile
from lxml import etree
from test_bookstore_app.models import Book
import os
import datetime 

"""Used to include namespace from any Onix file for simple xpath usage.
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
    """
    Get XML Root
    """
    with open(xmlFile) as fobj:
        encoding = fobj.readline()
        fobj.seek(0)
        xml = fobj.read()
    print(encoding)

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
        #collection = {'title' : title[0].text, 'num': num[0].text}

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
            return text[0].text
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
        #print("\nBook: ")
        book = Book()
        book.isbn = get_isbn_13(product)   
        #print(get_isbn_13(product))  

        collection = get_collection(product)
        if 'title' in collection.keys():
            book.series = collection['title']
            #print(collection['title'])
        if 'num' in collection.keys():
            book.vol_num = collection['num']
            #print(collection['num'])

        book.title = get_title(product)
        #print(get_title(product, root))

        authors = get_contributors(product)

        if len(authors) > 0:
            authors_str = authors[0]
            for x in range(1, len(authors)):
                authors_str += ", " + authors[x]
            book.authors = authors_str
            #print(get_contributors(product))

        book.language = get_language(product)
        #print(get_language(product))

        book.description = get_detail(product)
        #print(get_detail(product))

        isAvailable = get_availability(product)
        if isAvailable != -1:
            book.availability = isAvailable
            #print(get_availability(product))

        book.release_date = get_publish_date(product)
        #print(get_publish_date(product))

        book.price = get_price(product)
        #print(get_price(product))

        book.save()

    return True

def process_onix(file_path):
    root = get_root(file_path)
    process_products(root)

if __name__ == "__main__":
    process_onix("../resources/large_example.xml")
