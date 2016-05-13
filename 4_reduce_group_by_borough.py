#!/usr/bin/python

import sys

current_borough = None
current_borough_data = []

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    borough, data = line.strip().split("\t", 1)
    
    if borough == current_borough:
        current_borough_data.append(data)
    else:
        if current_borough:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d" %(current_borough, len(current_borough_data))
        current_borough = borough
        current_borough_data = []
        current_borough_data.append(data)
print "%s\t%d" %(current_borough, len(current_borough_data))

        
        