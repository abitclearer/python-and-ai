# Episode 10 · Python Input and Type Conversion

*input(), Strings from the Keyboard, int(), float() and bool()*

How to read what the user types with input(), why it always comes back as a string, and how to turn it into a number with int() or float().

**Notes:** [10-python-input-and-type-conversion.pdf](10-python-input-and-type-conversion.pdf) (colour PDF, A4)

## Key points

- **`input("prompt")`** shows the prompt, **waits** until the user presses Enter, and gives back what they typed.
- **`input()` always returns a string**, even when the user types a number. `"3" + "4"` is `"34"`, not `7`.
- **Convert before you do math:** `int(input(...))` for whole numbers, `float(input(...))` for decimals. `str()` turns values back into text.
- `int("3.5")` and `int("hello")` stop with a **`ValueError`**. `bool()` of any non-empty string is `True`, even `bool("False")`.

## Code

| File | What it is |
|---|---|
| [`code/add_as_text.py`](code/add_as_text.py) | Program from the video |
| [`code/add_numbers.py`](code/add_numbers.py) | Program from the video |
| [`code/atm.py`](code/atm.py) | Program from the video |
| [`code/conversions.py`](code/conversions.py) | Program from the video |
| [`code/hello_input.py`](code/hello_input.py) | Program from the video |
| [`code/mistakes/atm_no_int.py`](code/mistakes/atm_no_int.py) | Mistake example, stops with an error on purpose: amount is a string, and Python can't subtract a string from a number. |
| [`code/mistakes/int_decimal.py`](code/mistakes/int_decimal.py) | Mistake example, stops with an error on purpose: int can't read a decimal number written as text. Use float for that. |

Each program ends with a `# Output:` comment showing what it prints. To run one, install Python 3 from python.org,
then run `python <file>.py` in a terminal (on macOS and Linux: `python3 <file>.py`).

Files in `code/mistakes/` are the mistakes shown in the video. They are meant to fail, so you can see the error for yourself.

---
Part of [Python and AI](../README.md) by A Bit Clearer.
