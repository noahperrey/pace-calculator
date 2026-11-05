# Pace Calculator

A simple tool for runners that calculates distance, pace or finish time from the other two values.

## Getting Started

Requires Python 3.

```bash
python3 main.py
```

## Example

```
What would you like to have calculated?
1 for Distance
2 for Pace
3 for Finish Time
4 to end the program: 2
Please enter your distance (e.g. 42,2): 10
Please enter your finish time (e.g. 01:30): 0:57
05:42 min
```

## What I Learned

- Planning a small project on paper before writing code
- Splitting a program into small, testable functions
- Converting between strings and numbers (`split`, `replace`, `float`, `int`, `round`)
- Using `//` and `%` to convert minutes into hours and minutes
- Checking user input with a `while` loop
- Formatting numbers with f-strings (e.g. leading zeros)
- Writing docstrings and type hints
- Using Git and GitHub with small commits

## Ideas for Future Versions

- Handle invalid input formats (e.g. `5.30` instead of `5:30`)
- Support miles
- Graphical user interface

## Status

Version 1 finished (2026-11)
