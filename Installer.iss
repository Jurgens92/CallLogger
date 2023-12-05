[Setup]
AppName=YourAppName
AppVersion=1.0
DefaultDirName={pf}\YourAppName
OutputDir=Output
OutputBaseFilename=YourAppName_Setup

[Files]
Source: "dist\your_script.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\YourAppName"; Filename: "{app}\your_script.exe"
