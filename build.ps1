$exclude = @("venv", "prj_Busca_Passagens.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "prj_Busca_Passagens.zip" -Force