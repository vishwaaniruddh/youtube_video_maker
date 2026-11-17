Add-Type -AssemblyName System.Windows.Forms
$p = "F:\YouTube\funny_village_mystery\sample_images\shot_08.png"
if (Test-Path $p) {
    $img = [System.Drawing.Image]::FromFile($p)
    [System.Windows.Forms.Clipboard]::SetImage($img)
    Write-Host "SUCCESS: shot_08.png copied to clipboard as Image"
} else {
    Write-Error "File not found: $p"
}

