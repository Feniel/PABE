#! /usr/bin/env python3

import gdb

key = []

gdb.execute('start') #to get to the main function
gdb.execute('ni') #offset to get to jump point

for n in range(0,7): #we have a key length of 7 so we have to iterate 7 times
    for y in range(0,13): #iterate to next jump point (12 difference)
        gdb.execute('ni')
    tmp = gdb.execute('info registers edx', to_string=True) #read edx for next key part
    key.append(tmp[17:19]) #format for gdb output

output = []
for pos in range(0,7): #to change from hex to ascii
    output.append(bytes.fromhex(key[pos]).decode('utf-8'))  

print(''.join(output))

gdb.execute('quit')