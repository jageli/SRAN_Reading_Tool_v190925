# SRAN_Reading_Tool
SRAN Reading Tool使用手册
前言
目前此工具可读取的内容还不是很完善，只选取了基站配置的XML文件中部分class以及class下的参数信息进行读取，如需增加可读取的表的内容可联系进行添加。


一、界面介绍：
1、	工具包含的程序和文件夹:
 
2、	点击SRAN Reading Tool.exe，打开应用的界面如下：
 
打开后的应用所有的选项卡对应的可勾选按钮默认处于已勾选状态，如果要选取某部分按钮，可以点击SELECT_ALL取消所有勾选再进行选取所需的内容
3、	上图可对应的选项卡分别对应网管CM Operations Manager上5G/LTE/SRAN下的9个分支内容，打开的顺序如下图：
 
 
 
4、	每个选项卡中可勾选的内容为基站xml配置对应的Class Name，如下图的MRBTS
 


二、Access数据库中每张表的包含的内容
1、	数据库中的分组分别代表了工具里的9个选项卡：
 
 



2、	每个分组下面的数据表分别对应了工具选项卡内可勾选按钮的内容：
      

3、	每张表的内容为基站XML下的对应CLASS内容，以MRBTS表为例：
 
 
Class为managedObject这行的class=“”引号中的字段，EnodeBID为distName=””中MRBTS-后面的ID，version为version=“”引号中的字段，distName为distName=“”引号中的字段，数据库所有表头的class，EnodeBID，version，distName获取的字段都是一样的。除去name1这种受access限制导致的无法命名为name外，其余的表头和子节点的内容是保持一致的（例：表头altitude和XML里的name=”altitude”是对应的）。

		
    4、有些表，工具自定义了一部分从class截取的部分字段用来补充了部分信息方便个人使用，即数据库表头的名称在XML的配置不存在就是自定义的表头信息。
