# !/usr/bin/env python
# -*- coding:utf-8 -*- 
import os
import sys
import getopt
import json

def gitSync(repoListFile):
    if not os.path.exists(repoListFile):
        print("repoList" + repoList + "file not found")
        return
    with open(repoListFile, 'r') as f:
        temp = json.loads(f.read())
        repoList = temp['repos']
        for repo in repoList:
            syncRepo(repo['sourceUri'], repo['destUri'])

def syncRepo(sourceUri , destUri):
    createRepo = "cm repository create " + destUri
    sync = "cm sync " + destUri + " git " + sourceUri
    os.system(createRepo)
    os.system(sync)

    
def main():

    # get intput agrs
    options, args = getopt.getopt(sys.argv[1:], 'f:')
    for opt, arg in options:
        if opt == '-f':
            repoList = arg

    # sync git repos to plastic
    gitSync(repoList)


if __name__=="__main__":
    main()
