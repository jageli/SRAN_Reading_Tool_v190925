from public_fuction_lij import *
import win32com.client
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import (QMessageBox)
from checkbox_name import *

import TDD_mod.EQM
import TDD_mod.EQM_R
import TDD_mod.INVUNIT_R
import TDD_mod.LTE_BTS
import TDD_mod.MNL
import TDD_mod.MRBTS
import TDD_mod.SRAN_GNBTS
import TDD_mod.SRAN_HW
import TDD_mod.TNL

# import os
# import sys
# current_folder=os.getcwd()
# LIBFOLDER = current_folder + "\TDD_mod"
# sys.path.insert(0, LIBFOLDER)
# import EQM
# import EQM_R
# import INVUNIT_R
# import LTE_BTS
# import MNL
# import MRBTS
# import SRAN_GNBTS
# import SRAN_HW
# import TNL


# import res

# module= 'MRBTS'
# __import__('MRBTS')
# import MRBTS
# from MRBTS import *
# from HW import *
# from GNSSE_R import *
# from GNSSE_HW import *
# from GNBCF import *
# from GNCEL import *
# from GNCEL_R import *
# from LNBTS import *
# from LNCEL import *
# from LNCEL_FDD import *
# from NBIOT_FDD import *
# from VLANIF import *
# from IPADDRESSV4 import *
# from IPRT import *
# from MPLANENW import *
# from BBMOD_HW import *
# from SMOD_HW import *
# from RMOD_HW import *
# from BBMOD_R import *
# from SMOD_R import *
# from RMOD_R import *
# from LNMME import *
# from CHANNEL import *
# from CARRIERGROUPC_R import *
# from MNL_R import *
# from CHANNELGROUP import *
# from SECADM import *
# from FEATCADM import *
# from BBMOD_EQM import *
# from SMOD_EQM import *
# from RMOD_EQM import *
# from GNSSE_EQM import *

#清空access中的所有数据
def del_all(self,checkbox_name):
    # if win32api.MessageBox(0, "是否清空数据库？", "提示", win32con.MB_YESNO) == 6 :
    reply = QMessageBox.question(self, '提示',
                                 "是否清空数据库？", QMessageBox.Yes |
                                 QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
        self.textBrowser.append("开始清空数据库......")
        QtWidgets.QApplication.processEvents()
        conn = win32com.client.Dispatch(r"ADODB.Connection")
        DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = TDD.mdb'
        conn.Open(DSN)
        rs = win32com.client.Dispatch(r'ADODB.Recordset')

        for DatebaseName in checkbox_name:
            SQL = "Delete * FROM " + DatebaseName
            conn.Execute(SQL)
            QtWidgets.QApplication.processEvents()
        self.textBrowser.append("清空已完成！")


#清空access中的checkbox选中的数据
def del_rs(self,checkbox_state):
    # if win32api.MessageBox(0, "是否清空数据库？", "提示", win32con.MB_YESNO) == 6 :
    reply = QMessageBox.question(self, '提示',
                                 "是否清空数据库？", QMessageBox.Yes |
                                 QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
        conn = win32com.client.Dispatch(r"ADODB.Connection")
        DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = TDD.mdb'
        conn.Open(DSN)
        rs = win32com.client.Dispatch(r'ADODB.Recordset')
        for x in range(len(checkbox_state)):
            if checkbox_state[x] == 1:
                conn.Execute("Delete * FROM " + checkbox_name[x])
                QtWidgets.QApplication.processEvents()
        # if checkbox_state[0] == 1:
        #     conn.Execute("Delete * FROM MRBTS")



#用iterparse()函数迭代解析，可以读取超大型XML，大于1G
def read_XML_to_list(file, xmlns, NODE_LIST,checkbox_state):
    for event, Tree in ET.iterparse(file):
        if event == 'end':
            QtWidgets.QApplication.processEvents()
            if Tree.tag == (xmlns + 'managedObject'):
                managedObject_nodes = Tree.getiterator(xmlns + 'managedObject')
                for managedObject_node in managedObject_nodes:
                    read_node(managedObject_node, NODE_LIST,checkbox_state)
                Tree.clear()    #清除缓存

#读取节点及二级子节点
def read_node(node, NODE_LIST,checkbox_state):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # # # # # # # # # # # # # # # # # # # #

 # # # # # # # # # # # # # # MRBTS # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #读取MRBTS到list
    if node.attrib["class"] == "MRBTS" and checkbox_state[checkbox_name.index("MRBTS")] == 1:
        TDD_mod.MRBTS.MRBTS(node, NODE_LIST)

 # # # # # # # # # # # # # # EQM # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # 读取BBMOD_EQM到list
    if node.attrib["class"] == "BBMOD" and node.attrib["version"][:3] == "EQM" and checkbox_state[
        checkbox_name.index("BBMOD_EQM")] == 1:
        TDD_mod.EQM.BBMOD_EQM(node, NODE_LIST)

        # 读取SMOD_EQM到list
    if node.attrib["class"] == "SMOD" and node.attrib["version"][:3] == "EQM" and checkbox_state[
        checkbox_name.index("SMOD_EQM")] == 1:
        TDD_mod.EQM.SMOD_EQM(node, NODE_LIST)

        # 读取RMOD_EQM到list
    if node.attrib["class"] == "RMOD" and node.attrib["version"][:3] == "EQM" and checkbox_state[
        checkbox_name.index("RMOD_EQM")] == 1:
        TDD_mod.EQM.RMOD_EQM(node, NODE_LIST)

 # # # # # # # # # # # # # # EQM_R # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # 读取BBMOD_R到list
    if node.attrib["class"] == "BBMOD_R" and checkbox_state[checkbox_name.index("BBMOD_R")]== 1:
        TDD_mod.EQM_R.BBMOD_R(node, NODE_LIST)

    # 读取SMOD_R到list
    if node.attrib["class"] == "SMOD_R" and checkbox_state[checkbox_name.index("SMOD_R")]== 1:
        TDD_mod.EQM_R.SMOD_R(node, NODE_LIST)

    # 读取RMOD_R到list
    if node.attrib["class"] == "RMOD_R" and checkbox_state[checkbox_name.index("RMOD_R")] == 1:
        TDD_mod.EQM_R.RMOD_R(node, NODE_LIST)

    # 读取GNSSE_R到list
    if node.attrib["class"] == "GNSSE_R" and checkbox_state[checkbox_name.index("GNSSE_R")] == 1:
        TDD_mod.EQM_R.GNSSE_R(node, NODE_LIST)

    # 读取ANTL_R到list
    # if node.attrib["class"] == "ANTL_R" and checkbox_state[checkbox_name.index("ANTL_R")] == 1:
    #     EQM_R.ANTL_R(node, NODE_LIST)

    if node.attrib["class"] == "CABLINK_R" and checkbox_state[checkbox_name.index("CABLINK_R")]== 1:
        TDD_mod.EQM_R.CABLINK_R(node, NODE_LIST)

 # # # # # # # # # # # # # # INVUNIT_R # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # # # # # # # # # # # # # # LTE_BTS # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # 读取LNBTS到list
    if node.attrib["class"] == "LNBTS" and checkbox_state[checkbox_name.index("LNBTS")]== 1:
        TDD_mod.LTE_BTS.LNBTS(node, NODE_LIST)

    # 读取LNCEL到list
    if node.attrib["class"] == "LNCEL" and checkbox_state[checkbox_name.index("LNCEL")] == 1:
        TDD_mod.LTE_BTS.LNCEL(node, NODE_LIST)

    # 读取LNCEL_FDD到list
    if node.attrib["class"] == "LNCEL_FDD" and checkbox_state[checkbox_name.index("LNCEL_FDD")] == 1:
        TDD_mod.LTE_BTS.LNCEL_FDD(node, NODE_LIST)

    # 读取NBIOT_FDD到list
    if node.attrib["class"] == "NBIOT_FDD" and checkbox_state[checkbox_name.index("NBIOT_FDD")]== 1:
        TDD_mod.LTE_BTS.NBIOT_FDD(node, NODE_LIST)

    # 读取LNMME到list
    if node.attrib["class"] == "LNMME" and checkbox_state[checkbox_name.index("LNMME")]== 1:
        TDD_mod.LTE_BTS.LNMME(node, NODE_LIST)

 # # # # # # # # # # # # # # MNL # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # 读取GNSSE_MNL到list
    if node.attrib["class"] == "GNSSE" and node.attrib["version"][:3] == "MNL" and checkbox_state[
        checkbox_name.index("GNSSE_MNL")] == 1:
        TDD_mod.MNL.GNSSE_MNL(node, NODE_LIST)

    # 读取CHANNEL到list
    if node.attrib["class"] == "CHANNEL" and checkbox_state[checkbox_name.index("CHANNEL")] == 1:
        TDD_mod.MNL.CHANNEL(node, NODE_LIST)

    # 读取CHANNELGROUP到list
    if node.attrib["class"] == "CHANNELGROUP" and checkbox_state[checkbox_name.index("CHANNELGROUP")] == 1:
        TDD_mod.MNL.CHANNELGROUP(node, NODE_LIST)

    # 读取SECADM到list
    if node.attrib["class"] == "SECADM" and checkbox_state[checkbox_name.index("SECADM")]== 1:
        TDD_mod.MNL.SECADM(node, NODE_LIST)

    # 读取FEATCADM到list
    if node.attrib["class"] == "FEATCADM" and checkbox_state[checkbox_name.index("FEATCADM")] == 1:
        TDD_mod.MNL.FEATCADM(node, NODE_LIST)

    # 读取MPLANENW到list
    if node.attrib["class"] == "MPLANENW" and checkbox_state[checkbox_name.index("MPLANENW")] == 1:
        TDD_mod.MNL.MPLANENW(node, NODE_LIST)

    # 读取MNL_R到list
    if node.attrib["class"] == "MNL_R" and checkbox_state[checkbox_name.index("MNL_R")] == 1:
        TDD_mod.MNL.MNL_R(node, NODE_LIST)

    # 读取TIME到list
    # if node.attrib["class"] == "TIME" and checkbox_state[checkbox_name.index("TIME1")] == 1:
    #     MNL.TIME1(node, NODE_LIST)
 # # # # # # # # # # # # # # SRAN_GNBTS # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # 读取GNBCF到list
    if node.attrib["class"] == "GNBCF" and checkbox_state[checkbox_name.index("GNBCF")] == 1:
        TDD_mod.SRAN_GNBTS.GNBCF(node, NODE_LIST)

    # 读取GNCEL到list
    if node.attrib["class"] == "GNCEL" and checkbox_state[checkbox_name.index("GNCEL")] == 1:
        TDD_mod.SRAN_GNBTS.GNCEL(node, NODE_LIST)

    # 读取GNCEL_R到list
    if node.attrib["class"] == "GNCEL_R" and checkbox_state[checkbox_name.index("GNCEL_R")] == 1:
        TDD_mod.SRAN_GNBTS.GNCEL_R(node, NODE_LIST)

    # 读取CARRIERGROUPC_R到list
    if node.attrib["class"] == "CARRIERGROUPC_R" and checkbox_state[checkbox_name.index("CARRIERGROUPC_R")] == 1:
        TDD_mod.SRAN_GNBTS.CARRIERGROUPC_R(node, NODE_LIST)

 # # # # # # # # # # # # # # SRAN_HW # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # 读取GNSSE_HW到list
    if node.attrib["class"] == "GNSSE" and node.attrib["version"][:2] == "HW" and checkbox_state[
        checkbox_name.index("GNSSE_HW")]== 1:
        TDD_mod.SRAN_HW.GNSSE_HW(node, NODE_LIST)

    # 读取BBMOD_HW到list
    if node.attrib["class"] == "BBMOD" and node.attrib["version"][:2] == "HW" and checkbox_state[
        checkbox_name.index("BBMOD_HW")] == 1:
        TDD_mod.SRAN_HW.BBMOD_HW(node, NODE_LIST)

    # 读取SMOD_HW到list
    if node.attrib["class"] == "SMOD"and node.attrib["version"][:2] == "HW" and checkbox_state[
        checkbox_name.index("SMOD_HW")] == 1:
        TDD_mod.SRAN_HW.SMOD_HW(node, NODE_LIST)

    # 读取RMOD_HW到list
    if node.attrib["class"] == "RMOD" and node.attrib["version"][:2] == "HW"and checkbox_state[
        checkbox_name.index("RMOD_HW")] == 1:
        TDD_mod.SRAN_HW.RMOD_HW(node, NODE_LIST)

    # 读取HW到list
    if node.attrib["class"] == "HW" and checkbox_state[checkbox_name.index("HW")] == 1:
        TDD_mod.SRAN_HW.HW(node, NODE_LIST)

 # # # # # # # # # # # # # # TNL # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # 读取VLANIF到list
    if node.attrib["class"] == "VLANIF" and checkbox_state[checkbox_name.index("VLANIF")] == 1:
        TDD_mod.TNL.VLANIF(node, NODE_LIST)

    # 读取IPADDRESSV4到list
    if node.attrib["class"] == "IPADDRESSV4" and checkbox_state[checkbox_name.index("IPADDRESSV4")] == 1:
        TDD_mod.TNL.IPADDRESSV4(node, NODE_LIST)

    # 读取IPRT到list
    if node.attrib["class"] == "IPRT" and checkbox_state[checkbox_name.index("IPRT")] == 1:
       TDD_mod.TNL.IPRT(node, NODE_LIST)


# # # # # # # # # # # # # # GSM # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # 读取UNIT到list
    # if node.attrib["class"] == "UNIT" and checkbox_state[checkbox_name.index("UNIT")] == 1:
    #     GSM_18A.UNIT(node, NODE_LIST)
    # 读取GSM_HW到list
    # if node.attrib["class"] == "HW" and checkbox_state[checkbox_name.index("HW_GSM")] == 1:
    #     GSM_18A.HW_GSM(node, NODE_LIST)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # # # # # # # # # # # # # # # #
#插入数据到access
def read_list_to_access(NODE_LIST,self):
    conn = win32com.client.Dispatch(r"ADODB.Connection")
    DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = TDD.mdb'
    # DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = Database1.mdb'
    conn.Open(DSN)
    for rs_name in checkbox_name:
        if len(NODE_LIST[checkbox_name.index(rs_name)]) != 0:
            update_access(NODE_LIST[checkbox_name.index(rs_name)], conn, rs_name, self)
            NODE_LIST[checkbox_name.index(rs_name)].clear()

    # if len(NODE_LIST[0])!=0:
    #     update_access(NODE_LIST[0], conn, "MRBTS",self); NODE_LIST[0].clear()
    # if len(NODE_LIST[checkbox_name.index("HW")]) != 0:
    #     update_access(NODE_LIST[checkbox_name.index("HW")], conn, "HW",self); NODE_LIST[checkbox_name.index("HW")].clear()
    # if len(NODE_LIST[2]) != 0:
    #     update_access(NODE_LIST[2], conn, "GNSSE_R",self); NODE_LIST[2].clear()
    # if len(NODE_LIST[3]) != 0:
    #     update_access(NODE_LIST[3], conn, "GNSSE_HW",self); NODE_LIST[3].clear()
    # if len(NODE_LIST[4]) != 0:
    #     update_access(NODE_LIST[4], conn, "GNBCF",self); NODE_LIST[4].clear()
    # if len(NODE_LIST[5]) != 0:
    #     update_access(NODE_LIST[5], conn, "GNCEL",self); NODE_LIST[5].clear()
    # if len(NODE_LIST[6]) != 0:
    #     update_access(NODE_LIST[6], conn, "GNCEL_R",self); NODE_LIST[6].clear()
    # if len(NODE_LIST[7]) != 0:
    #     update_access(NODE_LIST[7], conn, "LNBTS",self); NODE_LIST[7].clear()
    # if len(NODE_LIST[8]) != 0:
    #     update_access(NODE_LIST[8], conn, "LNCEL",self); NODE_LIST[8].clear()
    # if len(NODE_LIST[9]) != 0:
    #     update_access(NODE_LIST[9], conn, "LNCEL_FDD",self); NODE_LIST[9].clear()
    # if len(NODE_LIST[10]) != 0:
    #     update_access(NODE_LIST[10], conn, "NBIOT_FDD",self); NODE_LIST[10].clear()
    # if len(NODE_LIST[11]) != 0:
    #     update_access(NODE_LIST[11], conn, "VLANIF",self); NODE_LIST[11].clear()
    # if len(NODE_LIST[12]) != 0:
    #     update_access(NODE_LIST[12], conn, "IPADDRESSV4",self); NODE_LIST[12].clear()
    # if len(NODE_LIST[13]) != 0:
    #     update_access(NODE_LIST[13], conn, "IPRT",self); NODE_LIST[13].clear()
    # if len(NODE_LIST[14]) != 0:
    #     update_access(NODE_LIST[14], conn, "MPLANENW",self); NODE_LIST[14].clear()
    # if len(NODE_LIST[15]) != 0:
    #     update_access(NODE_LIST[15], conn, "BBMOD_HW",self); NODE_LIST[15].clear()
    # if len(NODE_LIST[16]) != 0:
    #     update_access(NODE_LIST[16], conn, "SMOD_HW",self); NODE_LIST[16].clear()
    # if len(NODE_LIST[17]) != 0:
    #     update_access(NODE_LIST[17], conn, "RMOD_HW",self); NODE_LIST[17].clear()
    # if len(NODE_LIST[18]) != 0:
    #     update_access(NODE_LIST[18], conn, "BBMOD_R",self); NODE_LIST[18].clear()
    # if len(NODE_LIST[19]) != 0:
    #     update_access(NODE_LIST[19], conn, "SMOD_R",self); NODE_LIST[19].clear()
    # if len(NODE_LIST[20]) != 0:
    #     update_access(NODE_LIST[20], conn, "RMOD_R",self); NODE_LIST[20].clear()
    # if len(NODE_LIST[21]) != 0:
    #     update_access(NODE_LIST[21], conn, "LNMME",self); NODE_LIST[21].clear()
    # if len(NODE_LIST[22]) != 0:
    #      update_access(NODE_LIST[22], conn, "CHANNEL",self); NODE_LIST[22].clear()
    # if len(NODE_LIST[23]) != 0:
    #     update_access(NODE_LIST[23], conn, "CARRIERGROUPC_R",self); NODE_LIST[23].clear()
    # if len(NODE_LIST[24]) != 0:
    #     update_access(NODE_LIST[24], conn, "MNL_R",self); NODE_LIST[24].clear()
    # if len(NODE_LIST[25]) != 0:
    #     update_access(NODE_LIST[25], conn, "CHANNELGROUP",self); NODE_LIST[25].clear()
    # if len(NODE_LIST[26]) != 0:
    #     update_access(NODE_LIST[26], conn, "SECADM",self);NODE_LIST[26].clear()
    # if len(NODE_LIST[27]) != 0:
    #     update_access(NODE_LIST[27], conn, "FEATCADM",self);NODE_LIST[27].clear()
    # if len(NODE_LIST[28]) != 0:
    #     update_access(NODE_LIST[28], conn, "BBMOD_EQM",self); NODE_LIST[28].clear()
    # if len(NODE_LIST[29]) != 0:
    #     update_access(NODE_LIST[29], conn, "SMOD_EQM",self); NODE_LIST[29].clear()
    # if len(NODE_LIST[30]) != 0:
    #     update_access(NODE_LIST[30], conn, "RMOD_EQM",self); NODE_LIST[30].clear()
    # if len(NODE_LIST[31]) != 0:
    #     update_access(NODE_LIST[31], conn, "GNSSE_EQM",self); NODE_LIST[31].clear()