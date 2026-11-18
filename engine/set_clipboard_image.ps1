Add-Type -AssemblyName System.Windows.Forms
$filePath = $args[0]
if (-not (Test-Path $filePath)) {
    Write-Error "File not found: $filePath"
    exit 1
}
$img = [System.Drawing.Image]::FromFile($filePath)
[System.Windows.Forms.Clipboard]::SetDataObject($img, $true)
Write-Output "Copied $filePath to clipboard and persisted!"
