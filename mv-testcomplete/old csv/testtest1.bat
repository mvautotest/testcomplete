@echo off
python ClickMe.py > output.txt
::set "File2Read=output.txt"
::if not Exist "File2Read" (goto :Error)
setlocal EnableExtensions EnableDelayedExpansion
::set /p var =< output
@FOR /f "delims=" %%a in ('type AUTList.csv') DO (
	set /a count+=1
	set "Line[!count!]"=%%a"
)
for /L %%i in (l, l, %Count%%) do (
	echo %Count%
	if %Count%==0 goto :labela
	if %Count%==1 goto :labelb
	if %Count%==2 goto :labelc
	

	goto :labelc
	:labela
	start "test" /wait TestComplete.exe "..\mv-testcomplete\Emulator1\Emulator1.pjs" /run /el:"testlog\log.html" /e /SilentMode
	exit /b 0
	:labelb
	start "test" /wait TestComplete.exe "..\mv-testcomplete\Emulator1\Emulator1.pjs" /p:!Line[count]! /run /el:"testlog\log.html" /e /SilentMode
	exit /c 0
	:labelc
	start "test" /wait TestComplete.exe "..\mv-testcomplete\Emulator1\Emulator1.pjs" /p:AdvOCR /t:"Script|!Line[count]!|!Line[count]!" /run /el:"testlog\log.html" /e /SilentMode
	
)
::Error
::echo the file "%File2Read%" does not exist
::exit /b
::pause
::if %var% == Run_project_Suite goto :labela
::if not %var% == Run_project_Suite goto :labelb
::setlocal EnableDelayedExpansion

