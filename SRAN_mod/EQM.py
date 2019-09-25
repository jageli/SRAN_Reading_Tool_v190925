from public_fuction_lij import *
from checkbox_name import *

def BBMOD_EQM(node,NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    prodCodePlanned = get_child_node(node, "prodCodePlanned")
    useFullCapacity = get_child_node(node, "useFullCapacity")

    # 写入列表
    NODE_LIST[checkbox_name.index("BBMOD_EQM")].append([class1, EnodeBID, version, distName,prodCodePlanned, useFullCapacity])


def RMOD_EQM(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    climateControlProfiling = get_child_node(node, "climateControlProfiling")
    linkSpeed = get_child_node(node, "linkSpeed")
    moduleLocation = get_child_node(node, "moduleLocation")
    prodCodePlanned = get_child_node(node, "prodCodePlanned")
    # 写入列表
    NODE_LIST[checkbox_name.index("RMOD_EQM")].append([class1, EnodeBID, version, distName, climateControlProfiling, linkSpeed,
                          moduleLocation, prodCodePlanned])

def SMOD_EQM(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    moduleLocation = get_child_node(node, "moduleLocation")
    portMode = get_child_node(node, "portMode")
    prodCodePlanned = get_child_node(node, "prodCodePlanned")
    # 写入列表
    NODE_LIST[checkbox_name.index("SMOD_EQM")].append([class1, EnodeBID, version, distName, moduleLocation, portMode, prodCodePlanned])