@echo off
chcp 65001 >nul
REM Сборка SiiVehicleTransfer.exe через PyInstaller (Windows)
python -m pip install -r requirements-dev.txt || goto :error
python -m PyInstaller --noconfirm --clean sii_vehicle_transfer.spec || goto :error
if exist SII_Decrypt.exe copy /Y SII_Decrypt.exe dist\SII_Decrypt.exe >nul
echo.
echo Готово: dist\SiiVehicleTransfer.exe
echo Положите SII_Decrypt.exe рядом с exe или укажите путь в настройках.
pause
exit /b 0
:error
echo Ошибка сборки.
pause
exit /b 1
