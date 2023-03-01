from abc import ABC, abstractmethod
from typing import Any, Optional

'''
Using the composite design pattern to implement file system
'''

class FileSystemInterface(ABC):
    @abstractmethod
    def ls():
        pass

class FileTypeSystem(FileSystemInterface):
    def __init__(self, file_name: str):
        self.file_name = file_name
    def ls(self):
        print(f"FILENAME {self.file_name}")

class DirTypeSystem(FileSystemInterface):
    def __init__(self, dir_name: str):
        self.dir_name = dir_name
        self.sub_dir = []
    
    def ls(self):
        print(f"Dir name {self.dir_name}")
        for file_dir in self.sub_dir:
            file_dir.ls()
    
    def add(self, file_dir: FileSystemInterface):
        self.sub_dir.append(file_dir)


if __name__ == "__main__":
    parent_dir = DirTypeSystem("movies")
    border_movie = FileTypeSystem("border")
    golmal_movie = FileTypeSystem("golmal")
    sub_dir = DirTypeSystem("comedy")
    parent_dir.add(border_movie)
    sub_dir.add(golmal_movie)
    parent_dir.add(sub_dir)
    parent_dir.ls()