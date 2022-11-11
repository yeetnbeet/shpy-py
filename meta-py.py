
import requests as req
import os 

class MetaFieldsPy :
    STORE_NAME = os.getenv("STORE_NAME")
    SECRET_TOKEN = os.getenv("SECRET_TOKEN")
    H = {"X-Shopify-Access-Token":SECRET_TOKEN,
    "Content-Type":"application/json"}


    def getMetafields(self,productId) :
        res = req.get("https://"+self.STORE_NAME+"/admin/api/2022-10/products/"+str(productId)+"/metafields.json",headers=self.H)
        resdata = res.json()
        return resdata

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