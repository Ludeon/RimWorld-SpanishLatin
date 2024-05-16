:: credits Ragnar-F
@if (@a==@b) @end /*

@echo off
setlocal

for /f "delims=" %%I in ('cscript /nologo /e:jscript "%~f0"') do (
    set FLDR=%%I
)
if "%FLDR%"=="" (exit)

rd /q /s "%FLDR%\Data\Core\Languages\SpanishLatin (Español(Latinoamérica))"
rd /q /s "%FLDR%\Data\Royalty\Languages\SpanishLatin (Español(Latinoamérica))"
rd /q /s "%FLDR%\Data\Ideology\Languages\SpanishLatin (Español(Latinoamérica))"
rd /q /s "%FLDR%\Data\Biotech\Languages\SpanishLatin (Español(Latinoamérica))"
rd /q /s "%FLDR%\Data\Anomaly\Languages\SpanishLatin (Español(Latinoamérica))"

xcopy /s /i "Core" "%FLDR%\Data\Core\Languages\SpanishLatin (Español(Latinoamérica))"
xcopy /s /i "Royalty" "%FLDR%\Data\Royalty\Languages\SpanishLatin (Español(Latinoamérica))"
xcopy /s /i "Ideology" "%FLDR%\Data\Ideology\Languages\SpanishLatin (Español(Latinoamérica))"
xcopy /s /i "Biotech" "%FLDR%\Data\Biotech\Languages\SpanishLatin (Español(Latinoamérica))"
xcopy /s /i "Anomaly" "%FLDR%\Data\Anomaly\Languages\SpanishLatin (Español(Latinoamérica))"

del "%FLDR%\Data\Core\Languages\SpanishLatin (Español(Latinoamérica)).tar"
del "%FLDR%\Data\Royalty\Languages\SpanishLatin (Español(Latinoamérica)).tar"
del "%FLDR%\Data\Ideology\Languages\SpanishLatin (Español(Latinoamérica)).tar"
del "%FLDR%\Data\Biotech\Languages\SpanishLatin (Español(Latinoamérica)).tar"
del "%FLDR%\Data\Anomaly\Languages\SpanishLatin (Español(Latinoamérica)).tar"

goto :EOF

:: JScript portion */

var shl = new ActiveXObject("Shell.Application");
var folder = shl.BrowseForFolder(0, "Selecciona la carpeta de RimWorld. Por defecto:\nC:\\Program Files (x86)\\Steam\\steamapps\\common\\RimWorld", 0, 0x11);
WSH.Echo(folder ? folder.self.path : '');