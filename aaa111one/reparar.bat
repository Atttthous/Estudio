@echo off
DISM /Online /Cleanup-Image /CheckHealth
start cmd.exe /k start mrt && start cmd.exe /k powershell start winget upgrade
sfc /scannow
