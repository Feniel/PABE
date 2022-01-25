# Key Checker

The program `check_key` needs a valid key as an input.
Find out how to provide the key to the program and how the key checking algorithm works
(use a reverse engineering tool such as IDA Pro, Ghidra, radare2, or Binary Ninja, or use a debugger, such as gdb).

The final task is to write a Python script as `solution` that is able to generate valid keys and print _500_ of them to `stdout` (**unique keys**).

Your solution could, for example, look like this:

```shell
./solution
key1
key2
key3
...
key500
```

where `keyX` is a valid key. 

Note: Do not brute-force all solutions by executing the binary `check_key` and checking its output. This is a Reverse Engineering Task 😉
