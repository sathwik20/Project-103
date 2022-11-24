import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir='C:/Users/admin/Downloads'
to_dir='C:/Users/admin/Desktop/Downloaded_Files'
dir_tree={
    'Image_Files':['.jpg','.jpeg','jpeg','.png','.gif','jfif'],
    'Vedio_Files':['.npg','.np2','.npeg','.npe','.npv','.mp4','.m4p','.m4v','.avi','.nov',],
    'Document_Files':['.pdf','.txt','.ppt','.csv','.xls'],
    'Setup_Files':['.exe','.ben','.bin','.cmd']
}

#Event Handler Class
class FileEventHandler(FileSystemEventHandler):


    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.src_path}!")


#initialize Event Handler Class                    

event_handler =FileEventHandler()

#intialize Observer

observer = Observer()

#Schedule the observer

observer.schedule(event_handler,from_dir,recursive=True)

#Start the observer

observer.start()

try:
    while True:
        time.sleep(2)
        print('running...')
except KeyboardInterrupt:
    print('stoped!')        
    observer.stop()
