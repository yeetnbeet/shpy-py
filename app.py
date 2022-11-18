from shpy import MetaFieldsPy
from shpy import ProductsPy
from shpy import CollectionPy
from shpy import RedirectPy


shopifyMetaFields = MetaFieldsPy()
shopifyProducts = ProductsPy()
shopifyCollections = CollectionPy()
shopifyRedirects = RedirectPy()

shopifyRedirects.getAllRedirects()
print(len(shopifyRedirects.REDIRECT_LIST))


for x in range(0,100):
    print(shopifyRedirects.REDIRECT_LIST[x])


        


