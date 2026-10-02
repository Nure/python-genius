# FizzBuzz - Python Programming Challenge

## Overview

FizzBuzz is a classic programming exercise commonly used to practice:

- Loops
- Conditional statements
- Modulo (`%`) operator
- Basic Python syntax
- Problem-solving logic

The goal is to print a sequence of numbers while replacing certain numbers with specific words based on divisibility rules.

---

## Problem Statement

Write a Python program that prints the numbers from **1 to 100**.

For each number:

- If the number is divisible by **3**, print:

```text
Fizz
```

- If the number is divisible by **5**, print:

```text
Buzz
```

- If the number is divisible by **both 3 and 5**, print:

```text
FizzBuzz
```

- Otherwise, print the number itself.

---

## Example Output

The beginning of the output should look like this:

```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```

The program should continue until it reaches:

```text
100
```

---

## Requirements

Your program should:

1. Iterate through numbers from `1` to `100`.
2. Check whether each number is divisible by `3`, `5`, or both.
3. Print `FizzBuzz` when the number is divisible by both `3` and `5`.
4. Print `Fizz` when the number is divisible only by `3`.
5. Print `Buzz` when the number is divisible only by `5`.
6. Print the original number if none of the conditions match.

---

## Important Hint

Python's modulo operator `%` can be used to determine whether a number is divisible by another number.

Example:

```python
number % 3 == 0
```

This means that `number` is divisible by `3` without any remainder.

For example:

```python
6 % 3 == 0
```

returns:

```text
True
```

While:

```python
7 % 3 == 0
```

returns:

```text
False
```

---

## Suggested Program Structure

You may start with a loop like this:

```python
for number in range(1, 101):
    # Add your FizzBuzz logic here
```

Remember that:

```python
range(1, 101)
```

starts at `1` and stops before `101`, so the final number will be `100`.

---

## Challenge

Try solving the problem yourself before looking at a solution.

Think carefully about the order of your conditions.

For example, consider the number:

```text
15
```

It is divisible by both `3` and `5`.

Your program should print:

```text
FizzBuzz
```

instead of:

```text
Fizz
```

or:

```text
Buzz
```
