import win32com.client
import sys,time
from PyQt5 import QtWidgets

#处理disName
def spliter_M(distName,NUM,ID):
    distName = str(distName)
    distName = distName.split('/')[NUM]
    distName = distName.replace(ID, '')
    return distName

def spliter_N(distName,NUM):
    distName = str(distName)
    distName = distName.split('-')[NUM]
    return distName

def get_child_node(node,node_children_name):
    for node_children in node:
        if node_children.attrib["name"] == node_children_name:
            node_children_name = node_children.text
            return node_children_name
            break

def get_child_node2(node,node_children_name):
    for node_children in node:
        if node_children.attrib["name"] == node_children_name:
            if len(node_children)>0:
                for node_children2 in node_children:
                    # print(node_children2.text)
                    return node_children2.text
        break


#写入数据到access
def update_access(list_my,conn,Table_name,self):
    rs_my = win32com.client.Dispatch(r'ADODB.Recordset')
    rs_my.Open(Table_name, conn, 1, 3)

    # print("读取"+Table_name+"...")
    self.textBrowser.append("读取"+Table_name+"...")
    QtWidgets.QApplication.processEvents()
    num = 0
    for i in list_my:
        y = 0
        rs_my.AddNew()  # 添加一条新记录
        for j in i:
            rs_my.Fields.Item(y).Value = j
            y +=1
        rs_my.Update()  # 更新
        QtWidgets.QApplication.processEvents()
        num += 1
    # print("读取" , Table_name , "完成，共导入：" , num , "条数据\n")
    self.textBrowser.append("读取" + Table_name + "完成，共导入：" + str(num) + "条数据\n")


