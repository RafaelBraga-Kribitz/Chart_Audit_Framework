param(
    [Parameter(Mandatory = $true)][string]$ImageDir,
    [Parameter(Mandatory = $true)][string]$OutDir
)
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Media.Ocr, ContentType = WindowsRuntime]
$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq "AsTask" -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq "IAsyncOperation``1"
})[0]
function Await-Op($op, $type) {
    $method = $asTaskGeneric.MakeGenericMethod($type)
    $task = $method.Invoke($null, @($op))
    $task.Wait(-1) | Out-Null
    return $task.Result
}
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
$files = Get-ChildItem -Path $ImageDir -Filter *.jpg | Sort-Object Name
foreach ($f in $files) {
    $dest = Join-Path $OutDir ($f.BaseName + ".json")
    if (Test-Path $dest) { continue }
    $file = Await-Op ([Windows.Storage.StorageFile]::GetFileFromPathAsync($f.FullName)) ([Windows.Storage.StorageFile])
    $stream = Await-Op ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $decoder = Await-Op ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bitmap = Await-Op ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $result = Await-Op ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
    $words = @()
    foreach ($line in $result.Lines) {
        foreach ($w in $line.Words) {
            $rect = $w.BoundingRect
            $x = 0; $y = 0
            try { $x = [double]$rect.X } catch { $x = [double]$rect[0].X }
            try { $y = [double]$rect.Y } catch { $y = [double]$rect[0].Y }
            $words += [ordered]@{ t = $w.Text; x = [int]$x; y = [int]$y }
        }
    }
    $obj = [ordered]@{ file = $f.Name; words = $words }
    $obj | ConvertTo-Json -Depth 5 -Compress | Set-Content -Path $dest -Encoding utf8
    Write-Output $f.Name
}
