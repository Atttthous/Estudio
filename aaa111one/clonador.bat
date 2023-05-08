@echo off

set "REPO_URL_1=https://github.com/Atttthous/repositorio.git"
set "REPO_URL_2=https://github.com/Atttthous/Estudio.git"
set "REPO_URL_3=https://github.com/Atttthous/sh.git"
set "DEST_PATH=C:\users\%USERNAME%\Documents"

echo Clonando %REPO_URL_1% en %DEST_PATH%...
git clone %REPO_URL_1% %DEST_PATH%\repositorio

echo Clonando %REPO_URL_2% en %DEST_PATH%...
git clone %REPO_URL_2% %DEST_PATH%\Estudio

echo Clonando %REPO_URL_3% en %DEST_PATH%...
git clone %REPO_URL_3% %DEST_PATH%\sh

echo Clonado completado.