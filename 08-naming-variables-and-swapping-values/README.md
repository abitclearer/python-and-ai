# Episode 08 · Naming Variables and Swapping Values

*Identifier Rules, PEP 8 Names and the Classic Swap*

The four rules every Python name must follow, the PEP 8 habits that make names easy to read, and two ways to swap the values of two variables.

**Notes:** [08-naming-variables-and-swapping-values.pdf](08-naming-variables-and-swapping-values.pdf) (colour PDF, A4)

## Key points

- An **identifier** is a name you give to something in your code, like a variable.
- **Rules** (break one and the code won't run): only **letters, digits and `_`**; **no digit first**; **no keywords** (35 of them, like `True`, `if`, `for`); **case sensitive** (`age`, `Age`, `AGE` are three variables).
- **Conventions** from **PEP 8** (the code still runs without them): names that say what they hold, **all lowercase**, words joined with underscores (**snake case**).
- To **swap** two variables, save one value in a **temporary variable** first, or write `a, b = b, a`.

## Code

| File | What it is |
|---|---|
| [`code/mistakes/digit_first.py`](code/mistakes/digit_first.py) | Mistake example, stops with an error on purpose: a name can't start with a digit. |
| [`code/mistakes/keyword_name.py`](code/mistakes/keyword_name.py) | Mistake example, stops with an error on purpose: True is a keyword, so it can't be a variable name. |
| [`code/mistakes/swap_wrong.py`](code/mistakes/swap_wrong.py) | Mistake example |
| [`code/names.py`](code/names.py) | Program from the video |
| [`code/swap.py`](code/swap.py) | Program from the video |
| [`code/three_swap.py`](code/three_swap.py) | Program from the video |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

Files in `code/mistakes/` are the mistakes shown in the video. They are meant to fail, so you can see the error for yourself.

---
Part of [Python and AI](../README.md) by A Bit Clearer.
