@if (@a==@b) @end /*

@echo off
setlocal

:: Ejecuta el script JScript embebido y almacena el resultado en la variable FLDR
for /f "delims=" %%I in ('cscript /nologo /e:jscript "%~f0"') do (
    set FLDR=%%I
)
:: Si FLDR está vacío, el script termina
if "%FLDR%"=="" (exit)

:: Elimina los directorios de idioma español (latinoamérica) si existen
rd /q /s "%FLDR%\Data\Core\Languages\SpanishLatin (Español (Latinoamérica))"
rd /q /s "%FLDR%\Data\Royalty\Languages\SpanishLatin (Español (Latinoamérica))"
rd /q /s "%FLDR%\Data\Ideology\Languages\SpanishLatin (Español (Latinoamérica))"
rd /q /s "%FLDR%\Data\Biotech\Languages\SpanishLatin (Español (Latinoamérica))"
rd /q /s "%FLDR%\Data\Anomaly\Languages\SpanishLatin (Español (Latinoamérica))"

:: Descargar traducciones desde GitHub
curl -L -o SpanishLatin.zip https://github.com/Ludeon/RimWorld-SpanishLatin/archive/refs/heads/master.zip

:: Crear una carpeta temporal para la descompresión
md temp

:: Descomprimir el archivo descargado en la carpeta temporal
tar -xf SpanishLatin.zip -C temp

:: Mover los archivos descomprimidos a las ubicaciones correspondientes
xcopy /s /i "temp/RimWorld-SpanishLatin-master/Core" "%FLDR%\Data\Core\Languages\SpanishLatin (Español (Latinoamérica))"
xcopy /s /i "temp/RimWorld-SpanishLatin-master/Royalty" "%FLDR%\Data\Royalty\Languages\SpanishLatin (Español (Latinoamérica))"
xcopy /s /i "temp/RimWorld-SpanishLatin-master/Ideology" "%FLDR%\Data\Ideology\Languages\SpanishLatin (Español (Latinoamérica))"
xcopy /s /i "temp/RimWorld-SpanishLatin-master/Biotech" "%FLDR%\Data\Biotech\Languages\SpanishLatin (Español (Latinoamérica))"
xcopy /s /i "temp/RimWorld-SpanishLatin-master/Anomaly" "%FLDR%\Data\Anomaly\Languages\SpanishLatin (Español (Latinoamérica))"

:: Eliminar los archivos temporales y el archivo zip descargado
rd /q /s temp
del SpanishLatin.zip

:: Eliminar los archivos .tar si existen
del "%FLDR%\Data\Core\Languages\SpanishLatin (Español (Latinoamérica)).tar"
del "%FLDR%\Data\Royalty\Languages\SpanishLatin (Español (Latinoamérica)).tar"
del "%FLDR%\Data\Ideology\Languages\SpanishLatin (Español (Latinoamérica)).tar"
del "%FLDR%\Data\Biotech\Languages\SpanishLatin (Español (Latinoamérica)).tar"
del "%FLDR%\Data\Anomaly\Languages\SpanishLatin (Español (Latinoamérica)).tar"

goto :EOF

:: Parte JScript */

var shl = new ActiveXObject("Shell.Application");
var folder = shl.BrowseForFolder(0, "Selecciona la carpeta de RimWorld. Por defecto:\nC:\\Program Files (x86)\\Steam\\steamapps\\common\\RimWorld", 0, 0x11);
WSH.Echo(folder ? folder.self.path : '');
