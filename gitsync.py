# !/usr/bin/env python
# -*- coding:utf-8 -*- 
import os
import sys
import re
import getopt
import subprocess
import json

def gitSync(repoListFile, hostUri):
    if not os.path.exists(repoListFile):
        print("repoList" + repoList + "file not found")
        return
    with open(repoListFile, 'r') as f:
    temp = json.loads(f.read())
    repoList = temp['repos']
    for repo in repoList:
        syncRepo(repo['sourceUri'], repo['destUri'])
    f.close()

def syncRepo(repoUri , hostUri):
    temp = re.split('[/.]', repoUri)
    repoName = temp[len(temp)-2]
    createRepo = "cm repository create " + repoName + hostUri
    sync = "cm sync " + repoName + hostUri + " git " + repoUri
    os.system(createRepo)
    p = os.system(sync)
    print(sync)
    
def main():
    # define some varibles
    hostUri = "@ssl://unity-tech-cn@sh01-plasticscm.unity.cn:8787"

    # get intput agrs
    options, args = getopt.getopt(sys.argv[1:], 'f:')
    for opt, arg in options:
        if opt == '-f':
            repoList = arg

    # sync git repos to plastic
    gitSync(repoList, hostUri)


if __name__=="__main__":
    main()
