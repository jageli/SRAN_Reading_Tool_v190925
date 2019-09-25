from public_fuction_lij import *
from checkbox_name import *

def LNBTS(node,NODE_LIST):
        class1 = node.attrib["class"]
        distName = node.attrib["distName"]
        EnodeBID = spliter_M(distName,1,"MRBTS-")
        version = node.attrib["version"]

        enbName = get_child_node(node, "enbName")
        operationalState = get_child_node(node, "operationalState")

        #写入列表
        NODE_LIST[checkbox_name.index("LNBTS")].append([class1,EnodeBID,version,distName,enbName,operationalState])


def LNCEL(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]

    cellName = get_child_node(node, "cellName")
    cellTechnology = get_child_node(node, "cellTechnology")
    lcrId = get_child_node(node, "lcrId")
    pMax = get_child_node(node, "pMax")
    administrativeState = get_child_node(node, "administrativeState")
    tac = get_child_node(node, "tac")

    # 写入列表
    NODE_LIST[checkbox_name.index("LNCEL")].append([class1, EnodeBID, version, distName, lcrId, cellName, cellTechnology, pMax,
                         administrativeState, tac])

def LNCEL_FDD(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    lcelcI = spliter_M(distName, 3, "LNCEL-")
    version = node.attrib["version"]

    dlChBw = get_child_node(node, "dlChBw")
    earfcnDL = get_child_node(node, "earfcnDL")
    earfcnUL = get_child_node(node, "earfcnUL")
    dlRsBoost = get_child_node(node, "dlRsBoost")
    # 写入列表
    NODE_LIST[checkbox_name.index("LNCEL_FDD")].append([class1, EnodeBID, version, distName, lcelcI, dlChBw, earfcnUL, earfcnDL, dlRsBoost])

def LNMME(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    LNMMEID = spliter_M(distName, 3, "LNMME-")
    version = node.attrib["version"]

    administrativeState = get_child_node(node, "administrativeState")
    ipAddrPrim = get_child_node(node, "ipAddrPrim")
    ipAddrSec = get_child_node(node, "ipAddrSec")
    mmeRatSupport = get_child_node(node, "mmeRatSupport")
    relMmeCap = get_child_node(node, "relMmeCap")
    s1LinkStatus = get_child_node(node, "s1LinkStatus")
    transportNwId = get_child_node(node, "transportNwId")

    # 写入列表
    NODE_LIST[checkbox_name.index("LNMME")].append([class1, EnodeBID, version, distName, LNMMEID, administrativeState, ipAddrPrim, ipAddrSec,
                          mmeRatSupport, relMmeCap, s1LinkStatus, transportNwId])

def NBIOT_FDD(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    lcelcI = spliter_M(distName, 3, "LNCEL-")
    version = node.attrib["version"]

    dlChBw = get_child_node(node, "dlChBw")
    standaloneEarfcnDL = get_child_node(node, "standaloneEarfcnDL")
    standaloneEarfcnUL = get_child_node(node, "standaloneEarfcnUL")
    dlPwrBoost = get_child_node(node, "dlPwrBoost")

    # 写入列表
    NODE_LIST[checkbox_name.index("NBIOT_FDD")].append([class1, EnodeBID, version, distName, lcelcI, dlChBw, standaloneEarfcnUL, standaloneEarfcnDL, dlPwrBoost])

