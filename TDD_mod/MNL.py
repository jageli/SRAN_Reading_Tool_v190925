from public_fuction_lij import *
from checkbox_name import *
def GNSSE_MNL(node,NODE_LIST):
        class1 = node.attrib["class"]
        disName = node.attrib["distName"]
        EnodeBID = spliter_M(disName,1,"MRBTS-")
        version = node.attrib["version"]

        actGnssOutputLnaPowerSupply = get_child_node(node, "actGnssOutputLnaPowerSupply")
        gnssCableLength = get_child_node(node, "gnssCableLength")
        gnssControlMode = get_child_node(node, "gnssControlMode")
        gnssReceiverHoldoverMode = get_child_node(node, "gnssReceiverHoldoverMode")
        locationMode = get_child_node(node, "locationMode")

        # 写入列表
        NODE_LIST[checkbox_name.index("GNSSE_MNL")].append([class1, EnodeBID, version, disName, actGnssOutputLnaPowerSupply, gnssCableLength,
                             gnssControlMode, gnssReceiverHoldoverMode,locationMode])

def CHANNEL(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]
    cellid = spliter_N(spliter_M(disName, 5, ""), 1)
    if get_child_node(node, "resourceDN")== None :
        antlDN = get_child_node(node, "antlDN")
    else:
        antlDN = get_child_node(node, "resourceDN")


    RmodId = spliter_N(spliter_M(antlDN, 3, ""), 1)
    direction = get_child_node(node, "direction")

    # 写入列表
    NODE_LIST[checkbox_name.index("CHANNEL")].append(
        [class1, EnodeBID, version, disName, antlDN,RmodId,direction, cellid])

    # print(NODE_LIST)

def LCELL(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]
    cellid = spliter_N(spliter_M(disName, 5, ""), 1)


    # 写入列表
    NODE_LIST[checkbox_name.index("LCELL")].append(
        [class1, EnodeBID, version, disName,cellid])


def CHANNELGROUP(node,NODE_LIST):
            class1 = node.attrib["class"]
            disName = node.attrib["distName"]
            EnodeBID = spliter_M(disName, 1, "MRBTS-")
            version = node.attrib["version"]

            # 写入列表
            NODE_LIST[checkbox_name.index("CHANNELGROUP")].append([class1, EnodeBID, version, disName])

def MPLANENW(node,NODE_LIST):
            class1 = node.attrib["class"]
            disName = node.attrib["distName"]
            EnodeBID = spliter_M(disName, 1, "MRBTS-")
            version = node.attrib["version"]
            # id = node.attrib["id"]

            oamPeerIpAddress = get_child_node(node, "oamPeerIpAddress")
            oamTls = get_child_node(node, "oamTls")

            # 写入列表
            NODE_LIST[checkbox_name.index("MPLANENW")].append([class1, EnodeBID, version, disName, oamPeerIpAddress, oamTls])

def MNL_R(node,NODE_LIST):
                class1 = node.attrib["class"]
                disName = node.attrib["distName"]
                EnodeBID = spliter_M(disName,1,"MRBTS-")
                version = node.attrib["version"]

                activeGSMRATSWVersion = get_child_node(node, "activeGSMRATSWVersion")
                activeLTERATSWVersion = get_child_node(node, "activeLTERATSWVersion")
                activeSWActivationTime = get_child_node(node, "activeSWActivationTime")
                activeSWReleaseVersion = get_child_node(node, "activeSWReleaseVersion")
                configDataRevisionNumber = get_child_node(node, "configDataRevisionNumber")
                productVariant = get_child_node(node, "productVariant")
                sharedRfTechnologies = get_child_node(node, "sharedRfTechnologies")

                # 写入列表
                NODE_LIST[checkbox_name.index("MNL_R")].append([class1, EnodeBID, version, disName, activeGSMRATSWVersion,activeLTERATSWVersion
                                      ,activeSWActivationTime,activeSWReleaseVersion,configDataRevisionNumber,
                                      productVariant,sharedRfTechnologies])

def SECADM(node,NODE_LIST):
                class1 = node.attrib["class"]
                disName = node.attrib["distName"]
                EnodeBID = spliter_M(disName,1,"MRBTS-")
                version = node.attrib["version"]

                actServiceAccountSsh = get_child_node(node, "actServiceAccountSsh")

                # 写入列表
                NODE_LIST[checkbox_name.index("SECADM")].append([class1, EnodeBID, version, disName,actServiceAccountSsh])
def CLOCK(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]

    holdOverModeUsed = get_child_node(node, "holdOverModeUsed")
    outputConfiguration1Pps = get_child_node(node, "outputConfiguration1Pps")
    outputConfiguration2M048 = get_child_node(node, "outputConfiguration2M048")
    sModDN = get_child_node(node, "sModDN")
    totalDelayFromSHM = get_child_node(node, "totalDelayFromSHM")

    for child_node in (node):
        for child1_node in (child_node):
            syncInputPrio = get_child_node(child1_node, "syncInputPrio")
            syncInputType = get_child_node(child1_node, "syncInputType")

    NODE_LIST[checkbox_name.index("CLOCK")].append(
        [class1, EnodeBID, version, disName, holdOverModeUsed,outputConfiguration1Pps,outputConfiguration2M048,sModDN,syncInputPrio,syncInputType,totalDelayFromSHM])



def FEATCADM(node,NODE_LIST):
            class1 = node.attrib["class"]
            disName = node.attrib["distName"]
            EnodeBID = spliter_M(disName, 1, "MRBTS-")
            version = node.attrib["version"]

            systemAcctPermEnable = get_child_node(node, "systemAcctPermEnable")

            # 写入列表
            NODE_LIST[checkbox_name.index("FEATCADM")].append([class1, EnodeBID, version, disName, systemAcctPermEnable])