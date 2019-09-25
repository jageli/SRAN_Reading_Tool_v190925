from public_fuction_lij import *
from checkbox_name import *

def HW(node,NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]

    locationName = get_child_node(node, "locationName")
    swVersion = get_child_node(node, "swVersion")
    userLabel = get_child_node(node, "userLabel")
    vendorName = get_child_node(node, "vendorName")

    # 写入列表
    NODE_LIST[checkbox_name.index("HW")].append([class1, EnodeBID, version, distName, locationName, swVersion, userLabel, vendorName])

def GNSSE_HW(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]
    inventoryUnitType = get_child_node(node, "inventoryUnitType")
    # 写入列表
    NODE_LIST[checkbox_name.index("GNSSE_HW")].append([class1, EnodeBID, version, distName, inventoryUnitType])

def BBMOD_HW(node,NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    inventoryUnitType = get_child_node(node, "inventoryUnitType")
    serialNumber = get_child_node(node, "serialNumber")
    vendorUnitTypeNumber = get_child_node(node, "vendorUnitTypeNumber")

    # 写入列表
    NODE_LIST[checkbox_name.index("BBMOD_HW")].append([class1, EnodeBID, version, distName, inventoryUnitType, serialNumber, vendorUnitTypeNumber])

def SMOD_HW(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    inventoryUnitType = get_child_node(node, "inventoryUnitType")
    serialNumber = get_child_node(node, "serialNumber")
    vendorUnitTypeNumber = get_child_node(node, "vendorUnitTypeNumber")

    # 写入列表
    NODE_LIST[checkbox_name.index("SMOD_HW")].append([class1, EnodeBID, version, distName, inventoryUnitType, serialNumber, vendorUnitTypeNumber])

def RMOD_HW(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    inventoryUnitType = get_child_node(node, "inventoryUnitType")
    serialNumber = get_child_node(node, "serialNumber")
    vendorName = get_child_node(node, "vendorName")
    vendorUnitFamilyType = get_child_node(node, "vendorUnitFamilyType")
    vendorUnitTypeNumber = get_child_node(node, "vendorUnitTypeNumber")
    versionNumber = get_child_node(node, "versionNumber")

    # 写入列表
    NODE_LIST[checkbox_name.index("RMOD_HW")].append([class1, EnodeBID, version, distName, inventoryUnitType, serialNumber, vendorName,
                          vendorUnitFamilyType, vendorUnitTypeNumber, versionNumber])