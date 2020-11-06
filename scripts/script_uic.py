import sys
import os


"""
Make sure that you are inside script folder when using the follow commands
How to use:
    python script_uic [.ui file name]
        "this way the script will create .py relate to the .ui file specified"
    python script_uic
        "this way the script will create all .py for all .ui files"
"""


def update_ui(arguments):
    # sys.argv[0] is always our file 'script_uic.py'
    if len(arguments) > 1:
        files = arguments[1:]
        for file in files:
            command(file)
    else:
        print(
            """
*** All .py files related to .ui files are gonna be create/update ***
            """)
        files = os.listdir("../forms/")
        for file in files:
            command(file)


def command(file_name):
    if file_name.endswith(".ui"):
        output_name = file_name[:-3] + "_ui.py"

        cmd = f'pyside2-uic "../forms/{file_name}" '
        cmd += f'-o "../src/ui/{output_name}" '
        cmd += '--from-imports'

        print(f"-> {cmd}")
        os.system(cmd)
    else:
        print(f"{file_name} is not valid")


if __name__ == '__main__':
    update_ui(sys.argv)
