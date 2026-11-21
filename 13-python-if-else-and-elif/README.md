# Episode 13 · Python if, else and elif

*Two Paths, Many Paths, Nested Paths*

Two paths with else, many paths with elif, and one decision inside another, plus PyCharm's debugger to watch which lines run.

**Notes:** [13-python-if-else-and-elif.pdf](13-python-if-else-and-elif.pdf) (colour PDF, A4)

## Key points

- **else** runs when the `if` condition is `False`. It gets a **colon but never a condition**, so exactly one of the two blocks runs.
- **elif** (short for "else if") adds more conditions. Python checks them **top to bottom**, and **only the first True block runs**.
- A final **else** catches everything left over. It's optional, and if it's there it goes last.
- **Nested if:** an `if` inside another `if`. Indentation shows which decision each line belongs to; `pass` holds an empty block.

## Code

| File | What it is |
|---|---|
| [`code/accounts.py`](code/accounts.py) | Program from the video |
| [`code/leap_year.py`](code/leap_year.py) | Program from the video |
| [`code/login_else.py`](code/login_else.py) | Program from the video |
| [`code/mistakes/indented_elif.py`](code/mistakes/indented_elif.py) | Mistake example, stops with an error on purpose: the elif is indented, so Python reads it as part of the if block. |
| [`code/number_sign.py`](code/number_sign.py) | Program from the video |
| [`code/triangle.py`](code/triangle.py) | Program from the video |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

Files in `code/mistakes/` are the mistakes shown in the video. They are meant to fail, so you can see the error for yourself.

---
Part of [Python and AI](../README.md) by A Bit Clearer.
