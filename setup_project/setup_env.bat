python -m venv ..\venv
..\venv\Scripts\pip install -r requirements.txt
pause
IF %ERRORLEVEL% NEQ 0 exit 1