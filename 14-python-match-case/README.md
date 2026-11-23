# Episode 14 · Python match case

*One Value, Many Cases*

Check one value against a list of fixed values with match and case, then trace it in the debugger and build a small calculator.

**Notes:** [14-python-match-case.pdf](14-python-match-case.pdf) (colour PDF, A4)

## Key points

- **match** names the value once; each **case** lists one possible value. Python checks the cases **top to bottom**, and **only the first match runs**.
- A **vertical bar** lets one case match several values: `case "6" | "7":` means 6 **or** 7.
- **`case _:`** (no quotes) is a wildcard: it catches everything else, like `else`. It's optional and goes last.
- A **guard** adds a condition after the pattern: `case "/" if num2 != 0:` only matches when the guard is True. Needs **Python 3.10** or newer.

## Code

| File | What it is |
|---|---|
| [`code/calculator.py`](code/calculator.py) | Program from the video |
| [`code/game_controls.py`](code/game_controls.py) | Program from the video |
| [`code/mistakes/divide_by_zero.py`](code/mistakes/divide_by_zero.py) | Mistake example, stops with an error on purpose: the "/" case has no guard, so 10 / 0 crashes. |
| [`code/schedule.py`](code/schedule.py) | Program from the video |
| [`code/schedule_if.py`](code/schedule_if.py) | Program from the video |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

Files in `code/mistakes/` are the mistakes shown in the video. They are meant to fail, so you can see the error for yourself.

---
Part of [Python and AI](../README.md) by A Bit Clearer.
