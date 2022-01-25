# C++ and vtables

In this task you have to exploit a vulnerability that leads to a vtable pointer overwrite.
Although it is also possible to overwrite the return address of `main()`, you **must not** use this approach.

What you should do:

1. Find the bug(s)
2. Understand how vtables work in C++ (e.g., <https://en.wikipedia.org/wiki/Virtual_method_table>, <https://godbolt.org/z/les9Bx>)
3. Exploit the bug to get the flag from `flag.txt` by manipulating the vtable (pointer)

Once again, edit the provided `solution` template and explain your approach with meaningful comments!

Your solution should execute like this:

```shell
$ ./solution
FLAG{...}
```

Hints:

- Are there any useful functions in the binary?
- How can you manipulate the control flow without overwriting the return address?

Ask yourself the following questions:

- How is `PabeUser::set_username(std::string)` invoked at assembly level?
- What if you change the pointer from `set_username(std::string)` to a function which invokes `system` to get the flag printed?
