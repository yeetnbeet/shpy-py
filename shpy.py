
import requests as req
import os 

class MetaFieldsPy :
    STORE_NAME = os.getenv("STORE_NAME")
    H = {"X-Shopify-Access-Token":os.getenv("SECRET_TOKEN"),
    "Content-Type":"application/json"}


    def getMetafields(self,productId) :
        res = req.get("https://"+self.STORE_NAME+"/admin/api/2022-10/products/"+str(productId)+"/metafields.json",headers=self.H)
        resdata = res.json()
        return resdata["metafields"]

    def modifyExistingMetaField(self,metaFieldId,productId,value,type):
        d = {"metafield":{
            "id":metaFieldId,
            "value":value,
            "type":type
        }} 
        res = req.put("https://"+self.STORE_NAME+"/admin/api/2022-10/products/"+str(productId)+"/metafields/"+str(metaFieldId)+".json",headers=self.H,json=d)
        print(res.text)
        print(str(d))

    def createNewMetafield(self,productId,namespace,key,value,type):
        d = {"metafield":{
            "namespace":namespace,
            "key":key,
            "value":value,
            "type":type
        }}
        res = req.post("https://"+self.STORE_NAME+"/admin/api/2022-10/products/"+str(productId)+"/metafields.json",headers=self.H,json=d)
        print(res.status_code)

    def productHasMetaField(self,productId,metaFieldKey):
        metaFields = self.getMetafields(productId)
        for item in metaFields:
            if item["key"]== metaFieldKey :
                return int(item["id"])
        return False

class ProductsPy :
    STORE_NAME = os.getenv("STORE_NAME")
    H = {"X-Shopify-Access-Token":os.getenv("SECRET_TOKEN"),
        "Content-Type":"application/json"}
    PRODUCT_LIST = []

    def getAllProductsFromCollection(self,collectionID="",URL=""):
        if URL == "" :
            print("Recursive1")
            res = req.get("https://"+self.STORE_NAME+"/admin/api/2022-10/products.json?collection_id="+str(collectionID),headers=self.H)
            resdata = res.json()
            print(self.H)
            print(resdata)
            for item in resdata ["products"]:
                self.PRODUCT_LIST.append(item)
            if res.links != {}:
                url = res.links['next']['url']
                self.getAllProductsFromCollection(URL=url)

        elif URL != "":
            print("Recursive2")
            res = req.get(URL,headers=self.H)
            resdata = res.json()
            print(res.links)
            for item in resdata ["products"]:
                self.PRODUCT_LIST.append(item)
            if res.links != {} and len(res.links) == 2:
                url = res.links['next']['url']
                self.getAllProductsFromCollection(URL=url)

    def getSingleProduct(self,productID) :
        res = req.get("https://"+self.STORE_NAME+"/admin/api/2022-10/products/"+str(productID)+".json",headers=self.H)
        return res.json()

        
            