import os
import time
from classes import FileSnapshot, TextFile, ImageFile, ProgramFile


class FolderMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshots = self.load_snapshots()
        self.changes_detected = False

    @staticmethod
    def load_snapshots():
        snapshots = {}
        try:
            with open("snapshots.txt", "r") as file:
                for line in file:
                    values = line.strip().split(',')
                    if len(values) >= 2:
                        filename, last_modified = values[0], str(values[1])
                        snapshots[filename] = FileSnapshot(filename, last_modified)
        except FileNotFoundError:
            pass
        return snapshots

    def save_snapshots(self):
        with open("snapshots.txt", "w") as file:
            for filename, snapshot in self.snapshots.items():
                file.write(f"{filename},{snapshot.last_modified}\n")

    def commit(self):
        current_time = time.strftime("%Y-%m-%d, %H:%M:%S")
        deleted_files = set(self.snapshots.keys()) - set(os.listdir(self.folder_path))

        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                if filename in self.snapshots:
                    self.snapshots[filename].update_last_modified(current_time)
                else:
                    self.snapshots[filename] = FileSnapshot(filename, current_time)

        for deleted_file in deleted_files:
            del self.snapshots[deleted_file]

        print(f"Commit successful. Snapshot time updated to {current_time}.")
        self.save_snapshots()

    def get_file_info(self, filename):
        file_path = os.path.join(self.folder_path, filename)
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)
            if extension in ['.txt']:
                return TextFile(file_path)
            elif extension in ['.png', '.jpg']:
                return ImageFile(file_path)
            elif extension in ['.py', '.java']:
                return ProgramFile(file_path)
        return None

    def status(self):
        status_messages = []
        self.snapshots = self.load_snapshots()

        for filename, snapshot in self.snapshots.items():
            file_info = self.get_file_info(filename)
            if file_info:
                last_modified = file_info.get_last_modified()
                if last_modified and snapshot.last_modified != last_modified:
                    status_messages.append(f"{filename} has changed.")
                    snapshot.update_last_modified(last_modified)
                    self.changes_detected = True  # Set changes_detected to True
                else:
                    status_messages.append(f"{filename} has not changed.")

        new_files = set(os.listdir(self.folder_path)) - set(self.snapshots.keys())
        deleted_files = set(self.snapshots.keys()) - set(os.listdir(self.folder_path))

        for new_file in new_files:
            status_messages.append(f"{new_file} is a new file.")

        for deleted_file in deleted_files:
            status_messages.append(f"{deleted_file} has been deleted.")

        if not status_messages:
            print("No changes have been made.")
        else:
            for message in status_messages:
                print(message)
