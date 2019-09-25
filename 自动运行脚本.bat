@echo off
cd /d %~dp0
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit

title --python3 -- lijie --
MODE con: COLS=80 lines=30
color 1f
  
:begin  
@rem cls  
echo **********运行前要先定义python的安装目录**************************
 
echo 运行脚本....
echo.
@rem 根据个人电脑安装Python目录不同进行修改
C:\my\python\mypy37-32\readXML\venv\Scripts\python.exe main5.py

@echo 程序运行结束
pause
goto end  

:end 
exit  