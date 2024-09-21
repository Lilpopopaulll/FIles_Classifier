import os
import shutil


download_folder = './download'
files = os.listdir(download_folder)
folder_list = []

def get_file_type (file_name) : 
    extension = os.path.splitext(file_name)[1].lower()
    return extension

def folder_check (extension) : 
    if (extension in folder_list) or (extension == '') : 
        return False
    else :
        return True
    
def create_folder (files) :
    for file in files : 
        extension = get_file_type(file)
        if(folder_check(extension)) :
            folder_list.append(extension)
    for folder in folder_list : 
        os.mkdir(folder)
 
 
def move_files (files) :
    for file in files : 
        extension = get_file_type(file)
        shutil.move(os.path.join(download_folder, file), os.path.join(extension, file))



create_folder(files)
move_files(files)

