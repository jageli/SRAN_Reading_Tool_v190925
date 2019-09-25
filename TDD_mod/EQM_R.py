from public_fuction_lij import *
from checkbox_name import *

def SMOD_R(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    activeRole = get_child_node(node, "activeRole")
    configDN = get_child_node(node, "configDN")
    eutraSupport = get_child_node(node, "eutraSupport")
    function = get_child_node(node, "function")
    geranSupport = get_child_node(node, "geranSupport")
    horizontalPosition = get_child_node(node, "horizontalPosition")
    operationalState = get_child_node(node, "operationalState")
    productCode = get_child_node(node, "productCode")
    productName = get_child_node(node, "productName")
    utranSupport = get_child_node(node, "utranSupport")
    verticalPosition = get_child_node(node, "verticalPosition")
    serialNumber = get_child_node(node, "serialNumber")

    # 写入列表
    NODE_LIST[checkbox_name.index("SMOD_R")].append([class1, EnodeBID, version, disName, activeRole, configDN, eutraSupport, function, geranSupport,
                          horizontalPosition, operationalState, productCode, productName, utranSupport, verticalPosition
                             , serialNumber])

def BBMOD_R(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    configDN = get_child_node(node, "configDN")
    eutraSupport = get_child_node(node, "eutraSupport")
    function = get_child_node(node, "function")
    geranSupport = get_child_node(node, "geranSupport")
    horizontalPosition = get_child_node(node, "horizontalPosition")
    operationalState = get_child_node(node, "operationalState")
    productCode = get_child_node(node, "productCode")
    productName = get_child_node(node, "productName")
    utranSupport = get_child_node(node, "utranSupport")
    verticalPosition = get_child_node(node, "verticalPosition")
    serialNumber = get_child_node(node, "serialNumber")

    # 写入列表
    NODE_LIST[checkbox_name.index("BBMOD_R")].append([class1, EnodeBID, version, disName, configDN, eutraSupport, function, geranSupport,
                          horizontalPosition, operationalState, productCode, productName, utranSupport,
                          verticalPosition, serialNumber])

def RMOD_R(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    RmodId = spliter_N(spliter_M(disName, 4, ""), 1)

    aldManagementProtocol = get_child_node(node, "aldManagementProtocol")
    antennaPathDelayMeasurementCapable = get_child_node(node, "antennaPathDelayMeasurementCapable")
    blocking = get_child_node(node, "blocking")
    configDN = get_child_node(node, "configDN")
    hwVersion = get_child_node(node, "hwVersion")
    operationalState = get_child_node(node, "operationalState")
    productCode = get_child_node(node, "productCode")
    productName = get_child_node(node, "productName")
    radioMasterDN = get_child_node(node, "radioMasterDN")
    radioModuleHwReleaseCode = get_child_node(node, "radioModuleHwReleaseCode")
    rfmTransmitModeStatus = get_child_node(node, "rfmTransmitModeStatus")
    serialNumber = get_child_node(node, "serialNumber")

    # 写入列表
    NODE_LIST[checkbox_name.index("RMOD_R")].append(
        [class1, EnodeBID, version, disName,RmodId, aldManagementProtocol, antennaPathDelayMeasurementCapable,
         blocking, configDN, hwVersion, operationalState, productCode, productName, radioMasterDN,
         radioModuleHwReleaseCode, rfmTransmitModeStatus, serialNumber])

def GNSSE_R(node,NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]

    gnssAntennaAltitude = get_child_node(node, "gnssAntennaAltitude")
    gnssAntennaLatitude = get_child_node(node, "gnssAntennaLatitude")
    gnssAntennaLongitude = get_child_node(node, "gnssAntennaLongitude")
    gnssConstellationMode = get_child_node(node, "gnssConstellationMode")
    gnssUnitName = get_child_node(node, "gnssUnitName")

    # 写入列表
    NODE_LIST[checkbox_name.index("GNSSE_R")].append([class1, EnodeBID, version, disName, gnssAntennaAltitude, gnssAntennaLatitude,
                         gnssAntennaLongitude, gnssConstellationMode, gnssUnitName])

def SFP_R(node,NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]

    physicalPort = get_child_node(node, "physicalPort")
    serialNumber = get_child_node(node, "serialNumber")
    transmissionDistance = get_child_node(node, "transmissionDistance")
    transmissionRate = get_child_node(node, "transmissionRate")
    vendorPartNumber = get_child_node(node, "vendorPartNumber")

    NODE_LIST[checkbox_name.index("SFP_R")].append([class1, EnodeBID, version, disName, physicalPort,serialNumber,transmissionDistance,transmissionRate,vendorPartNumber])

def ASIRMOD_R(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]
    # id = node.attrib["id"]

    RmodId = spliter_N(spliter_M(disName, 4, ""), 1)

    antennaPathDelayMeasurementCapable = get_child_node(node, "antennaPathDelayMeasurementCapable")
    blocking = get_child_node(node, "blocking")
    configDN = get_child_node(node, "configDN")
    configuredAntCount=get_child_node(node, "configuredAntCount")
    hwVersion = get_child_node(node, "hwVersion")
    operationalState = get_child_node(node, "operationalState")
    productCode = get_child_node(node, "productCode")
    productName = get_child_node(node, "productName")
    radioMasterDN = get_child_node(node, "radioMasterDN")
    radioModuleHwReleaseCode = get_child_node(node, "radioModuleHwReleaseCode")
    serialNumber = get_child_node(node, "serialNumber")

    # 写入列表
    NODE_LIST[checkbox_name.index("ASIRMOD_R")].append(
        [class1, EnodeBID,version,disName,RmodId,antennaPathDelayMeasurementCapable,blocking,configDN,configuredAntCount,hwVersion,
         operationalState, productCode, productName, radioMasterDN, radioModuleHwReleaseCode, serialNumber])


def SYNC(node, NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]

    btsSyncMode = get_child_node(node, "btsSyncMode")
    manualFrameTimingAdjustment = get_child_node(node, "manualFrameTimingAdjustment")


    # 写入列表
    NODE_LIST[checkbox_name.index("SYNC")].append(
        [class1, EnodeBID,version,disName,btsSyncMode,manualFrameTimingAdjustment])

def CABLINK_R(node,NODE_LIST):
    class1 = node.attrib["class"]
    disName = node.attrib["distName"]
    EnodeBID = spliter_M(disName, 1, "MRBTS-")
    version = node.attrib["version"]

    cablinkType = get_child_node(node, "cablinkType")
    configDN = get_child_node(node, "configDN")
    firstEndpointDN = get_child_node(node, "firstEndpointDN")
    firstEndpointLabel = get_child_node(node, "firstEndpointLabel")
    firstEndpointPortId = get_child_node(node, "firstEndpointPortId")
    iqCompression = get_child_node(node, "iqCompression")
    linkMaxPhysicalCapacity = get_child_node(node, "linkMaxPhysicalCapacity")
    linkModeConfiguration = get_child_node(node, "linkModeConfiguration")
    linkModeDC = get_child_node(node, "linkModeDC")
    linkModeData = get_child_node(node, "linkModeData")
    linkModeSynchronization = get_child_node(node, "linkModeSynchronization")
    linkSpeed = get_child_node(node, "linkSpeed")
    operationalState = get_child_node(node, "operationalState")
    secondEndpointDN = get_child_node(node, "secondEndpointDN")
    secondEndpointLabel = get_child_node(node, "secondEndpointLabel")
    secondEndpointPortId = get_child_node(node, "secondEndpointPortId")

    NODE_LIST[checkbox_name.index("CABLINK_R")].append(
        [class1, EnodeBID, version, disName, cablinkType,configDN,firstEndpointDN,firstEndpointLabel,firstEndpointPortId,iqCompression,linkMaxPhysicalCapacity,linkModeConfiguration,linkModeDC,linkModeData,linkModeSynchronization,linkSpeed,operationalState,secondEndpointDN,secondEndpointLabel,secondEndpointPortId])
