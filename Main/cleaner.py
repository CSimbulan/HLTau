from os import system
import sys

## Dropbox paths

## Generic paths
dataPath = "DataFiles/"
logPath = "LogFiles/"
hbPath = "HBFiles/"
savePath = "SaveStates/"
resPath = "ResFiles/"
posPath = "PosFiles/"

system("rm -rf " + dataPath)
system("rm -rf " + logPath)
#system("rm -rf " + hbPath)
system("rm -rf " + savePath)
#system("rm -rf " + resPath)
system("rm -rf " + posPath)

if len(sys.argv) > 1:
    system("mkdir " + dataPath)
    system("mkdir " + logPath)
    #system("mkdir " + hbPath)
    system("mkdir " + savePath)
    #system("mkdir " + resPath)
    system("mkdir " + posPath)
