@echo Start build process
@echo Remove previous folders
cd ..
rd /s /q build
rd /s /q dist\KivyTimer
.\venv\Scripts\pyinstaller -n KivyTimer --onefile --clean -y --noconsole main.py --paths "%CD%" --contents-directory . 
pause
IF %ERRORLEVEL% NEQ 0 exit 1
@echo Build completed successfully