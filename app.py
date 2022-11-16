from shpy import MetaFieldsPy
from shpy import ProductsPy
from shpy import CollectionPy
import csv

searchTerms = []
with open('SKU.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        searchTerms.append(row.pop())
        
for item in searchTerms:
    print(item)

shopifyMetaFields = MetaFieldsPy()
shopifyProducts = ProductsPy()
shopifyCollections = CollectionPy()

shopifyProducts.getAllProductsFromCollection(403466617077)
print(len(shopifyProducts.PRODUCT_LIST))
for item in shopifyProducts.PRODUCT_LIST:
    included = 0
    for term in searchTerms:
        if term in str(item["title"]).lower():
            print(item["title"])
            included = 1
        print("...")
    if included == 0: 
        shopifyCollections.addItemToExistingCollection(item["id"],403472974069)        
    included = 0
##print(shopifyCollections.addItemToExistingCollection(6743871979688,403471302901))





        


