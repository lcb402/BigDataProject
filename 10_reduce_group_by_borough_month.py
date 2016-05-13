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
            jan = current_borough_data.count("0")
            feb = current_borough_data.count("1")
            mar = current_borough_data.count("2")
            apr = current_borough_data.count("3")
            may = current_borough_data.count("4")
            june = current_borough_data.count("5")
            july = current_borough_data.count("6")
            aug = current_borough_data.count("7")
            sept = current_borough_data.count("8")
            oct = current_borough_data.count("9")
            nov = current_borough_data.count("10")
            dec = current_borough_data.count("11")
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d" %(current_borough, jan, feb, mar, apr, may, june, july, aug, sept, oct, nov, dec)
        current_borough = borough
        current_borough_data = []
        current_borough_data.append(data)
		
jan = current_borough, current_borough_data.count("0")
feb = current_borough, current_borough_data.count("1")
mar = current_borough, current_borough_data.count("2")
apr = current_borough, current_borough_data.count("3")
may = current_borough, current_borough_data.count("4")
june = current_borough, current_borough_data.count("5")
july = current_borough, current_borough_data.count("6")
aug = current_borough, current_borough_data.count("7")
sept = current_borough, current_borough_data.count("8")
oct = current_borough, current_borough_data.count("9")
nov = current_borough, current_borough_data.count("10")
dec = current_borough, current_borough_data.count("11")
print "%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d" %(current_borough, jan, feb, mar, apr, may, june, july, aug, sept, oct, nov, dec)

        
        