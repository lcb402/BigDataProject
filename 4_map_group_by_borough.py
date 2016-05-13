#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    result = line.split(",")
    if 'medallion' not in result:
        date = result[0]
        borough = result[1]
        print '%s\t%s' % (borough, line)
        