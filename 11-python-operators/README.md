# Episode 11 · Python Operators

*Arithmetic, Assignment, Comparison and Logical Operators*

Python's four families of operators (arithmetic, assignment, comparison, logical), plus why 0.5 - 0.4 isn't exactly 0.1.

**Notes:** [11-python-operators.pdf](11-python-operators.pdf) (colour PDF, A4)

## Key points

- **Arithmetic:** `+ - * / // % **`. A single `/` **always gives a float** (`10 / 5` is `2.0`); `//` rounds down (`10 // 3` is `3`); `%` is the remainder (`10 % 3` is `1`).
- **Floats can be a tiny bit off:** `0.5 - 0.4` is `0.09999999999999998`, because binary can't store most decimals exactly. Use `round(x, 2)` for a tidy answer.
- **Assignment:** `=` stores the right side in the variable on the left; `number += 2` means `number = number + 2`.
- **Comparison and logic:** `==` `!=` `>` `<` `>=` `<=` give `True` or `False` (`=` assigns, `==` compares). `and` needs every condition, `or` needs just one, `not` flips the answer.

## Code

| File | What it is |
|---|---|
| [`code/add_subtract.py`](code/add_subtract.py) | Program from the video |
| [`code/arithmetic.py`](code/arithmetic.py) | Program from the video |
| [`code/assignment.py`](code/assignment.py) | Program from the video |
| [`code/between.py`](code/between.py) | Program from the video |
| [`code/comparison.py`](code/comparison.py) | Program from the video |
| [`code/float_precision.py`](code/float_precision.py) | Program from the video |
| [`code/mistakes/add_subtract_int.py`](code/mistakes/add_subtract_int.py) | Mistake example, stops with an error on purpose: int() can't read a number with a decimal point. Use float() for that. |
| [`code/mistakes/add_subtract_text.py`](code/mistakes/add_subtract_text.py) | Mistake example, stops with an error on purpose: input() gives back strings, so + joins them and - doesn't work on text. |
| [`code/outside.py`](code/outside.py) | Program from the video |
| [`code/precedence.py`](code/precedence.py) | Program from the video |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

Files in `code/mistakes/` are the mistakes shown in the video. They are meant to fail, so you can see the error for yourself.

---
Part of [Python and AI](../README.md) by A Bit Clearer.
