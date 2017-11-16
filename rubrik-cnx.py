import json
import requests
import base64
from pprint import pprint
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()


class Session():
        def __init__(self,username,password):
                self.username = username
                self.password = password

        def getUsername(self):
                return self.username

        def getPassword(self):
                return self.password

        def getUserId(self):
                return self.userId

        def getToken(self):
                return self.token

        def getTokenB64(self):
                return self.token_b64

        def getAuthHeader(self):
                return self.auth_header


class Cluster():

        def __init__(self,ip,Session):
                self.ip = ip
                self.url = "https://" + self.ip
                self.api_url = self.url + "/api/v1"
                self.login_url_end = "/login"
                self.login_url = self.api_url + self.login_url_end
                self.session = Session

        def auth(self):
                login_header={'Accept':'application/json'}
                userdata = "{" + "\"username\":\""+self.session.getUsername()+"\",\"password\":\""+self.session.password+"\"}"
                r = requests.post(self.login_url,headers=login_header,data=userdata,verify=False)
                if r.status_code == 200:
                        print "Connection OK"
                        Session.userId = (r.json().get('userId'))
                        Session.token = (r.json().get('token'))
                        Session.token_b64 = base64.b64encode(bytes(Session.token))
                        Session.auth_header = {"Authorization": "Basic " + Session.token_b64.decode("utf-8")}

                else:
                        if r.status_code == 400:
                                print "The connection request is malformated"

        def getClusterInfo(self,info):
                r = requests.get(self.api_url+'/cluster/me',verify=False,headers=self.session.getAuthHeader())
                return r.json()[info]

        def getClusterVersion(self):
                self.version = self.getClusterInfo("version")
                return self.version

        def getClusterId(self):
                self.id = self.getClusterInfo("id")
                return self.id

        def getClusterIsSingleNode(self):
                self.isSingleNode = self.getClusterInfo("isSingleNode")
                return self.isSingleNode

        def getBrikCount(self):
                r = requests.get(self.api_url+'/cluster/me/brik_count',verify=False,headers=self.session.getAuthHeader())
                self.brik_count = r.json()["count"]
                return self.brik_count

        def getDisksList(self):
                disksList = []
                r = requests.get(self.api_url+'/cluster/me/disk',verify=False,headers=self.session.getAuthHeader())
                for disk in r.json()["data"]:
                        disksList.append(Disk(disk["id"],disk["status"],disk["isEncrypted"],disk["diskType"],disk["nodeId"],disk["capacityBytes"],disk["path"],disk["unallocatedBytes"],disk["usableBytes"]))
                return disksList

        def getDiskCapacity(self):
                r = requests.get(self.api_url+'/cluster/me/disk_capacity',verify=False,headers=self.session.getAuthHeader())
                self.diskCapacity = r.json()["bytes"]
                return self.diskCapacity

        def getDnsServerList(self):
                dnsServerList = []
                r = requests.get(self.api_url+'/cluster/me/dns_nameserver',verify=False,headers=self.session.getAuthHeader())
                for dns in r.json()["data"]:
                        dnsServerList.append(dns)
                return dnsServerList

        def getNtpServerList(self):
                ntpServerList = []
                r = requests.get(self.api_url+'/cluster/me/ntp_server',verify=False,headers=self.session.getAuthHeader())
                for server in r.json()["data"]:
                        ntpServerList.append(server)
                return ntpServerList

        def getMemoryCapacity(self):
                r = requests.get(self.api_url+'/cluster/me/memory_capacity',verify=False,headers=self.session.getAuthHeader())
                return r.json()["bytes"]

        def getClusterName(self):
                r = requests.get(self.api_url+'/cluster/me/name',verify=False,headers=self.session.getAuthHeader())
                return r.json()

        def getNodesList(self):
                nodesList = []
                r = requests.get(self.api_url+'/cluster/me/node',verify=False,headers=self.session.getAuthHeader())
                for node in r.json()["data"]:
                        nodesList.append(Node(node["id"],node["brikId"],node["status"],node["ipAddress"],node["needsInspection"]))
                return nodesList


class Disk():
        def __init__(self,id,status,isEncrypted,diskType,nodeId,capacityBytes,path,unallocatedBytes,usableBytes):
                self.id = id
                self.status = status
                self.isEncrypted = isEncrypted
                self.diskType = diskType
                self.nodeId = nodeId
                self.capacityBytes = capacityBytes
                self.path = path
                self.uanllocatedBytes = unallocatedBytes
                self.usableBytes = usableBytes


class Node():
        def __init__(self,id,brikId,status,ipAddress,needsInspection):
                self.id = id
                self.brikId = brikId
                self.status = status
                self.ipAddress = ipAddress
                self.needsInspection = needsInspection





# Create a Session object with rubrik credentials
# Create a Cluster object with ip of the cluster and the belonging session object
# Call the auth method of the Cluster object

ms = Session("XXX","XXX")
r_test = Cluster("0.0.0.0",ms)
r_test.auth()
