#!/usr/bin/env python

import os
import os.path
import sys

def usage():
    print """this code is to"""

def searchDir(folder, property):
    for i in os.listdir(folder):
        fullname = os.path.join(folder, i)
        if os.path.isdir(fullname):
            searchDir(fullname, property)
        elif i[-3:] == "edr":
            p = os.popen('echo "%s" | g_energy -f %s -b 200' % (property, fullname), "r")
            for j in p:
                if j.startswith("Statistics"):
                    break
            for j in p:
                if j.strip().startswith(property):
                #if j.strip().startswith(property) and folder[-2:-1] == 'a':
                    sys.stdout.write(folder + i.split('.')[0] + "     ")
                    sys.stdout.write(j)
            p.close()
            os.system("rm \#*xvg*")

    # os.system("rm %s/\#*", fullname)

if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        usage() 
    else:
        searchDir('./', sys.argv[1])

