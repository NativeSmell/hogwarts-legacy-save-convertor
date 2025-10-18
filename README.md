# hogwarts-legacy-save-convertor
Convert Hogwarts Legacy saves from GamePass to Steam

This is a tool for converting a GamePass save file to a Steam save file.

Insruction:

1. Download the latest version of the script from the [Releases page](https://github.com/NativeSmell/hogwarts-legacy-save-convertor/releases/tag/v1)
2. Unzip it and go to hogwarts-legacy-save-convertor folder
3. Find the GamePass save file and copy the path (You can try to find here: C:\Users\{user}\AppData\Local\Packages\WarnerBros.Interactive.PHX_ktmk1xygcecda\SystemAppData\wgs\)
4. Run the script with the path to the GamePass save file
5. Check the output folder in the script directory
6. Move all the files from the output folder to the Steam saves folder (You will find it in: C:\Users\{user}\AppData\Local\Hogwarts Legacy\Saved\SaveGames\{steam_id})

To run the script, Go to hogwarts-legacy-save-convertor folder -> Right click + Shift on empty space and choose Run Terminal/PowerShell here -> use the following command:
```bash
convert.exe -p /path/to/wgs/folder
```
