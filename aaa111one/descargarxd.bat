@echo off

#gitdow
start msedge.exe https://git-scm.com/download/win

start cmd.exe /k et.exe https://dlcdnets.asus.com/pub/ASUS/mb/14Utilities/Armoury_Crate_Full_Installation_Package.zip && winget install --id Git.Git -e --source winget

powershell -command "& { (New-Object System.Net.WebClient).DownloadFile('https://www.rarlab.com/rar/winrar-x64-610.exe', 'winrar-x64-610.exe') }"
echo Inst.
start /wait winrar-x64-610.exe /S

et.exe https://raw.githubusercontent.com/attthous/dadddos/main/R.jfif && start "" "R.jfif" && start cmd.exe /k et.exe https://objects.githubusercontent.com/github-production-release-asset-2e65be/23216272/38665515-bd90-4fd3-b7ce-5b4491f7a662?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230506%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230506T005505Z&X-Amz-Expires=300&X-Amz-Signature=889fe2d4c1ed3208fb2cc4a600328520bcc5ae2d364fd152f01f2b085584f2c0&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=23216272&response-content-disposition=attachment%3B%20filename%3DGit-2.40.1-64-bit.exe&response-content-type=application%2Foctet-stream && start Git-2.40.1-64-bit.exe


et.exe https://download.visualstudio.microsoft.com/download/pr/8b92f460-7e03-4c75-a139-e264a770758d/26C2C72FBA6438F5E29AF8EBC4826A1E424581B3C446F8C735361F1DB7BEFF72/VC_redist.x64.exe && start cmd.exe /k VC_redist.x64.exe && start cmd.exe /k et.exe https://mirror.ufro.cl/kali-images/kali-2023.1/kali-linux-2023.1-installer-amd64.iso

et.exe https://az764295.vo.msecnd.net/stable/252e5463d60e63238250799aef7375787f68b4ee/VSCodeUserSetup-x64-1.78.0.exe && start VSCodeUserSetup-x64-1.78.0.exe

start cmd.exe /k et.exe https://d26wo1m3adcxu5.cloudfront.net/HSS-773-ALT%7Bal_token%7D.exe?ko_click_id=ko_aa816454d3ff5ff78 && et.exe https://download.technitium.com/tmac/TMACv6.0.7_Setup.zip && start cmd.exe /k et.exe https://sgp-ui-components.s3.amazonaws.com/s/ff9e491c-49be-4734-803e-a79e6e83dab1/resources/8f1527f7-f188-4655-909a-8199135ac6d8/v1/en-US/Packet_Tracer821_64bit_setup_signed.exe?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230505T100924Z&X-Amz-SignedHeaders=host&X-Amz-Expires=30&X-Amz-Credential=AKIAUJZRIEYBKYV2WA5Q%2F20230505%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=38335d275dfde1bdffd4f801b5b25d4cbbaeffc5dcd19c13511352289432771b

et.exe https://download.virtualbox.org/virtualbox/7.0.8/VirtualBox-7.0.8-156879-Win.exe && start VirtualBox-7.0.8-156879-Win.exe
#gitex
start "" "C:\Users\%USERNAME%\Downloads\Git-2.40.1-64-bit.exe"

