from public_fuction_lij import *
from checkbox_name import *

def MRBTS(node,NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName ,1 ,"MRBTS-")
    version = node.attrib["version"]

    altitude = get_child_node(node, "altitude")
    btsName = get_child_node(node, "btsName")
    latitude = get_child_node(node, "latitude")
    longitude = get_child_node(node, "longitude")

    # 写入列表
    NODE_LIST[checkbox_name.index("MRBTS")].append([class1, EnodeBID, version, disName, btsName, latitude ,longitude,altitude])
    # print(NODE_LIST)


def IPNO(node,NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName ,1 ,"MRBTS-")
    version = node.attrib["version"]

    btsId = get_child_node(node, "btsId")
    cPlaneIpAddress = get_child_node(node, "cPlaneIpAddress")
    mPlaneIpAddress = get_child_node(node, "mPlaneIpAddress")
    oamIpAddr = get_child_node(node, "oamIpAddr")
    omsTls = get_child_node(node, "omsTls")
    sPlaneIpAddress = get_child_node(node, "sPlaneIpAddress")
    secOmsIpAddr = get_child_node(node, "secOmsIpAddr")
    servingOms = get_child_node(node, "servingOms")
    servingOmsAdminSetting = get_child_node(node, "servingOmsAdminSetting")
    twampMessageRate = get_child_node(node, "twampMessageRate")
    twampReflectorPort = get_child_node(node, "twampReflectorPort")
    uPlaneIpAddress = get_child_node(node, "uPlaneIpAddress")

    # 写入列表
    NODE_LIST[checkbox_name.index("IPNO")].append([class1, EnodeBID, version, disName, btsId, cPlaneIpAddress, mPlaneIpAddress ,oamIpAddr, omsTls, sPlaneIpAddress, secOmsIpAddr ,servingOms,servingOmsAdminSetting,twampMessageRate,twampReflectorPort,uPlaneIpAddress])

