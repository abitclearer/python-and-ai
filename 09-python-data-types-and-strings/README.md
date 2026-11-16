# Episode 09 · Python Data Types and Strings

*type(), isinstance(), Quotes, Escapes, + and f-strings*

How to ask Python for the type of a value, the three ways to write a string, escape characters, and three ways to put your own data into text.

**Notes:** [09-python-data-types-and-strings.pdf](09-python-data-types-and-strings.pdf) (colour PDF, A4)

## Key points

- Five basic types: **`int`**, **`float`**, **`str`**, **`bool`**, **`NoneType`**. **`type(x)`** tells you the type; **`isinstance(x, int)`** answers with `True` or `False`.
- **Variables don't have types; values do.** The same variable can hold an `int` now and a `str` later.
- Strings use **single**, **double** or **triple** quotes (triple = several lines). A **backslash** escapes a quote; **`\n`** is a new line, **`\t`** a tab.
- **`+`** joins strings with strings only (use **`str()`** for numbers). **`%s`** fills placeholders in order. **f-strings** put variables right inside the text: `f"Hi, {name}"`.

## Code

| File | What it is |
|---|---|
| [`code/join_format.py`](code/join_format.py) | Program from the video |
| [`code/mistakes/missing_value.py`](code/mistakes/missing_value.py) | Mistake example, stops with an error on purpose: there are four %s placeholders but only three values. |
| [`code/mistakes/no_f.py`](code/mistakes/no_f.py) | Mistake example |
| [`code/mistakes/plus_number.py`](code/mistakes/plus_number.py) | Mistake example, stops with an error on purpose: + cannot join a number (int) to a string. |
| [`code/mistakes/quote_inside.py`](code/mistakes/quote_inside.py) | Mistake example, stops with an error on purpose: the apostrophe in It's ends the single-quoted string early. |
| [`code/strings.py`](code/strings.py) | Program from the video |
| [`code/types.py`](code/types.py) | Program from the video |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

Files in `code/mistakes/` are the mistakes shown in the video. They are meant to fail, so you can see the error for yourself.

---
Part of [Python and AI](../README.md) by A Bit Clearer.
