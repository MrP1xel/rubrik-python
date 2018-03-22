import json
import requests
import base64
from pprint import pprint
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

class Session():
        LOGIN_HEADER = {'Accept':'application/json'}
        API_VERSION_ENDPOINT = "/api/v1"
        LOGIN_ENDPOINT = "/login"

        def __init__(self,username,password,ip):
                self.username = username
                self._password = password
                self.ip = ip
                self.login_url = "https://" + self.ip + Session.API_VERSION_ENDPOINT + Session.LOGIN_ENDPOINT
		self._authCode = ""

        def auth(self):
                self._userdata = "{" + "\"username\":\""+ self.username+"\",\"password\":\""+ self._password+"\"}"
                r_auth = requests.post(self.login_url,headers=Session.LOGIN_HEADER,data=self._userdata,verify=False)

                if r_auth.status_code == 200:
                       # code 200 = connection OK
                        self._userId = (r_auth.json().get('userId'))
                        self._token = (r_auth.json().get('token'))
                        self._token_b64 = base64.b64encode(bytes(self._token))
                        self._auth_header = {"Authorization": "Basic " + self._token_b64.decode("utf-8")}
                        self._isConnected = True
			self._authCode = 200
                        return self._isConnected

                else:
                        if r_auth.status_code == 400:
				# code 400 = connection request is malformated	
                                self._isConnected = False
				self.authCode = 400
                                return self._isConnected
                        else:
                                if r_auth.status_code == 422:
				# code 422 = incorrect credentials
                                        self._isConnected = False
					self._authCode = 422
                                        return self._isConnected

	def getAuthCode(self):
		return self._authCode
	
        #API MAPPING

        CLUSTER_ID = "/cluster/me"
        CLUSTER_ID_BOOTSTRAP = "/cluster/me/bootstrap"
        CLUSTER_ID_BRIK_COUNT = "/cluster/me/brik_count"
        CLUSTER_ID_DECOMMISSION_NODE = "/cluster/me/decommission_node"
        CLUSTER_ID_DISCOVER = "/cluster/me/discover"
        CLUSTER_ID_DISK = "/cluster/me/disk"
        CLUSTER_ID_DISK_CAPACITY = "/cluster/me/disk_capacity"
        CLUSTER_ID_DNS_NAMESERVER = "/cluster/me/dns_nameserver"
        CLUSTER_ID_DNS_SEARCH_DOMAIN = "/cluster/me/dns_search_domain"
        CLUSTER_ID_FLASH_CAPACITY = "/cluster/me/flash_capacity"
        CLUSTER_ID_IO_STATS = "/cluster/me/io_stats"
        CLUSTER_ID_IS_SINGLE_NODE = "/cluster/me/is_single_node"
        CLUSTER_ID__NAME = "/cluster/me/name"
        CLUSTER_ID_MEMORY_CAPACITY = "/cluster/me/memory_capacity"
        CLUSTER_ID_NODE = "/cluster/me/node"
        CLUSTER_ID_NTP_SERVER = "/cluster/me/ntp_server"
        CLUSTER_ID_VERSION = "/cluster/me/version"
        CLUSTER_ID_VLAN = "/cluster/me/vlan"
        CLUSTER_ID_SLA_DOMAIN = "/cluster/me/sla_domain"
        CLUSTER_ID_SLA_DOMAIN_ID = "/cluster/me/sla_domain"
	CLUSTER_ID_NODE = "/cluster/me/node"
        USER = "/user"
        USER_NOTIFICATION = "/user_notification"
        VCENTER = "/vmware/vcenter"
        VIRTUAL_DISK = "/vmware/virtual_disk"
	


        def _getApi(self,api_endpoint):
                return requests.get("https://" + self.ip + Session.API_VERSION_ENDPOINT + api_endpoint, verify=False,headers=self._auth_header).json()

        def _getApiWithId(self,api_endpoint,id):
                return requests.get("https://" + self.ip + Session.API_VERSION_ENDPOINT + api_endpoint +"/"+id,verify=False,headers=self._auth_header).json()


	def getClusterVersion(self):
        	return self._getApi(self.CLUSTER_ID_VERSION)

	def getClusterBrikCount(self):
        	return self._getApi(self.CLUSTER_ID_BRIK_COUNT)["count"]

	def getClusterUserList(self):
       		user_list = []
        	for user in  self._getApi(self.USER):
               		 user_list.append(User(user["username"],user["firstName"],user["authDomainId"],user["isAdmin"],user["role"],user["lastName"],user["emailAddress"],user["id"]))
        	return user_list

	def getClusterNodeList(self):
		node_list = []
		for node in self._getApi(self.CLUSTER_ID_NODE)['data']:
			node_list.append(Node(node["status"],node["ipAddress"],node["id"],node["needsInspection"],node["brikId"]))
		return node_list

	def getClusterVcenterList(self):
		vcenter_list = []
		for vc in self._getApi(self.VCENTER)['data']:
			vcenter_list.append(Vcenter(vc["id"],vc["managedId"],vc["ip"],vc["username"],vc["configuredSlaDomainId"],vc["primaryClusterUuid"]))
		return vcenter_list

class User():
        def __init__(self,userName,firstName,authDomainId,isAdmin,role,lastName,emailAddress,id):
                self._userName = userName
                self._firstName = firstName
                self._authDomainId = authDomainId
                self._isAdmin = isAdmin
                self._role = role
                self._lastName = lastName
                self._emailAddress = emailAddress
                self._id = id

        def getUserName(self):
                return self._userName

        def getFirstName(self):
                return self._fistName

        def getAuthDomainId(self):
                return self._authDomainId

        def getIsAdmin(self):
                return self._isAdmin

        def getRole(self):
                return self._role

        def getLastName(self):
                return self._lastName

        def getEmailAddress(self):
                return self._emailAddress

        def getId(self):
                return self._id


class Node():
	def __init__(self,status,ipAddress,id,needsInspection,brikId):
		self._status = status
		self._ipAddress = ipAddress
		self._id = id
		self._needsInspection = needsInspection
		self._brikId = brikId

	def getNodeStatus(self):
		return self._status

	def getNodeIpAddress(self):
		return self._ipAddress

	def getNodeId(self):
		return self._id

	def getNodeNeedsInspection(self):
		return self._needsInspection

	def getNodeBrikId(self):
		return self._brikId


class Vcenter():
	def __init__(self,id,managedId,ip,userName,configuredSlaDomainId,primaryClusterUuid):
		self._id = id
		self._managedId = managedId
		self._ip = ip
		self._userName = userName
		self._configuredSlaDomainId = configuredSlaDomainId
		self._primaryClusterUuid = primaryClusterUuid

	def getVcenterId(self):
		return self._id

	def getVcenterManagedId(self):
		return self._managedId

	def getVcenterIp(self):
		return self._ip

	def getVcenterUserName(self):
		return self._userName

	def getVcenterConfiguredSlaDomainId(self):
		return self._configuredSlaDomainId

	def getVcenterPrmimaryClusterUuid(self):
		self._primaryClusterUuid 
		
