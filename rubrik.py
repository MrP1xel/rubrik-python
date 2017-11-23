from rubrik_wrapper import *

#About user
def get_all_users(Cluster):
        user_list = []
        for user in Cluster.get_user():
                user_list.append(User(user["firstName"],user["authDomainId"],user["isAdmin"],user["role"],user["lastName"],user["lastName"],user["emailAddress"],user["id"]))
        return user_list


#About Cluster
def getInfo(Cluster):
        return Cluster.getCluster()

def getVersion(Cluster):
        return getInfo(Cluster)["version"]

def getId(Cluster):
        return getInfo(Cluster)["id"]

def getIsSingleNode(Cluster):
        return getInfo(Cluster)["isSingleNode"]

def getBrikCount(Cluster):
        return Cluster.get_cluster_brik_count()["count"]

def getDisk(Cluster):
        disk_list = []
        for disk in Cluster.get_cluster_disk()["data"]:
                disk_list.append(Disk(disk["id"],disk["status"],disk["isEncrypted"],disk["diskType"],disk["nodeId"],disk["capacityBytes"],disk["path"],disk["unallocatedBytes"],disk["usableBytes"]))
        return disk_list


def getDiskCapacity(Cluster):
        return Cluster.get_cluster_disk_capacity()["bytes"]

def getDnsServer(Cluster):
        return Cluster.get_cluster_dns_nameserver()["data"]
