#handles the upload

import os
from pydrive.drive import GoogleDrive

def upload_handler(gauth, os_root_path, gdrive_root_folder_id):
    #Google Authentication
    drive = GoogleDrive(gauth)
    dir_dict = {os_root_path: gdrive_root_folder_id}

    #for each dir path, starting from os_root_path by os.walk()
    for dirpath, dirnames, files in os.walk(os_root_path):
        print(dirpath, dirnames)

        for file in files:
            #create GoogleDriveFile instance to parentID
            new_file = drive.CreateFile({'title': file, "parents": [{"kind": "drive#fileLink","id": dir_dict[dirpath]}]})
            file_path = os.path.join(dirpath, file)

            #set content of the file from given string
            new_file.SetContentFile(file_path)
            print(new_file)
            new_file.Upload()

        #for this path, create a folder
        for dirname in dirnames:
            new_folder = drive.CreateFile({'title': dirname, "parents":  [{"id": dir_dict[dirpath]}], "mimeType": "application/vnd.google-apps.folder" })
            new_folder.Upload()
            dir_dict[os.path.join(dirpath, dirname)] = new_folder['id']