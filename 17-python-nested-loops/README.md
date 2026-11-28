# Episode 17 · Python Nested Loops

*A Loop Inside a Loop*

Put a loop inside another loop, print a rectangle of stars in any size, control where print ends a line, and print the multiplication table up to 9 x 9.

**Notes:** [17-python-nested-loops.pdf](17-python-nested-loops.pdf) (colour PDF, A4)

## Key points

- A **nested loop** is a loop inside the **body** of another loop: the **outer** loop and the **inner** loop.
- For **every round of the outer loop**, the inner loop runs **all the way through**, like the second hand going round once for every tick of the minute hand.
- `print` adds a **new line** after its output. The **end** option changes that: `end=""`, `end="  "`, `end="\t"`. `print()` on its own just starts a new line.
- For a grid of output, the **outer loop handles the rows** and the **inner loop handles the cells** in each row. The inner loop can use the outer loop's variable.

## Code

| File | What it is |
|---|---|
| [`code/rectangle.py`](code/rectangle.py) | Program from the video |
| [`code/times_table.py`](code/times_table.py) | Program from the video |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

---
Part of [Python and AI](../README.md) by A Bit Clearer.
