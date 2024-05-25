
REM Check if Python is installed
python --version > nul 2>&1
if %errorlevel% neq 0 (
    REM Check if Chocolatey is installed
    choco -? >nul 2>&1
    if errorlevel 1 (
        @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
        echo Chocolatey installation completed.
        choco install python -Y
    ) else (
        echo Chocolatey is already installed.
        choco install python -Y
    )
)
%userprofile%\tab.pdf

@pause