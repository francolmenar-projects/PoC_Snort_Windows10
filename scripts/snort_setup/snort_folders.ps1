# $new_rules_dir= TODO Add that the path for the new rules is calculated automatically
$new_rules_dir="C:\Users\Fran Colmenar\project\res\snort\snortrules\rules\*"

$snort_dir="C:\Snort"  # Change in the case the base Snort path is different
$rules_dir="\rules"
$pre_rules_dir="\preproc_rules"

<######## Creating-Checking the existance of the default folders #########>

if (-Not (Test-Path $snort_dir)) {
    Write-Host "Snort folder not found. Exiting..."
    exit -1
}
if (-Not (Test-Path $snort_dir$rules_dir)){
    New-Item -Path $snort_dir$rules_dir -ItemType Directory
}
if (-Not (Test-Path $snort_dir$pre_rules_dir)){
    New-Item -Path $snort_dir$pre_rules_dir -ItemType Directory
}

# TODO Remove the files inside the folders to set up Snort with no previous stuff

Copy-Item -Path $new_rules_dir -Destination $snort_dir$rules_dir -PassThru
