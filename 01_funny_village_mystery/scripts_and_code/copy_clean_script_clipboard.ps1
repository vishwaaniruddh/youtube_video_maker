$content = Get-Content -Path "F:\YouTube\funny_village_mystery\scripts_and_code\clean_hindi_script_no_tags.txt" -Raw -Encoding utf8
Set-Clipboard -Value $content
Write-Host "SUCCESS: Clean Hindi script copied to clipboard without any tone tags!"

