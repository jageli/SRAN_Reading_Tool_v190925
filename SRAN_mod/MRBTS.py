from public_fuction_lij import *
from checkbox_name import *
def MRBTS(node,NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName ,1 ,"MRBTS-")
    version = node.attrib["version"]

    name = get_child_node(node, "name")
    altitude = get_child_node(node, "altitude")
    btsName = get_child_node(node, "btsName")
    latitude1 = get_child_node(node, "latitude")
    latitude = str(latitude1)
    longitude1 = get_child_node(node, "longitude")
    longitude = str(longitude1)

    # 写入列表
    NODE_LIST[checkbox_name.index("MRBTS")].append([class1, EnodeBID, version, distName, name, altitude, btsName, latitude ,longitude])
    QtWidgets.QApplication.processEvents()