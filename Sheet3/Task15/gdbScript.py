#! /usr/bin/env python3

import gdb

key = []
output = []

#This time the key is contained in a shellcode. 
#This shellcode is xorated and called in a subfunction.
#In this subfunction the key is decoded

gdb.execute('set confirm off') #this is set so we dont get the quit anyway promopt
gdb.execute("set pagination off") #so the ouput is not split into pages

gdb.execute('b *main+176') #set break at point where subfunction is entered
gdb.execute('run') #start debugging

for counter in range(0,210): #step through the subfunction
    gdb.execute('ni') #after this point the key is decrypted in parts

for counter in range(0,20): #the key length seems to be 20 character long
    for in_counter in range(0,6): #it takes 6 steps to iterate one character
        gdb.execute('ni')
    tmp = gdb.execute('info registers $eax', to_string=True) #the key part is temporary stored in eax
    local_output = tmp[17:19] #correct format of the part
    key.append(local_output) #append part to key

#This is separated because the structure is broken in the last part of the key.
gdb.execute('ni')
tmp = gdb.execute('info registers $eax', to_string=True)
local_output = tmp[17:19] #correct format of the part
key.append(local_output) #append part to key

for pos in range(0,21): #to change key part from hex to ascii
    output.append(bytes.fromhex(key[pos]).decode('utf-8'))  

f = open("temp_key_file.txt", "w")
f.write("".join(output))
f.close()

gdb.execute('quit')