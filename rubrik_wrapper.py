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

        def getApi(self,url):
                return requests.get(self.api_url + url,verify=False,headers=self.session.getAuthHeader())

        def getCluster(self):
                return self.getApi("/cluster/me").json()


        def getClusterBootstrap(self):
                return self.getApi("/cluster/me/bootstrap").json()

        def get_cluster_brik_count(self):
                return self.getApi("/cluster/me/brik_count").json()

        def get_cluster_decommission_node(self):
                return self.getApi("/cluster/me/decommission_node").json()

        def get_cluster_discover(self):
                return self.getApi("/cluster/me/discover").json()

        def get_cluster_disk(self):
                return self.getApi("/cluster/me/disk").json()

        def get_cluster_disk_capacity(self):
                return self.getApi("/cluster/me/disk_capacity").json()

        def get_cluster_dns_nameserver(self):
                return self.getApi("/cluster/me/dns_nameserver").json()

        def get_cluster_dns_search_domain(self):
                return self.getApi("/cluster/me/dns_search_domain").json()

        def get_cluster_flash_capacity(self):
                return self.getApi("/cluster/me/flash_capacity").json()

        def get_cluster_io_stats(self):
                return self.getApi("/cluster/me/io_stats").json()


        def get_cluster_is_single_node(self):
                return self.getApi("/cluster/me/is_single_node").json()

        def get_cluster_name(self):
                return self.getApi("/cluster/me/name").json()

        def get_cluster_memory_capacity(self):
                return self.getApi("/cluster/me/memory_capacity").json()

        def get_cluster_node(self):
                return self.getApi("/cluster/me/node").json()

        def get_cluster_ntp_server(self):
                return self.getApi("/cluster/me/ntp_server").json()

        def get_cluster_version(self):
                return self.getApi("/cluster/me/version").json()

        def get_cluster_vlan(self):
                return self.getApi("/cluster/me/vlan").json()

        def get_sla_domain(self):
                return self.getApi("/sla_domain").json()["data"]

        def get_sla_domain_id(self,id):
                return self.getApi("/sla_domain/" + id).json()["data"]


        def get_user(self):
                return self.getApi("/user").json()

        def get_user_notification(self):
                return self.getApi("/user_notification").json()

        def get_vcenter(self):
                return self.getApi("/vmware/vcenter").json()


        def get_virtual_disk(self):
                return self.getApi("/vmware/virtual_disk").json()


        def get_virtual_disk_id(self,id):
                return self.getApi("/vmware/virtual_disk/" + id).json()


        def get_vm(self):
                r = requests.get(self.api_url+'/vmware/vm',verify=False,headers=self.session.getAuthHeader())
                total =  r.json()["total"]
                payload = {}
                payload["limit"] = total
                r = requests.get(self.api_url+'/vmware/vm',verify=False,params=payload,headers=self.session.getAuthHeader())
                return r.json()

        def get_vm_id(self,id):
                return self.getApi("/vmware/vm/" + id).json()


        def get_vm_id_snapshot(self,id):
                return self.getApi("/vmware/vm/"+ id +"/snapshot").json()

        def get_vm_count(self):
                return self.getApi("/vmware/vm/count").json()

        def get_vm_credential_failure(self):
                return self.getApi("/vmware/vm/credential_failure").json()


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


class Vm():
        def __init__(self,id,managedId,moid,name,vcenterId,hostname,hostid,powerstatus):
                self.id = id
                self.managedId = managedId
                self.moid = moid
                self.name = name
                self.vcenterId = vcenterId
                self.hostname = hostname
                self.hostId = hostid
                self.powerStatus = powerstatus

class SlaDomain():
        def __init__(self,id,name,vmlist):
                self.id = id
                self.name = name
                self.numVms = 0
                self.vmList = vmlist