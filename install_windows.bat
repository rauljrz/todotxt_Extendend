@echo off
setlocal enabledelayedexpansion

:: Obtener el directorio home del usuario
set "HOME_DIR=%USERPROFILE%"

:: Verificar si existe el archivo .todo
set "TODO_CONFIG=%HOME_DIR%\.todo"
if not exist "%TODO_CONFIG%" (
    echo Creando archivo .todo...
    
    :: Crear la carpeta Life si no existe
    set "LIFE_DIR=%HOME_DIR%\Life"
    if not exist "%LIFE_DIR%" mkdir "%LIFE_DIR%"
    
    :: Crear la carpeta Inbox dentro de Life si no existe
    set "INBOX_DIR=%LIFE_DIR%\Inbox"
    if not exist "%INBOX_DIR%" mkdir "%INBOX_DIR%"
    
    :: Crear el archivo .todo con las entradas correspondientes
    (
        echo TODO_FILE = %LIFE_DIR%\todo.txt
        echo DONE_FILE = %LIFE_DIR%\done.txt
        echo HELP_FILE = %INBOX_DIR%\todohelp.txt
    ) > "%TODO_CONFIG%"
    echo Archivo .todo creado con éxito.
) else (
    echo El archivo .todo ya existe.
)

:: Crear la carpeta bin en el home si no existe
set "BIN_DIR=%HOME_DIR%\bin"
if not exist "%BIN_DIR%" (
    echo Creando carpeta bin en el home...
    mkdir "%BIN_DIR%"
)

:: Copiar archivos a la carpeta bin
echo Copiando archivos a la carpeta bin...
copy todo.py "%BIN_DIR%\"
copy todohelp_es.txt "%BIN_DIR%\"
copy todohelp.txt "%BIN_DIR%\"

:: Crear un archivo batch para el alias 't'
set "ALIAS_FILE=%BIN_DIR%\t.bat"
echo @echo off > "%ALIAS_FILE%"
echo python "%BIN_DIR%\todo.py" %%* >> "%ALIAS_FILE%"
echo Alias 't' creado como %ALIAS_FILE%

:: Agregar la carpeta bin al PATH si no está ya
echo Actualizando la variable PATH...
set "PATH_TO_ADD=%BIN_DIR%"
for %%I in ("%PATH_TO_ADD%") do set "PATH_TO_ADD=%%~fI"
echo %PATH% | find /i "%PATH_TO_ADD%" > nul
if errorlevel 1 (
    setx PATH "%PATH%;%PATH_TO_ADD%"
    echo La carpeta bin ha sido añadida al PATH.
) else (
    echo La carpeta bin ya está en el PATH.
)

echo Instalación completada. Por favor, reinicia tu terminal para aplicar los cambios.
pause