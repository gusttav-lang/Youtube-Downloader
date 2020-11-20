import sys
import os


def update_ui(arguments):
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
