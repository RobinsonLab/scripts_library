#!/usr/bin/env python
#
# Purpose: convert file from picoquant format to global curve format.
#
# Author: John Robinson
# 
# Date: 8-13-2014
#
# Usage: convert file_name
#
# Result: converts file_name.dat to file_name.prn
#
# cd '/Users/jmrobinson/Cubbies/GiHo-JMR_Cubby/8_11_2014/analysis/no_drug/Mg'
#
import sys
if len(sys.argv) != 2:
    print 'Call convert with one argument, the root filename'
    sys.exit(0)
root = sys.argv[1]
TCAL = 0.016
START = 55
STOP = 1300
CHI_SQR = 115
last_line = STOP + 50
filename_in = root + '.dat'
filename_out = root + '.prn'
f_in = open(filename_in, 'r')
print 'opened: ', filename_in
f_out = open(filename_out, 'w')
print 'writing to: ', filename_out
str = '{:>12}  {:>12} {:>12}  {:>12}\r\n'.format(TCAL, START, STOP, CHI_SQR)
f_out.write(str)

lines = f_in.readlines()
body = False
for line in lines[0:last_line]:
    #print line
    words = line.split()
    if body == True:
        time = words[0]
        IR = words[1]
        sample = words[2]
        str = '{:>12}  {:>12} \r\n'.format(IR, sample)
        f_out.write(str)
    for word in words:
        if word == 'Time[ns]':
            print 'found end of header'
            body = True
f_in.close()
f_out.close()