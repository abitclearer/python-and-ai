# Episode 07 · Literals and Variables

*How Python Writes, Stores and Changes Data*

How to write values straight into Python code (literals), how to store and change them (variables), and a small program that predicts a video's views.

**Notes:** [07-literals-and-variables.pdf](07-literals-and-variables.pdf) (colour PDF, A4)

## Key points

- A **literal** is a fixed value typed into your code: **int** `18`, **float** `3.14`, **bool** `True` / `False`, **str** `"Hello"`, and **None**.
- **Anything in quotes is a string**, even `"10000"`. `True` and `False` need a capital letter, and in maths they count as **1** and **0**.
- A **variable** is a name for a value: `name = value`. The `=` means **assign**: Python works out the right side first, then stores the result on the left.
- A variable holds **one value at a time** and needs a value **before** you use it. `print` shows several values at once, separated by commas.

## Code

| File | What it is |
|---|---|
| [`code/literals.py`](code/literals.py) | Program from the video |
| [`code/mistakes/lowercase_true.py`](code/mistakes/lowercase_true.py) | Mistake example, stops with an error on purpose: True and False need a capital letter. |
| [`code/mistakes/not_assigned.py`](code/mistakes/not_assigned.py) | Mistake example, stops with an error on purpose: a variable needs a value before you can use it. |
| [`code/mistakes/string_plus_number.py`](code/mistakes/string_plus_number.py) | Mistake example, stops with an error on purpose: "10000" is a string, so you can't add a number to it. |
| [`code/variables.py`](code/variables.py) | Program from the video |
| [`code/views.py`](code/views.py) | Program from the video |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

Files in `code/mistakes/` are the mistakes shown in the video. They are meant to fail, so you can see the error for yourself.

---
Part of [Python and AI](../README.md) by A Bit Clearer.
