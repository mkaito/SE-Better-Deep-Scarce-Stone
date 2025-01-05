# Enable strict mode
Set-StrictMode -Version Latest

# Cleanup function
function Cleanup {
    Remove-Item -Path "mod.vdf", "description.bb", "changenote.bb" -ErrorAction SilentlyContinue
}
# Register the cleanup function to run on script exit
Register-EngineEvent -SourceIdentifier PowerShell.Exiting -Action { Cleanup }

# Define paths and variables
$pandocPath = (Get-Command pandoc).Source
$steamCmdPath = (Get-Command steamcmd).Source
$readmeInput = "readme.md"
$changenoteInput = "changenote.md"
$descriptionOutput = "description.bb"
$changenoteOutput = "changenote.bb"
$maxDescriptionSize = 7999
$modVdfFile = "mod.vdf"
$steamPassword = $env:STEAMPASSWORD

if (-not $steamPassword) {
    throw "Environment variable 'STEAMPASSWORD' is not set. Please set it before running the script."
}

# Convert Markdown to Steam BBCode
& $pandocPath -f gfm -t ./vendor/2bbcode/bbcode_steam.lua -o $descriptionOutput -- $readmeInput
& $pandocPath -f gfm -t ./vendor/2bbcode/bbcode_steam.lua -o $changenoteOutput -- $changenoteInput

# Read the description content once
$descriptionContent = Get-Content $descriptionOutput -Raw
if ($descriptionContent.Length -gt $maxDescriptionSize) {
    throw "Description size too big: $($descriptionContent.Length). Limit $maxDescriptionSize."
}

# Read the changenote content
$changenoteContent = Get-Content $changenoteOutput -Raw

# Generate mod.vdf content
$modVdfContent = @"
"workshopitem"
{
  "appid"             "244850"
  "publishedfileid"   "2724252237"
  "contentfolder"     "$($PSScriptRoot)\Upload"
  "previewfile"       "$($PSScriptRoot)\Upload\preview.jpg"
  "description"       "$descriptionContent"
  "changenote"        "$changenoteContent"
}
"@
Set-Content -Path $modVdfFile -Value $modVdfContent

# Upload to Steam Workshop
& $steamCmdPath +login mkaito $steamPassword +workshop_build_item (Resolve-Path $modVdfFile) +quit

Write-Output "Upload complete!"
