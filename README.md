# hogwarts-legacy-save-convertor
Convert Hogwarts Legacy saves from GamePass to Steam

This is a tool for converting a GamePass save file to a Steam save file.

Insruction:

1. Download the latest version of the script from the [GitHub repository](https://github.com/hogwarts-legacy-save-convertor)
2. Find the GamePass save file and copy the path (You can try to find here: C:\Users\{user}\AppData\Local\Packages\WarnerBros.Interactive.PHX_ktmk1xygcecda\SystemAppData\wgs\)
3. Run the script with the path to the GamePass save file
4. Check the output folder in the script directory
5. Move all the files from the output folder to the Steam saves folder (You will find it in: C:\Users\{user}\AppData\Local\Hogwarts Legacy\Saved\SaveGames\{steam_id})

To run the script, use the following command:
```bash
python3 convert.py -p /path/to/wgs/folder
```