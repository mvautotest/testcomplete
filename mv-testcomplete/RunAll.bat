@echo off
::if exist "..\mv-testcomplete\testlog" (echo Y)
::del "..\mv-testcomplete\testlog" /Q


::set /p var =< output
@FOR /f "delims=" %%i in ('type TestSet.txt') DO set var=%%i

echo %var%
::pause
if %var% == Run_project_Suite goto :labela
if not %var% == Run_project_Suite goto :labelb
::setlocal EnableDelayedExpansion
::set str = %var%
::call :strLen str strlen
::echo String is %strlen% characters long

::if %strlen% > 20 goto :labelc
set AdvOCR = %var1%
set AdvOCR_Train_002 = %var2%
echo %var1%%
echo %var2%%
::if %var% ==AdvOCR_AdvOCR_Train_002 goto :labelc
:labela
start "test" /wait TestComplete.exe "..\mv-testcomplete\Emulator1\Emulator1.pjs" /run /el:"testlog\log.html" /e /SilentMode
exit /b 0
:labelb
start "test" /wait TestComplete.exe "..\mv-testcomplete\Emulator1\Emulator1.pjs" /p:%var% /run /el:"testlog\log.html" /e /SilentMode
exit /c 0
:labelc
start "test" /wait TestComplete.exe "..\mv-testcomplete\Emulator1\Emulator1.pjs" /p:%var1% /t:"Script|%var2%|%var2%" /run /el:"testlog\log.html" /e /SilentMode

::labeld
::start "test" /wait TestComplete.exe "..\mv-testcomplete\Emulator1\Emulator1.pjs" /p:PinpointPatternFind /run /el:"testlog\log.html" /e /SilentMode

::start "test" /wait TestComplete.exe "..\mv-testcomplete\Emulator1\Emulator1.pjs" ::/p:%var1% /t:"Script|%var2%|%var2%" /run /el:"testlog\log.html" /e /SilentMode


::del output.txt

::/p:AdvOCR /t:"Script|AdvOCR_Train_002|AdvOCR_Train_002"