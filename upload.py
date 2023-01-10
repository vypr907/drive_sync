#this bad boy puts all the pieces together, syncs folders to Google Drive

from pydrive.drive import GoogleDrive
from empty_gdrive_folder import empty_gdrive_folder
from upload_handler import upload_handler
from pydrive.auth import GoogleAuth
from datetime import datetime

def upload(path, folder_id):

    #INITIAL AUTH
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    #Google Folder IDs (if you want to hardcode them in)
    #folder_id = ''

    #EMPTY FOLDER
    #(going to make this an optional step later)
    #empty_gdrive_folder(gauth, folder_id)

    #Path to local folder (if you want to hardcode them in)
    #path = ''


    #Initialize upload handler for local folder path and gdrive folder
    upload_handler(gauth,path,folder_id)

    with open('./update_log.txt','a') as update_log:
        update_log.write('\n'+'Synced with Google Drive on '+ str(datetime.now()))


#If you decide to hard code the Google Drive folder IDs and Directory paths into the upload function, remove the code below,
#and uncomment the upload call at the bottom.

import csv
with open('sync_folder_registry.txt','r') as f:
    reader = csv.reader(f,delimiter=',')
    for row in reader:
        upload(row[0],row[1])


#upload()