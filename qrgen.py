#!/usr/bin/env python
import os
import sys

PATH = './images'
def savecode(name, value):
    os.environ['var']=str(value)
    os.environ['name']=str(PATH + '/'+name +'.png')
    os.system('qrencode -o $name $var')

def newdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

try:
    filename = sys.argv[1]
    newdir(PATH)
    with open(filename) as f:
        data = f.readlines()
        cnt = 0
        for i in data:
            if i.find("LinkNodeR8") != -1:
                (devName,devType,devID,apikey)=i.split(',')
                devID = devID.strip()
                apikey = apikey.strip()
                name = devID+apikey
                info = "d1:" + devID + ",k1:" + apikey
                savecode(name, info)
                cnt += 1
        print cnt,"png files generated"

except:
    print "usage:",sys.argv[0],"<cvs file>"

