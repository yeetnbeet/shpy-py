from shpy import MetaFieldsPy
from shpy import ProductsPy

shopifyMetaFields = MetaFieldsPy()
shopifyProducts = ProductsPy()

shopifyProducts.getAllProductsFromCollection(403466617077)
print(len(shopifyProducts.PRODUCT_LIST))

        


