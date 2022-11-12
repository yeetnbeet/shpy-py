
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
            