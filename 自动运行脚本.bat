@echo off
cd /d %~dp0
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit

title --python3 -- lijie --
MODE con: COLS=80 lines=30
color 1f
  
:begin  
@rem cls  
echo **********����ǰҪ�ȶ���python�İ�װĿ¼**************************
 
echo ���нű�....
echo.
@rem ���ݸ��˵��԰�װPythonĿ¼��ͬ�����޸�
C:\my\python\mypy37-32\readXML\venv\Scripts\python.exe main5.py

@echo �������н���
pause
goto end  

:end 
exit  