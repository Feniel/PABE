# Some Poison for the cash machine

Money is not everything, but with money everything is more fun.
Therefore we want to use this awesome cash machine to get our money printed.

Poison `cash_machine` in a way that it gives you a shell, and use the shell to print the flag!

Edit the provided `solution` template and explain your approach with meaningful comments!


Hints:

- Have a look at the backdoor function
- How can you set up `RDI` when invoking the backdoor function?
- Which functions offers you the possiblity that your allocation gets into the **TCACHE**?
- Can you see the diference between the `cashbox_delete` and the `cashbox_update` functions? What can you use after that?

Your solution should execute like this:

```
./solution
FLAG{some letters here}
```


