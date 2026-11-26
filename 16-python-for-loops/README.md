# Episode 16 · Python for Loops

*One Item at a Time*

Go through a collection one item at a time with a for loop, step through a string in the debugger, and let range make the numbers for two sums.

**Notes:** [16-python-for-loops.pdf](16-python-for-loops.pdf) (colour PDF, A4)

## Key points

- A **for** loop takes the items of a collection **one at a time**: each round, the current item goes into the **loop variable** and the indented **body** runs. No items left → the loop ends.
- The number of rounds is the **number of items**: no counter, no condition to write. A string is a collection of **characters** (spaces and commas count too).
- Use **while** when you know the condition but not the count; use **for** when you've got the data or know how many rounds.
- **range** makes the numbers: `range(end)`, `range(start, end)`, `range(start, end, step)`. The **end is never included**.

## Code

| File | What it is |
|---|---|
| [`code/for_loop.py`](code/for_loop.py) | Program from the video |
| [`code/multiples_of_3.py`](code/multiples_of_3.py) | Program from the video |
| [`code/odd_sum.py`](code/odd_sum.py) | Program from the video |
| [`code/odd_sum_step2.py`](code/odd_sum_step2.py) | Program from the video |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

---
Part of [Python and AI](../README.md) by A Bit Clearer.
