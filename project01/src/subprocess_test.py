#!/usr/bin/env python3

import subprocess
import sys

def main():
    dir = '/var/log'
    print('listdir function called')
    listdir(dir)

## Given a dir path, run an external 'ls -l' on it --
## shows how to call an external program
def listdir(dir):
  cmd = 'ls -l ' + dir
  print("Command to run:", cmd)   ## good to debug cmd before actually running it
  (status, output) = subprocess.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(status)
  print(output)  ## Otherwise do something with the command's output



if __name__  ==  '__main__' : 
      main()
