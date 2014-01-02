#!/usr/bin/env python
import os
for dirPath, dirNames, fileNames in os.walk("./"):
    #print (dirPath)
    #for f in fileNames:
    #    print (os.path.join(dirPath, f))
    print(dirPath)
    #print(fileNames)

    file_name = dirPath[2:]
    #print(file_name)
    change_path = "cd "+dirPath
    #print(change_path)
    comparess_data = "tar -jcvf %s.tar.bz2 JKZ_* sim.log.gz waypoint_gen.v"%file_name
    #print(comparess_data)
    command = change_path+" ; "+comparess_data
    comaand = change_path+" ; "+"mv *.tar.bz2 ../"
    print(command)
    os.system(command)
    #os.system("ls")


os.system("echo Finish")
