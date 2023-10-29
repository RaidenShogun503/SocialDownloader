@echo off
title INSTALLER
echo   ####    ##  ##    ####    ######     ##     ##       ##        ####    ##  ##    #### 
echo    ##     ### ##   ##  ##     ##      ####    ##       ##         ##     ### ##   ##  ## 
echo    ##     ######   ##         ##     ##  ##   ##       ##         ##     ######   ##      
echo    ##     ######    ####      ##     ######   ##       ##         ##     ######   ## ###  
echo    ##     ## ###       ##     ##     ##  ##   ##       ##         ##     ## ###   ##  ##    
echo    ##     ##  ##   ##  ##     ##     ##  ##   ##       ##         ##     ##  ##   ##  ##
echo   ####    ##  ##    ####      ##     ##  ##   ######   ######    ####    ##  ##    ####   
winget install --id=Python.Python.3.11 -e 
winget install --id=Git.Git -e 
curl -o run.bat https://raw.githubusercontent.com/RaidenShogun503/SocialDownloader/main/run.bat
git clone https://github.com/RaidenShogun503/SocialDownloader
cd SocialDownloader
pip install -r requirements.txt
echo  ####      ####    ##  ##   ######  
echo ## ##    ##  ##   ### ##   ##      
echo ##  ##   ##  ##   ######   ##      
echo ##  ##   ##  ##   ######   ####    
echo ##  ##   ##  ##   ## ###   ##      
echo ## ##    ##  ##   ##  ##   ##      
echo ####      ####    ##  ##   ######  
py main.py