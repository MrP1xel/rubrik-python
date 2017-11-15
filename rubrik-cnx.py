import json
import requests
import base64
from pprint import pprint
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

class Rubrik():
        def __init__(self,ip,username,password):
                self.ip = ip
                self.url = "https://" + self.ip
                self.username = username
                self.password = password
                self.api_url = self.url + "/api/v1"
                self.login_url_end = "/login"
                self.login_session_end = "/session"
                self.login_url = self.api_url + self.login_url_end



        def auth(self):
                login_header={'Content-Type':'application/json','Accept':'application/json'}
                #userdata = "'{\"username\":\"%s\",\"password\":\"%s\"}'" % (self.username,self.password)
                userdata = "{" + "\"username\":\""+self.username+"\",\"password\":\""+self.password+"\"}"
                #print str(userdata)
                #print self.login_url
                #r = requests.post(self.login_url,headers=login_header,data='{"username":"admin","password":"Rotiontan"}',verify=False)
                r = requests.post(self.login_url,headers=login_header,data=userdata,verify=False)
                self.userID = (r.json().get('userId'))
                self.token = (r.json().get('token'))
                self.token_b64 = base64.b64encode(bytes(self.token))
                self.auth_header = {"Authorization": "Basic " + self.token_b64.decode("utf-8")}

				
rubrik_test = Rubrik("ip","user","password")
rubrik_test.auth()
