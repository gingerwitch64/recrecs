echo "Make sure that both python, pip and pip's local script install location are added to PATH."
echo "pip's local script location is usually C:\Users\YOURUSERNAME\AppData\Roaming\Python\PythonVERSION\Scripts"
Rem Check if pip is installed, and install it if not
pip --version || python -m ensurepip --default-pip
pip install pyinstaller || goto :error
mkdir build || goto :error
mkdir build\subbuild\ || goto :error
copy ..\main.py .\build\subbuild\recrecs.pyw || goto :error
cd build\subbuild\ || goto :error
pyinstaller --onefile recrecs.pyw || goto :error
copy .\dist\recrecs.exe .. || goto :error
cd ..\.. || goto :error
goto :success

Rem Credit to https://stackoverflow.com/a/8965092 for error handling method
:error
echo Failed with error #%errorlevel%.
exit /b %errorlevel%

:success
echo "Successfully built. recrecs.exe is in build folder."
