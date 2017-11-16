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
                self.login_url = self.api_url + self.login_url_end

        def auth(self):
                # Send username + password to /login API endpoint
                # get the token
                # create an header with "Authorization":"Basic" + token encoded with base64

                login_header={'Accept':'application/json'}
                userdata = "{" + "\"username\":\""+self.username+"\",\"password\":\""+self.password+"\"}"
                r = requests.post(self.login_url,headers=login_header,data=userdata,verify=False)
                if r.status_code == 200:
                        print "Connection OK"
                        self.userID = (r.json().get('userId'))
                        self.token = (r.json().get('token'))
                        self.token_b64 = base64.b64encode(bytes(self.token))
                        self.auth_header = {"Authorization": "Basic " + self.token_b64.decode("utf-8")}

                else:
                        if r.status_code == 400:
                                print "The connection request is malformated"

# To connect to your rubrik, just create a Rubrik object with following params : IP, username, password
# Then call the auth() method of this object

r_test = Rubrik("172.17.42.90","admin","Rotiontan")
r_test.auth()