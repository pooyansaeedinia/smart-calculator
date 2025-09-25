# Calculator Project

**A multifunctional command-line calculator written in Python.**

This project provides an interactive terminal-based calculator with extended features: arithmetic operations, BMI calculation, length conversions, geometric area/perimeter/volume calculations, and persistent history tracking using SQLite.

---

## Table of Contents
- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Database & History](#database--history)
- [Development](#development)
- [License](#license)

---

## About
This is an **all-in-one calculator CLI tool** built in Python. Unlike a simple calculator, it allows you to:
- Perform arithmetic operations (addition, subtraction, multiplication, division, powers, radicals).
- Calculate **BMI** interactively with classification (underweight, normal, overweight, etc.).
- Convert **length units** (cm, m, mm, km, miles).
- Calculate **area, perimeter, and volume** for common shapes (square, rectangle, triangle, circle, cube, sphere, cylinder, etc.).
- Store calculation history in an **SQLite database** and review or delete it later.

The program runs entirely in the terminal with interactive menus.

---

## Features
- **Arithmetic operations**: +, -, ×, ÷, power, square root.
- **BMI Calculator**: interactive with validation.
- **Length Converter**: supports cm, m, mm, km, and miles.
- **Area calculations**: square, rectangle, triangle, rhomboid, parallelogram, trapezium, circle.
- **Perimeter calculations**: square, rectangle, triangle, rhomboid, parallelogram, trapezium, circle.
- **Volume calculations**: cube, sphere, hemisphere, cylinder, cone.
- **History management**:
  - Stores all operations in `history.db` (SQLite)
  - Retrieve history by category (operation, area, perimeter, volume)
  - Delete histories individually.

---

## Requirements
- Python 3.8+
- Standard library modules only:
  - `sqlite3`
  - `time`
  - `os`
  - `math`

No external dependencies required.

---

## Usage
When you run the program, you’ll see a **home menu** with options:

```text
home menu
what is your request?
1-operation menu
2-apv menu
3-bmi menu
4-length menu
5-history menu
0-exit
```

Choose a menu by entering its number. For example:

- Enter 1 → arithmetic operations

- Enter 2 → area/perimeter/volume

- Enter 3 → BMI calculator

- Enter 4 → length conversion

- Enter 5 → view or manage history

- Enter 0 → exit program

## Examples
1. Arithmetic operation (sum):
```text
  enter your first number: 5
  enter your second number: 7
     5 + 7 = 12
```




## Installation
Clone the repository and run the calculator directly:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
