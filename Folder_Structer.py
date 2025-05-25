from PIL import Image 
import numpy as np
import os
from pathlib import Path
import shutil

class folder_structer:
    def __init__(self):
        self.folders = []
        self.save_path = ""

    def format_struc(self,path):
        return(str(path).lower())

    def get_folders_struc(self,look_path):
        # Specify the directory path
        directory_path = Path(look_path)
        # Get all subfolders recursively
        folders = [item for item in directory_path.rglob("*") if item.is_dir()]
        # Print the list of folders
        for folders in folders:
            self.folders.append(self.format_struc(folders))
        return(self.folders)
    
    def get_items(self,save_path):
        source_dirs = self.folders # Add your folder paths here

        # Copy files from each source directory
        for src_dir in source_dirs:
            destination_dir = Path(str(save_path)+ "/" + src_dir)  # Destination folder
            # Ensure destination exists
            destination_dir.mkdir(parents=True, exist_ok=True)
            src_path = Path(src_dir)
            
            for file in src_path.iterdir():
                if file.is_file():  # Ensure it's a file, not a folder
                    file_format = self.format_struc(file.name)
                    shutil.copy(file, destination_dir /  file_format)  # Copy file to destination
                    print(f"Copied: {(file.name.lower())}")

    def copy_struc_save(self,save_path,look_path):
        os.makedirs(save_path, exist_ok=True)
        self.folders = self.get_folders_struc(look_path)
        self.get_items(save_path)

#a = folder_structer()
#a.run("sprite/Idle/idle.png",[48,64])
#a.copy_struc_save("animation","Sprite")