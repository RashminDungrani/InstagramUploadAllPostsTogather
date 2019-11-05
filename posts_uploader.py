#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# python 2

from instapy_cli import client
import os
from time import sleep
import time
import random
import shutil
import traceback
import os.path, time
import msvcrt
import sys
from captions import *


username = 'instagram_username'    #Your Instagram username
password = 'instgram_password'       #Your Instagram password


uploaded_dir = str(os.getcwd()) 
posts_location = str(os.getcwd()) + "/posts/"

def uploaded_dir_creating():
    os.chdir(posts_location)
    os.chdir("..")
    uploaded_dir = str(os.getcwd()) + "/"
    if not os.path.isdir(uploaded_dir + "Uploaded"):
        os.mkdir("Uploaded")
    uploaded_dir = uploaded_dir + "Uploaded"

def posts_uploader():
    
    #def uploaded_dir_creating():
    os.chdir(posts_location)
    os.chdir("..")
    uploaded_dir = str(os.getcwd()) + "/"
    if not os.path.isdir(uploaded_dir + "Uploaded"):
        os.mkdir("Uploaded")
    uploaded_dir = uploaded_dir + "Uploaded"

    #Counting Folder images
    def getCountImages():
        return len(os.listdir(posts_location))


    def random_sleep():
        secs = random.randint(10,15)
        print ''
        for i in range(secs):
            sys.stdout.write("\r\t Waiting Time : %d seconds\t" % secs)
            sys.stdout.flush()
            time.sleep(1)
            secs -= 1
        print ''


    def insta_upload():
        if(len(os.listdir(posts_location)) > 0):
            files = os.listdir(posts_location)


            cookie_file = 'COOKIE_FOR_' + username + '.json'
            final_caption = random.choice(text_of_captions)
            with client(username, password, cookie_file=cookie_file, write_cookie_file=True) as cli:
                
                for f in files:
                    cli.upload(posts_location+f, final_caption)
                    shutil.move(posts_location+f,uploaded_dir)
                    print("")
                    print("Caption : " + final_caption)
                    print("")
                    print("*"*10 +"\t" + str(getCountImages()) + " Images Remaining" + "*"*10)
                    print("********************************")
                    random_sleep()

            
            Print("All Post uploaded to Your insta account...")
            print("You can now check out now")
            sleep(1)
        else:
            print("")
            print("**************** Directory is Empty ****************")
            print("")
            sleep(3)

    insta_upload()


posts_uploader()


