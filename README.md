# drive_sync
Short little blep to sync local folders to Google Drive

This program syncs listed pathnames in `sync_folder_registry.txt` to matching Google folder IDs.

____________________________________
### Run program:
Run `upload.py`
____________________________________
Current version works by emptying the Google Drive folder and uploading local folder. Obviously, a little less than ideal, as what if something happens mid-upload?

Version I'm working on next is a full sync, where it will only upload modified or new files.
____________________________________

This [Medium](https://medium.com/@s.laszloffy/<insert_article_name_here>) post runs through my process, and how to implement this code yourself!

Project based off of Sam Stands' project, which you can read about [here](https://medium.com/swlh/sync-a-folder-on-your-computer-to-google-drive-with-python-5155e73e18ca),
and
dtsvetkov1's project [here](https://github.com/dtsvetkov1/Google-Drive-sync).
