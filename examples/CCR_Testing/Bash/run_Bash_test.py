#######################################################
# For module testing on CCR.
# Run as python run_Bash_test.py username
#
# Requires input file f.a,
# src/Bash/receive_lunch_items.sh,
# src/Bash/consume_lunch_items.sh and
# remotebin/Bash/Bash_Launch.sh (mode 755) files.
#######################################################

import sys
import os
import subprocess

def main(argv):

    if (len(argv) == 2):
    
        scriptname = argv[0]
        print ('scriptname: %s' %scriptname)
        username = str(argv[1])
        print ('username: %s' %username)

        if os.path.exists('f.b'):
            os.remove ('f.b')
        if os.path.exists('f.c'):
            os.remove ('f.c')
        
        # Launch
        
        exitStatus = subprocess.call(['./Bash_Launch.sh','receive_lunch_items.sh',username])
        print ('receive_lunch_items.sh exitStatus: %d' %exitStatus)
        
        exitStatus = subprocess.call(['./Bash_Launch.sh','consume_lunch_items.sh'])
        print ('consume_lunch_items.sh exitStatus: %d' %exitStatus)
        
    else:
    
        print ('Wrong number of arguments')
        
#######################################################

if __name__ == "__main__":

    main(sys.argv)