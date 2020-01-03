@echo off
if exist "..\mv-testcomplete\testlog" (echo Y)
::del "..\mv-testcomplete\testlog" /a /s /q /f
::rmdir "../mv-testcomplete/testlog/testScriptMainExceltest"
rmdir "../mv-testcomplete/testlog/" /q *.* /s