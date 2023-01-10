# cleans out Google Drive folder

from pydrive.drive import GoogleDrive

def empty_gdrive_folder(gauth, folder_id):

    #passing in authentication to Drive
    drive = GoogleDrive(gauth)
    

    #iterate through passed folder (via folder_id) and delete all the items in it
    item_list = drive.ListFile({'q':"'{folder_id}' in parents and trashed=false".format(folder_id=folder_id)}).GetList()
    for item in item_list:
        #to view item:
        #print('title: %s, id: %s' % (item['title'], item['id']))
        delete_item = drive.CreateFile({'id': item['id']})
        delete_item.Delete()
        #to view deleted item:
        #print('Deleted title: %s, id: %s' % (item['title'], item['id']))