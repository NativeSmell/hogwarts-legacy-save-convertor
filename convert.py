import os
import sys
import argparse
import re


PATTERN = re.compile(r'HL-\d{2}-\d{2}')
NEED_TO_SAVE = {"SavedUserOptions.sav", "SaveGameList.sav", "HL-00-00.sav", "HL-00-10.sav"}



def check_folder_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def check_dir_for_files(save_dir: str) -> list[str]:
    files = []
    for f in os.listdir(save_dir):
        if os.path.isfile(os.path.join(save_dir, f)):
            files.append(os.path.join(save_dir, f))
        elif os.path.isdir(os.path.join(save_dir, f)):
            files += check_dir_for_files(os.path.join(save_dir, f))
    return files


def recognize_file_type(file_data: bytes) -> str | None:
    if b"/Script/Phoenix.SavedSettingsData" in file_data:
        return "SavedUserOptions.sav"
    if b"/Script/PersistentData.PersistentGameData" in file_data:
        text_data = file_data.decode('utf-8', errors='ignore')
        matches = re.findall(PATTERN, text_data)
        if len(matches) > 1:
            return "SaveGameList.sav"
        elif len(matches) == 1:
            return matches[0] + ".sav"

def convert_saves(save_dir: str, need_to_save: set[str]) ->  None:

    files = check_dir_for_files(save_dir)
    saved_files = set()
    for f in files:
        print(f"Find file: {f}")
        with open(f, "rb") as file:
            _type = recognize_file_type(file.read())

            if _type is None:
                print(f"Can't recognize file: {f}. Skipping...")
                continue

            if isinstance(_type, str):
                with open(os.path.join("../hogwarts_legacy_save_converter/output", _type), "wb") as new_file:
                    print(f"Writing file: {os.path.join("../hogwarts_legacy_save_converter/output", _type)}")
                    new_file.write(file.read())
                    saved_files.add(_type)

    for f in need_to_save - saved_files:
        print(f"File {f} not found. It will make a problems!...")
        if f.endswith("10.sav"):
            print("There is no Autosave files")
        elif f.endswith("00-00.sav"):
            print("There is no Manual Save files! Just save game manually")


def arg_parse() -> str | None:
    parser = argparse.ArgumentParser(description="A simple program to convert Hogwarts Legacy saves from GamePass to Steam")
    parser.add_argument("-p", "--path", type=str, help="Path to saves folder")
    return parser.parse_args().path


if __name__ == "__main__":


    check_folder_exists("output")

    path = arg_parse()

    if not path:
        print("No path provided")
        sys.exit(1)

    print(f"Checking path: {path}")
    convert_saves(path, NEED_TO_SAVE)

