from public_fuction_lij import *
from checkbox_name import *

def BBMOD_EQM(node,NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    prodCodePlanned = get_child_node(node, "prodCodePlanned")
    radioProtSearchOrder=get_child_node(node, "radioProtSearchOrder")
    useFullCapacity = get_child_node(node, "useFullCapacity")

    # 写入列表
    NODE_LIST[checkbox_name.index("BBMOD_EQM")].append([class1, EnodeBID, version, disName,prodCodePlanned,radioProtSearchOrder, useFullCapacity])


def RMOD_EQM(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    cpriARfSharing = get_child_node(node, "cpriARfSharing")
    digitalCombinerMode = get_child_node(node, "digitalCombinerMode")
    moduleLocation = get_child_node(node, "moduleLocation")
    prodCodePlanned = get_child_node(node, "prodCodePlanned")
    # 写入列表
    NODE_LIST[checkbox_name.index("RMOD_EQM")].append([class1, EnodeBID, version, disName, cpriARfSharing, digitalCombinerMode,
                          moduleLocation, prodCodePlanned])

def SMOD_EQM(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    moduleLocation = get_child_node(node, "moduleLocation")
    portMode = get_child_node(node, "portMode")
    positionInSubrack = get_child_node(node, "positionInSubrack")
    prodCodePlanned = get_child_node(node, "prodCodePlanned")
    # 写入列表
    NODE_LIST[checkbox_name.index("SMOD_EQM")].append([class1, EnodeBID, version, disName, moduleLocation, portMode,positionInSubrack, prodCodePlanned])