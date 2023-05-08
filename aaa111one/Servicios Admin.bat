@echo off

echo Deteniendo el servicio de Fax...
net stop fax

echo Deshabilitando el servicio de Fax...
sc config fax start= disabled

echo Deteniendo el servicio de Telefonía...
net stop TapiSrv

echo Deshabilitando el servicio de Telefonía...
sc config TapiSrv start= disabled

echo Deteniendo el servicio de Administrador de cuentas de Xbox Live...
net stop XboxLiveAuthManager

echo Deshabilitando el servicio de Administrador de cuentas de Xbox Live...
sc config XboxLiveAuthManager start= disabled

echo Deteniendo el servicio de Autenticación de Xbox Live...
net stop XboxNetApiSvc

echo Deshabilitando el servicio de Autenticación de Xbox Live...
sc config XboxNetApiSvc start= disabled

echo Deteniendo el servicio de Servicio de red de Xbox Live...
net stop XboxNetApiSvc

echo Deshabilitando el servicio de Servicio de red de Xbox Live...
sc config XboxNetApiSvc start= disabled

echo Deteniendo el servicio de Administración de mapas...
net stop MapsBroker

echo Deshabilitando el servicio de Administración de mapas...
sc config MapsBroker start= disabled

echo Deteniendo el servicio de Control parental...
net stop WPCSvc

echo Deshabilitando el servicio de Control parental...
sc config WPCSvc start= disabled

echo Deteniendo el servicio de Cola de impresión...
net stop Spooler

echo Deshabilitando el servicio de Cola de impresión...
sc config Spooler start= disabled

echo Deteniendo el servicio de Experiencia de usuario y telemetría asociadas...
net stop DiagTrack

echo Deshabilitando el servicio de Experiencia de usuario y telemetría asociadas...
sc config DiagTrack start= disabled

echo Deteniendo el servicio de Servicio de enrutamiento de mensaje de inserción de protocolo de aplicación inalámbrica (WAP) de administración de dispositivos...
net stop wapsvc

echo Deshabilitando el servicio de Servicio de enrutamiento de mensaje de inserción de protocolo de aplicación inalámbrica (WAP) de administración de dispositivos...
sc config wapsvc start= disabled

echo Deteniendo el servicio de Registro remoto...
net stop RemoteRegistry

echo Deshabilitando el servicio de Registro remoto...
sc config RemoteRegistry start= disabled

echo Deteniendo el servicio de Panel de escritura a mano y teclado táctil...
net stop TabletInputService

echo Deshabilitando el servicio de Panel de escritura a mano y teclado táctil...
sc config TabletInputService start= disabled

echo Deteniendo el servicio de Servicio biométrico de Windows...
net stop WbioSrvc

echo Deshabilitando el servicio de Servicio biométrico de Windows...
sc config WbioSrvc start= disabled

echo Deteniendo el servicio de Windows Insider...
net stop WaaSMedicSvc

echo Deshabilitando el servicio de Windows Insider...
sc config WaaSMedicSvc start= disabled

echo Deteniendo el servicio de Servicio Frameserver de la cámara de Windows...
net stop FrameServer

echo Deshabilitando el servicio de Servicio Frameserver de la cámara de Windows...
sc config FrameServer start= disabled

echo Deteniendo el servicio de Windows Search...
net stop WSearch

echo Deshabilitando el servicio de Windows Search...
sc config WSearch start= disabled

echo Deteniendo todos los servicios relacionados con Xbox...
net stop XblAuthManager
net stop XblGameSave
net stop XblGpuDrv
net stop XboxGipSvc
net stop XboxNetApiSvc
net stop XboxPvrSvc

echo Deshabilitando todos los servicios relacionados con Xbox...
sc config XblAuthManager start= disabled
sc config XblGameSave start= disabled
sc config XblGpuDrv start= disabled
sc config XboxGipSvc start= disabled
sc config XboxNetApiSvc start= disabled
sc config XboxPvrSvc start= disabled

echo Todos los servicios han sido detenidos y deshabilitados.
pause




