# Episode 04 · Your First Python Program

*Getting Started*

Run Python two ways, one line at a time at the >>> prompt, or as a program saved in a .py file, and fix the three mistakes that trip up almost every beginner.

**Notes:** [04-your-first-python-program.pdf](04-your-first-python-program.pdf) (colour PDF, A4)

## Key points

- At the **>>>** prompt, each line runs as soon as you press Enter. `print("Hello World")` shows text on screen.
- Use **straight quotes** and a lowercase **print**. Curly quotes and `Print` both stop with an error.
- Save a program as a **.py** file and run it with `python hello.py` **from the folder the file is in**.
- The terminal finds `python` by searching the folders in **PATH**, top to bottom. The first match wins.

## Code

| File | What it is |
|---|---|
| [`code/hello.py`](code/hello.py) | Program from the video |
| [`code/mistakes/capital_print.py`](code/mistakes/capital_print.py) | Mistake example, stops with an error on purpose: Python is case sensitive, so Print is not print. |
| [`code/mistakes/curly_quotes.py`](code/mistakes/curly_quotes.py) | Mistake example, stops with an error on purpose: curly quotes from a word processor are not valid Python. |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

Files in `code/mistakes/` are the mistakes shown in the video. They are meant to fail, so you can see the error for yourself.

---
Part of [Python and AI](../README.md) by A Bit Clearer.
