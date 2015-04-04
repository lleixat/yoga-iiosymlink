#!/usr/bin/env python

#Search specific device name and make a symlink to it
import os, errno, shutil

iiodir  = "/sys/bus/iio/devices/"
basedir = "/tmp/bus/iio/devices/" # devicename/

# get the IIOName
def getIIOName(dir):
    with open(dir + "/name") as f:
        return f.read().rstrip('\r\n') 

# mkdir -p like
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as e: # Python >2.5
        if e.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

# if basedir exists removeit
if os.path.exists(basedir) and os.access(basedir, os.R_OK):
    #print("File exists and is readable")
    try:
        shutil.rmtree(basedir)
        mkdir_p(basedir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename,e.strerror))
else:
    mkdir_p(basedir)


# for each device in iio:deviceX
for device in os.listdir(iiodir):
    if "iio" in device :
        # get the device name
        src  = iiodir + device
        dest = basedir + getIIOName(src)

        # create the symlink
        os.symlink(src, dest)

        print("Symlink: %s -> %s" % (src, dest))
