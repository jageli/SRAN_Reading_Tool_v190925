from public_fuction_lij import *
from checkbox_name import *


def IPRT(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    for child_node in (node):
        IPRT_ID = 1
        for child1_node in (child_node):
            destIpAddr = get_child_node(child1_node, "destIpAddr")
            destinationIpPrefixLength = get_child_node(child1_node, "destinationIpPrefixLength")
            gateway = get_child_node(child1_node, "gateway")
            preSrcIpv4Addr = get_child_node(child1_node, "preSrcIpv4Addr")
            preference = get_child_node(child1_node, "preference")

            # 写入列表
            NODE_LIST[checkbox_name.index("IPRT")].append([class1, EnodeBID, version, disName, destIpAddr, destinationIpPrefixLength, gateway,
                                  preSrcIpv4Addr, preference, IPRT_ID])
            IPRT_ID += 1

def IPADDRESSV4(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    IPIFID = spliter_M(disName, 5, "IPIF-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    ipAddressAllocationMethod = get_child_node(node, "ipAddressAllocationMethod")
    localIpAddr = get_child_node(node, "localIpAddr")
    localIpPrefixLength = get_child_node(node, "localIpPrefixLength")
    # 写入列表
    NODE_LIST[checkbox_name.index("IPADDRESSV4")].append([class1, EnodeBID, version, disName, IPIFID, ipAddressAllocationMethod, localIpAddr,
                          localIpPrefixLength])

def VLANIF(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    VLANIFID = spliter_M(disName, 6, "VLANIF-")
    version = node.attrib["version"]

    vlanId = get_child_node(node, "vlanId")

    # 写入列表
    NODE_LIST[checkbox_name.index("VLANIF")].append([class1, EnodeBID, version, disName, VLANIFID, vlanId])

def IVIF(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    IVIFID = spliter_M(disName, 6, "IVIF-")
    version = node.attrib["version"]

    localIpAddr = get_child_node(node, "localIpAddr")
    netmask = get_child_node(node, "netmask")
    qosEnabled = get_child_node(node, "qosEnabled")
    vlanId = get_child_node(node, "vlanId")

    # 写入列表
    NODE_LIST[checkbox_name.index("IVIF")].append([class1, EnodeBID, version, disName, IVIFID,localIpAddr,netmask,qosEnabled, vlanId])