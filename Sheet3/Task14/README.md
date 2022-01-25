# Reverse Me

Seeing how effortless you managed to parse integers on the last sheet, we fired our old programmer without further consideration.
However, we were informed that his legacy code still drives a part of our system.

We found one of these binaries: `reverseme`.
Please re-implement its functionality as a Python script called `solution`.
We had a brief look, and what seemed a bit strange to us, we can not remember him ever implementing *so many* functions!?

Hints: 
- Use all the tools we mentioned in the lecture to get a good overview first! 
- What is a callback?
- How does this program take user input? How does it behave if there is no such input?
- The program has different exit codes / return value types (4 of them) depending on the user input.
  Make sure your program uses the same codes depending on the user input!
- Use high level python libraries such as requests or httpx.
- You are reimplementing this in Python 3 for a reason.
  Do not meticulously recreate the effects of limited buffer sizes in C, or the exact behaviour of hacky shortcuts our old programmer might have taken.
- The easiest solution is to just call the binary directly in your python script.
  That is however not the point of this exercise 😂

PS: Encodings are annoying, do not worry about the occasional � in your strings for this task.
