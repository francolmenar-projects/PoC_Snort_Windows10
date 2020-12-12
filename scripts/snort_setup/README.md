# snort_setup
Scripts used for the set of Snort at Windows 10. 

## snort_folders.ps1

- Checks the existence of some of the needed Snort folders and if they do not exist they are created.
- Copies the downloaded rules into to the folder "rules" from Snort.
    - At this version the path to the new rules is set at the script and the Snort Path is set to "C:\Snort".  