# Enable strict mode
Set-StrictMode -Version Latest

# WSL2 Paths
$GAMEDATA = "C:\Program Files (x86)\Steam\steamapps\common\SpaceEngineers\Content\Data"

# Generate ore maps
Write-Output "** Generating ore maps..."
Push-Location -Path Procedural_Ore_Generator
Start-Process -FilePath "java.exe" -ArgumentList "-Xms2G -Xmx16G -jar Procedural_Ore_Generator.jar" -Wait
Pop-Location

# Reset output folder
Write-Output "** Resetting output folder..."
if (Test-Path -Path "./Upload") {
    Remove-Item -Path "./Upload" -Recurse -Force
}
New-Item -ItemType Directory -Path "./Upload/Data" | Out-Null

# Copy base game data files
Write-Output "** Copying vanilla planet data files..."
Robocopy "$GAMEDATA\PlanetDataFiles" "./Upload/Data/" /E /XD "*Tutorial" "SystemTestMap" "Extra"

# Merge ore generator output
Write-Output "** Merging ore generator output..."
Robocopy "Procedural_Ore_Generator\PlanetDataFiles" "./Upload/Data/" /E /XF "*_coloured.png"
Copy-Item -Path "Procedural_Ore_Generator\*.sbc" -Destination "./Upload/Data" -Force

# Merge manual overrides
Write-Output "** Merging manual overrides..."
Robocopy "./Assets/" "./Upload/" /E /L
Robocopy "./Data/" "./Upload/Data/" /E /L

Write-Output "** Done"
