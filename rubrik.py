from rubrik_w2 import *


def getVersion(Session):
        return Session._getApi(Session.CLUSTER_ID_VERSION)

def getBrikCount(Session):
        return Session._getApi(Session.CLUSTER_ID_BRIK_COUNT)["count"]

def getVirtualDisk(Session):
        for disk in Session._getApi(Session.VIRTUAL_DISK)["data"]:
                print disk

def getUserList(Session):
        user_list = []
        for user in  Session._getApi(Session.USER):
                user_list.append(User(user["username"],user["firstName"],user["authDomainId"],user["isAdmin"],user["role"],user["lastName"],user["emailAddress"],user["id"]))
        return user_list


def getUserInfo(Session,user_id):
        return Session._getApiWithId(Session.USER,user_id)

def getVlan(Session):
        vlan_list = []
        for vlan in Session._getApi(Session.CLUSTER_ID_VLAN)["data"]:
                vlan_list.append(vlan)
        return vlan_list
