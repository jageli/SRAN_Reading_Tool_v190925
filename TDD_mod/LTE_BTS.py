from public_fuction_lij import *
from checkbox_name import *

def LNBTS(node,NODE_LIST):
        class1 = node.attrib["class"]
        disName = node.attrib["distName"]
        EnodeBID = spliter_M(disName,1,"MRBTS-")
        version = node.attrib["version"]

        enbName = get_child_node(node, "enbName")
        actDLCAggr = get_child_node(node, "actDLCAggr")
        operationalState = get_child_node(node, "operationalState")

        #写入列表
        NODE_LIST[checkbox_name.index("LNBTS")].append([class1,EnodeBID,version,disName,enbName,actDLCAggr,operationalState])


def LNCEL(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]

    cellName = get_child_node(node, "cellName")
    cellTechnology = get_child_node(node, "cellTechnology")
    lcrId = get_child_node(node, "lcrId")
    phyCellId = get_child_node(node, "phyCellId")
    pMax = get_child_node(node, "pMax")
    administrativeState = get_child_node(node, "administrativeState")
    tac = get_child_node(node, "tac")

    # 写入列表
    NODE_LIST[checkbox_name.index("LNCEL")].append([class1, EnodeBID, version, disName, lcrId, cellName, cellTechnology,phyCellId, pMax,
                         administrativeState, tac])

def LNCEL_TDD(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    lcelcI = spliter_M(disName, 3, "LNCEL-")
    version = node.attrib["version"]

    chBw = get_child_node(node, "chBw")
    earfcn = get_child_node(node, "earfcn")
    dlRsBoost = get_child_node(node, "dlRsBoost")
    actSuperCell = get_child_node(node, "actSuperCell")
    dlMimoMode = get_child_node(node, "dlMimoMode")
    # 写入列表
    NODE_LIST[checkbox_name.index("LNCEL_TDD")].append([class1, EnodeBID, version, disName, lcelcI, chBw, earfcn, dlRsBoost,actSuperCell,dlMimoMode])

def LNMME(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    LNMMEID = spliter_M(disName, 3, "LNMME-")
    version = node.attrib["version"]

    administrativeState = get_child_node(node, "administrativeState")
    ipAddrPrim = get_child_node(node, "ipAddrPrim")
    ipAddrSec = get_child_node(node, "ipAddrSec")
    mmeRatSupport = get_child_node(node, "mmeRatSupport")
    relMmeCap = get_child_node(node, "relMmeCap")
    s1LinkStatus = get_child_node(node, "s1LinkStatus")
    transportNwId = get_child_node(node, "transportNwId")

    # 写入列表
    NODE_LIST[checkbox_name.index("LNMME")].append([class1, EnodeBID, version, disName, LNMMEID, administrativeState, ipAddrPrim, ipAddrSec,
                          mmeRatSupport, relMmeCap, s1LinkStatus, transportNwId])

def NBIOT_FDD(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    lcelcI = spliter_M(disName, 3, "LNCEL-")
    version = node.attrib["version"]

    dlChBw = get_child_node(node, "dlChBw")
    standaloneEarfcnDL = get_child_node(node, "standaloneEarfcnDL")
    standaloneEarfcnUL = get_child_node(node, "standaloneEarfcnUL")
    dlPwrBoost = get_child_node(node, "dlPwrBoost")

    # 写入列表
    NODE_LIST[checkbox_name.index("NBIOT_FDD")].append([class1, EnodeBID, version, disName, lcelcI, dlChBw, standaloneEarfcnUL, standaloneEarfcnDL, dlPwrBoost])

# def MRBTS(node, NODE_LIST):
#     class1 = node.attrib["class"]
#     disName = node.attrib["distName"]
#     EnodeBID = spliter_M(disName, 1, "MRBTS-")
#     version = node.attrib["version"]
#
#     btsName = get_child_node(node, "btsName")
#     latitude = get_child_node(node, "latitude")
#     longitude = get_child_node(node, "longitude")
#     altitude = get_child_node(node, "altitude")
#      # 写入列表
#     NODE_LIST[checkbox_name.index("MRBTS")].append([class1, EnodeBID, version, disName, btsName, latitude, longitude,altitude])
#


