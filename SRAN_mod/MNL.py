from public_fuction_lij import *
from checkbox_name import *
def GNSSE_MNL(node,NODE_LIST):
        class1 = node.attrib["class"]
        distName = node.attrib["distName"]
        EnodeBID = spliter_M(distName,1,"MRBTS-")
        version = node.attrib["version"]

        actGnssOutputLnaPowerSupply = get_child_node(node, "actGnssOutputLnaPowerSupply")
        gnssCableLength = get_child_node(node, "gnssCableLength")
        gnssControlMode = get_child_node(node, "gnssControlMode")
        gnssReceiverHoldoverMode = get_child_node(node, "gnssReceiverHoldoverMode")
        locationMode = get_child_node(node, "locationMode")

        # 写入列表
        NODE_LIST[checkbox_name.index("GNSSE_MNL")].append([class1, EnodeBID, version, distName, actGnssOutputLnaPowerSupply, gnssCableLength,
                             gnssControlMode, gnssReceiverHoldoverMode,locationMode])

def CHANNEL(node,NODE_LIST):
        class1 = node.attrib["class"]
        distName = node.attrib["distName"]
        EnodeBID = spliter_M(distName,1,"MRBTS-")
        version = node.attrib["version"]
        cellid = spliter_N(spliter_M(distName, 5,""),1)

        antlDN = get_child_node(node, "antlDN")
        direction = get_child_node(node, "direction")

        # 写入列表
        NODE_LIST[checkbox_name.index("CHANNEL")].append([class1, EnodeBID, version, distName, antlDN,direction,cellid])

def CHANNELGROUP(node,NODE_LIST):
            class1 = node.attrib["class"]
            distName = node.attrib["distName"]
            EnodeBID = spliter_M(distName, 1, "MRBTS-")
            version = node.attrib["version"]

            # 写入列表
            NODE_LIST[checkbox_name.index("CHANNELGROUP")].append([class1, EnodeBID, version, distName])

def MPLANENW(node,NODE_LIST):
            class1 = node.attrib["class"]
            distName = node.attrib["distName"]
            EnodeBID = spliter_M(distName, 1, "MRBTS-")
            version = node.attrib["version"]
            # id = node.attrib["id"]

            oamPeerIpAddress = get_child_node(node, "oamPeerIpAddress")
            oamTls = get_child_node(node, "oamTls")

            # 写入列表
            NODE_LIST[checkbox_name.index("MPLANENW")].append([class1, EnodeBID, version, distName, oamPeerIpAddress, oamTls])

def MNL_R(node,NODE_LIST):
                class1 = node.attrib["class"]
                distName = node.attrib["distName"]
                EnodeBID = spliter_M(distName,1,"MRBTS-")
                version = node.attrib["version"]

                activeGSMRATSWVersion = get_child_node(node, "activeGSMRATSWVersion")
                activeLTERATSWVersion = get_child_node(node, "activeLTERATSWVersion")
                activeSWActivationTime = get_child_node(node, "activeSWActivationTime")
                activeSWReleaseVersion = get_child_node(node, "activeSWReleaseVersion")
                configDataRevisionNumber = get_child_node(node, "configDataRevisionNumber")
                productVariant = get_child_node(node, "productVariant")
                sharedRfTechnologies = get_child_node(node, "sharedRfTechnologies")

                # 写入列表
                NODE_LIST[checkbox_name.index("MNL_R")].append([class1, EnodeBID, version, distName, activeGSMRATSWVersion,activeLTERATSWVersion
                                      ,activeSWActivationTime,activeSWReleaseVersion,configDataRevisionNumber,
                                      productVariant,sharedRfTechnologies])

def SECADM(node,NODE_LIST):
                class1 = node.attrib["class"]
                distName = node.attrib["distName"]
                EnodeBID = spliter_M(distName,1,"MRBTS-")
                version = node.attrib["version"]

                actServiceAccountSsh = get_child_node(node, "actServiceAccountSsh")

                # 写入列表
                NODE_LIST[checkbox_name.index("SECADM")].append([class1, EnodeBID, version, distName,actServiceAccountSsh])

def FEATCADM(node,NODE_LIST):
            class1 = node.attrib["class"]
            distName = node.attrib["distName"]
            EnodeBID = spliter_M(distName, 1, "MRBTS-")
            version = node.attrib["version"]

            systemAcctPermEnable = get_child_node(node, "systemAcctPermEnable")

            # 写入列表
            NODE_LIST[checkbox_name.index("FEATCADM")].append([class1, EnodeBID, version, distName, systemAcctPermEnable])


def TIME1(node, NODE_LIST):
         class1 = node.attrib["class"]
         distName = node.attrib["distName"]
         EnodeBID = spliter_M(distName, 1, "MRBTS-")
         version = node.attrib["version"]

         changeDate = get_child_node(node, "changeDate")
         offsetAfter = get_child_node(node, "offsetAfter")
         offsetBefore = get_child_node(node, "offsetBefore")
         timeZone = get_child_node(node, "timeZone")

         # 写入列表
         NODE_LIST[checkbox_name.index("TIME1")].append([class1, EnodeBID, version, distName, changeDate,offsetAfter,
                                                       offsetBefore,timeZone])