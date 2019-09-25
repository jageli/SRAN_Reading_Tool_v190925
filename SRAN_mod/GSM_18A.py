from public_fuction_lij import *
from checkbox_name import *

def UNIT(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    BSC = spliter_M(distName, 1, "BSC-")
    BCF = spliter_M(distName, 2, "BCF-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    identificationCode = get_child_node(node, "identificationCode")
    operationalState = get_child_node(node, "operationalState")
    position = get_child_node(node, "position")
    serialNumber = get_child_node(node, "serialNumber")
    unitId = get_child_node(node, "unitId")
    unitType = get_child_node(node, "unitType")
    vendorName = get_child_node(node, "vendorName")
    version_HW = get_child_node(node, "version")

    availabilityStatus = get_child_node2(node, "availabilityStatus")
    # 写入列表
    NODE_LIST[checkbox_name.index("UNIT")].append([class1, version, distName, BSC, BCF, identificationCode, operationalState,
                                                   position,serialNumber,unitId,unitType,vendorName,version_HW,availabilityStatus])

def HW_GSM(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    BSC = spliter_M(distName, 1, "BSC-")
    BCF = spliter_M(distName, 2, "BCF-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    operationalState = get_child_node(node, "operationalState")
    systemTitle = get_child_node(node, "systemTitle")
    vendorName = get_child_node(node, "vendorName")

    # 写入列表
    NODE_LIST[checkbox_name.index("HW_GSM")].append([class1, version, distName, BSC, BCF, operationalState, systemTitle,
                                                     vendorName])