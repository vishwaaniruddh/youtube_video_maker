$wshell = New-Object -ComObject wscript.shell;
Start-Sleep -Seconds 2;
$wshell.SendKeys('F:\YouTube\funny_village_mystery\100_percent_real_motion_cartoon_movie.mp4');
Start-Sleep -Milliseconds 500;
$wshell.SendKeys('{ENTER}');
Write-Host "KEYSTROKES_SENT";

