# MYGITHUB

A small collection of Python example utilities and beginner projects.

## Overview

- `python/math_example/` — small math-related scripts: `big.py`, `evenorodd.py`, `grade.py`, `negpos.py`.
- `python/money_splitter/` — simple CLI app `app.py` for splitting bills; includes `export.json` sample data.
- `python/surface-area-calculator/` — small calculator app `app.py` for computing surface areas.

## Requirements

- Python 3.7+ (3.8 or newer recommended)
- No external dependencies unless a subproject adds them (none in this repo by default).

## Running the examples

Open a terminal at the repository root and run the desired script. Example commands:

```bash
python3 python/math_example/big.py
python3 python/math_example/evenorodd.py
python3 python/math_example/grade.py
python3 python/math_example/negpos.py

python3 python/money_splitter/app.py
python3 python/surface-area-calculator/app.py
```

Some scripts may prompt for input or include example calls inside the file. Inspect the source files for specific usage and sample inputs.

## What each script does

- `python/math_example/big.py` — attempts to determine the largest, second-largest and smallest of three numbers (script contains a "not working properly" note and may have bugs).
- `python/math_example/evenorodd.py` — prompts for a number and prints whether it is even or odd.
- `python/math_example/grade.py` — prompts for a numeric score and prints a textual grade (e.g. "Excellent", "Very Good", "Good", "Faild").
- `python/math_example/negpos.py` — prompts for a number and reports whether it is positive, negative, or zero.
- `python/money_splitter/app.py` — interactive CLI that breaks an integer amount into banknotes (100, 50, 20, 10, 5, 2, 1), shows a table using `rich`, and writes the breakdown to `python/money_splitter/export.json`. The script prints an author header (`Denis Varga`).
- `python/surface-area-calculator/app.py` — interactive surface-area calculator supporting at least Cube and Cuboid; prompts for dimensions and prints the result.

## Authorship

All scripts in this repository were created by the repository owner (Denis Varga). If you want to attribute differently, update the file headers or add per-project `README.md` files.

## Project structure

```
readme.md
python/
	math_example/
		big.py
		evenorodd.py
		grade.py
		negpos.py
	money_splitter/
		app.py
		export.json
	surface-area-calculator/
		app.py
```

## Contributing

Feel free to open PRs that add tests, better CLI options, or packaging (e.g., `requirements.txt` or `pyproject.toml`).

## License

This repository has no license specified. Add a `LICENSE` file if you want to make the code reusable under a specific license.

