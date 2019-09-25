from public_fuction_lij import *
from checkbox_name import *

def CARRIERGROUPC_R(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    # GNCELID = spliterGNCEL(distName)
    GNCELID = spliter_M(distName, 4, "GNCEL-")
    # print(GNCELID)

    version = node.attrib["version"]

    channelGroupId = get_child_node(node, "channelGroupId")
    trxAdminState = get_child_node(node, "trxAdminState")

    # 写入列表
    NODE_LIST[checkbox_name.index("CARRIERGROUPC_R")].append([class1, EnodeBID, version, distName, GNCELID, channelGroupId, trxAdminState])

def GNBCF(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]

    bcfId = get_child_node(node, "bcfId")
    bscId = get_child_node(node, "bscId")
    mPlaneRemoteIpAddressOmuSig = get_child_node(node, "mPlaneRemoteIpAddressOmuSig")
    sctpPortOmuSig = get_child_node(node, "sctpPortOmuSig")
    txPowerPooling = get_child_node(node, "txPowerPooling")

    # 写入列表
    NODE_LIST[checkbox_name.index("GNBCF")].append(
        [class1, EnodeBID, version, distName, bcfId, bscId, mPlaneRemoteIpAddressOmuSig, sctpPortOmuSig,
         txPowerPooling])

def GNCEL(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]

    lcelcId = get_child_node(node, "lcelcId")
    perTrxPower = get_child_node(node, "perTrxPower")

    # 写入列表
    NODE_LIST[checkbox_name.index("GNCEL")].append([class1, EnodeBID, version, distName, lcelcId, perTrxPower])

def GNCEL_R(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    lcelcI = spliter_M(distName, 4, "GNCEL-")
    version = node.attrib["version"]

    gsmBtsId = get_child_node(node, "gsmBtsId")

    # 写入列表
    NODE_LIST[checkbox_name.index("GNCEL_R")].append([class1, EnodeBID, version, distName, lcelcI, gsmBtsId])
