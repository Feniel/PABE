## ROP ROP ROP ROP ROP

This time there are two binaries: `vuln` and `execute_me_with_rop`.
There is a simple vulnerability in `vuln`.

Your task is to build a ROP chain that executes `execute_me_with_rop` so that it prints the flag.

Use the `execve` system call and prepare all necessary arguments accordingly.

You must **not** use pwntools' `pwnlib.shellcraft` for this exercise!

You must also **not** just `execve("/bin/sh -c './execute_me_with_rop arg1 arg2'")` for the execution of `execute_me_with_rop`!

Once again, edit the provided `solution` template and explain your approach with meaningful comments!

Hints: 

- Try to write a C program first which executes `execute_me_with_rop`, to find out how to build your ROP chain:

```c
#include <unistd.h>

int main()
{
  char* argv[] = { "./execute_me_with_rop" , "foo", "bar", NULL };
  char* envp[] = { "PABE=FUN",  NULL };
  execve("./execute_me_with_rop", argv, envp);
  return 0;
}
```

- Have a look at the Hello-World ROP chain in order to build your ROP chain

- Remember how to set `argv**`

**Leaking the address**

- Try to leak the address of `__libc_csu_init` from the stack and calculate the `file_base_addr`

- Next, use the `file_base_addr` to build a small ROP-chain from the `./vuln` which invokes `puts-PLT` and as an `puts-GOT` entry as its parameter and finally start the program again through the ROP-chain in oder to leak `puts@GLIBC`.
