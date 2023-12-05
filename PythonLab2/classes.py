# classes.py
from abc import ABC, abstractmethod
import os
import time
from PIL import Image


class FileSnapshot:
    def __init__(self, filename, last_modified):
        self.filename = filename
        self.last_modified = last_modified

    def update_last_modified(self, last_modified):
        self.last_modified = last_modified

    def __str__(self):
        return f"{self.filename} (last modified: {self.last_modified})"


class File(ABC):
    def __init__(self, filename):
        self.filename = filename
        self.snapshot = None

    def set_snapshot(self, snapshot):
        self.snapshot = snapshot

    def get_last_modified(self):
        if self.snapshot:
            return self.snapshot.last_modified
        else:
            return None

    @abstractmethod
    def get_info(self):
        pass


class TextFile(File):
    def __init__(self, filename):
        super().__init__(filename)

    def get_info(self):
        info_str = f"{os.path.basename(self.filename)}"

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()
                line_count = content.count('\n') + 1
                word_count = len(content.split())
                char_count = len(content)

                if line_count > 0:
                    info_str += f" (lines: {line_count}"

                if word_count > 0:
                    info_str += f", words: {word_count}"

                if char_count > 0:
                    info_str += f", characters: {char_count}"

                if os.path.exists(self.filename):
                    last_modified = os.path.getmtime(self.filename)
                    info_str += f", last modified: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modified))}"

                if line_count > 0 or word_count > 0 or char_count > 0:
                    info_str += ")"
        except FileNotFoundError:
            info_str += " (File not found)"

        return info_str


class ImageFile(File):
    def __init__(self, filename):
        super().__init__(filename)
        self.image_size = self.calculate_image_size()

    def calculate_image_size(self):
        try:
            with Image.open(self.filename) as img:
                width, height = img.size
                return f"{width}x{height}"
        except (FileNotFoundError, OSError, IOError):
            return "Unknown"

    def get_info(self):
        info_str = f"Image File: {os.path.basename(self.filename)}, Size: {self.image_size}"

        if os.path.exists(self.filename):
            last_modified = os.path.getmtime(self.filename)
            info_str += f", last modified: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modified))}"

        return info_str


class ProgramFile(File):
    def __init__(self, filename):
        super().__init__(filename)
        self.line_count, self.class_count, self.method_count = self.calculate_statistics()

    def calculate_statistics(self):
        line_count = 0
        class_count = 0
        method_count = 0

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    line_count += 1
                    line = line.strip()

                    if line.startswith("class "):
                        class_count += 1
                    elif line.startswith("def "):
                        method_count += 1
        except FileNotFoundError:
            pass

        return line_count, class_count, method_count

    def get_info(self):
        info_str = f"{os.path.basename(self.filename)}"

        if self.line_count > 0:
            info_str += f" (Lines: {self.line_count}"

        if self.class_count > 0:
            info_str += f", Classes: {self.class_count}"

        if self.method_count > 0:
            info_str += f", Methods: {self.method_count}"

        if os.path.exists(self.filename):
            last_modified = os.path.getmtime(self.filename)
            info_str += f", last modified: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modified))}"

        if self.line_count > 0 or self.class_count > 0 or self.method_count > 0:
            info_str += ")"

        return info_str
