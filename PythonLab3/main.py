# main.py
import os
import time
from functions import FolderMonitor


def main():
    folder_path = r"C:\Users\OSAdmin\OneDrive\UTM\Year 2\SEM 1\Object Oriented Programming\Lab3ExampleFolder"
    folder_monitor = FolderMonitor(folder_path)

    while True:
        command = input("Enter command (commit, info <filename>, status, exit): ").split()

        if command[0] == 'commit':
            folder_monitor.commit()
        elif command[0] == 'info':
            if len(command) == 2:
                filename = command[1]
                file_info = folder_monitor.get_file_info(filename)
                if file_info:
                    print(file_info.get_info())
                else:
                    print(f"File not found: {filename}")
            else:
                print("Invalid command. Usage: info <filename>")
        elif command[0] == 'status':
            folder_monitor.status()
        elif command[0] == 'exit':
            break
        else:
            print("Invalid command. Please enter a valid command.")


if __name__ == "__main__":
    main()
