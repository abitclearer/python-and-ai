# Episode 15 · Python while Loops

*Repeat Until It's False*

Repeat code with a while loop, watch it run in the debugger, stop an infinite loop, and add up the even numbers from 1 to 100.

**Notes:** [15-python-while-loops.pdf](15-python-while-loops.pdf) (colour PDF, A4)

## Key points

- A **while** loop runs its indented **body** again and again, for as long as its **condition** is True. The condition is checked **before every round**.
- When the condition comes out **False**, the loop ends and Python moves on. If it never becomes False, you get an **infinite loop**: stop it with the red **Stop** button.
- **Something in the body has to change the condition**, usually a counter: `i += 1`.
- The optional **else** block runs once, when the condition comes out False.

## Code

| File | What it is |
|---|---|
| [`code/even_sum.py`](code/even_sum.py) | Program from the video |
| [`code/even_sum_step2.py`](code/even_sum_step2.py) | Program from the video |
| [`code/while_loop.py`](code/while_loop.py) | Program from the video |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

---
Part of [Python and AI](../README.md) by A Bit Clearer.
