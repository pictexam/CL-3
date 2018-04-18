import os
import sys

def createf():
	os.system("./dropbox_uploader.sh mkdir newdir")

def listf():
	os.system("./dropbox_uploader.sh list")
	
def uploadf():
	os.system("./dropbox_uploader.sh upload /home/rashi/x.py /newdir/")
	
def downloadf():
	os.system("./dropbox_uploader.sh download /newdir/x.py")

def deletef():
	os.system("./dropbox_uploader.sh delete /newdir")


