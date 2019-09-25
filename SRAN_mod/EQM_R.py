from public_fuction_lij import *
from checkbox_name import *

def SMOD_R(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]
    EQM_R = spliter_M(distName, 2, "EQM_R-")
    APEQM_R = spliter_M(distName, 3, "APEQM_R-")
    CABINET_R = spliter_M(distName, 4, "CABINET_R-")
    SMOD_R = spliter_M(distName, 5, "SMOD_R-")
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
    NODE_LIST[checkbox_name.index("SMOD_R")].append([class1,EnodeBID,version,distName,configDN,eutraSupport,
                          function,geranSupport,horizontalPosition,operationalState,productCode,productName,
                          utranSupport,verticalPosition,serialNumber,EQM_R,APEQM_R,CABINET_R,SMOD_R])

def BBMOD_R(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
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
    NODE_LIST[checkbox_name.index("BBMOD_R")].append([class1, EnodeBID, version, distName, configDN, eutraSupport, function, geranSupport,
                          horizontalPosition, operationalState, productCode, productName, utranSupport,
                          verticalPosition, serialNumber])

def RMOD_R(node, NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]
    EQM_R = spliter_M(distName, 2, "EQM_R-")
    APEQM_R = spliter_M(distName, 3, "APEQM_R-")
    RMOD_R = spliter_M(distName, 4, "RMOD_R-")
    # id = node.attrib["id"]

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
        [class1, EnodeBID, version, distName, aldManagementProtocol, antennaPathDelayMeasurementCapable,
         blocking, configDN, hwVersion, operationalState, productCode, productName, radioMasterDN,
         radioModuleHwReleaseCode, rfmTransmitModeStatus, serialNumber,EQM_R,APEQM_R,RMOD_R])

def GNSSE_R(node,NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]

    gnssAntennaAltitude = get_child_node(node, "gnssAntennaAltitude")
    gnssAntennaLatitude = get_child_node(node, "gnssAntennaLatitude")
    gnssAntennaLongitude = get_child_node(node, "gnssAntennaLongitude")
    gnssConstellationMode = get_child_node(node, "gnssConstellationMode")
    gnssUnitName = get_child_node(node, "gnssUnitName")

    # 写入列表
    NODE_LIST[checkbox_name.index("GNSSE_R")].append([class1, EnodeBID, version, distName, gnssAntennaAltitude, gnssAntennaLatitude,
                         gnssAntennaLongitude, gnssConstellationMode, gnssUnitName])

def ANTL_R(node,NODE_LIST):
    class1 = node.attrib["class"]
    distName = node.attrib["distName"]
    EnodeBID = spliter_M(distName, 1, "MRBTS-")
    version = node.attrib["version"]
    EQM_R = spliter_M(distName, 2, "EQM_R-")
    APEQM_R = spliter_M(distName, 3, "APEQM_R-")
    RMOD_R = spliter_M(distName, 4, "RMOD_R-")
    ANTL_R = spliter_M(distName, 5, "ANTL_R-")

    antennaPathDelayDL = get_child_node(node, "antennaPathDelayDL")
    antennaPathDelayUL = get_child_node(node, "antennaPathDelayUL")
    antennaPathDelayValuesUsed = get_child_node(node, "antennaPathDelayValuesUsed")
    calcFEG = get_child_node(node, "calcFEG")
    configDN = get_child_node(node, "configDN")
    dcVoltage = get_child_node(node, "dcVoltage")
    hdlcCommunicationAllowed = get_child_node(node, "hdlcCommunicationAllowed")
    maxMCPApower = get_child_node(node, "maxMCPApower")
    rxCapable = get_child_node(node, "rxCapable")
    ulDelay = get_child_node(node, "ulDelay")
    vswrMajorThreshold = get_child_node(node, "vswrMajorThreshold")
    vswrMinorThreshold = get_child_node(node, "vswrMinorThreshold")

    # 写入列表
    NODE_LIST[checkbox_name.index("ANTL_R")].append([class1, EnodeBID, version, distName, antennaPathDelayDL, antennaPathDelayUL,
                         antennaPathDelayValuesUsed, calcFEG, configDN,dcVoltage,hdlcCommunicationAllowed,
                         maxMCPApower,rxCapable,ulDelay,vswrMajorThreshold,vswrMinorThreshold,EQM_R,APEQM_R,RMOD_R,
                         ANTL_R])