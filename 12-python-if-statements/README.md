# Episode 12 · Python if Statements

*Conditions, Colons and Indentation*

The if statement: run code only when a condition is True, and let indentation decide which lines belong to it.

**Notes:** [12-python-if-statements.pdf](12-python-if-statements.pdf) (colour PDF, A4)

## Key points

- **Shape:** `if`, a space, a condition, a **colon**, then an **indented block** underneath.
- **The condition** comes out as `True` or `False` (usually a comparison). When it's `False`, the whole block is skipped.
- **Indentation decides what belongs to the if.** Lines in one block must line up exactly; use **4 spaces** (PyCharm's Tab key puts them in). A line that isn't indented is outside the block and runs either way.
- **Combine conditions:** `and` needs every condition to be True, `or` needs just one.

## Code

| File | What it is |
|---|---|
| [`code/if_basics.py`](code/if_basics.py) | Program from the video |
| [`code/login.py`](code/login.py) | Program from the video |
| [`code/mistakes/extra_space.py`](code/mistakes/extra_space.py) | Mistake example, stops with an error on purpose: the second print has one extra space, so the block doesn't line up. |
| [`code/mistakes/missing_colon.py`](code/mistakes/missing_colon.py) | Mistake example, stops with an error on purpose: the if line has no colon at the end. |
| [`code/mistakes/no_indent.py`](code/mistakes/no_indent.py) | Mistake example, stops with an error on purpose: the line under the if isn't indented. |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

Files in `code/mistakes/` are the mistakes shown in the video. They are meant to fail, so you can see the error for yourself.

---
Part of [Python and AI](../README.md) by A Bit Clearer.
