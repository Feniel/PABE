#! /usr/bin/env python3

import gdb
import re

pattern = "\<(.*?)\>"     # should match the current function <my_func>
called_function = ""

# rbreak: Set a breakpoint for all functions matching REGEXP
gdb.execute("rbreak .")
# run until first breakpoint (aka first function start)
gdb.execute("run")

with open("./my_called_functions", "w") as file:

    while called_function != "_exit":   # manual debugging showed this is the last function executed
        current_instruction = gdb.execute("x/i $pc", to_string=True)

        # extract function from instruction and save it
        called_function = re.findall(pattern, current_instruction)[0]
        file.write(f"{called_function}\n")

        gdb.execute("continue")

gdb.execute("quit")
