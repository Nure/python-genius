# FizzBuzz Checker - User Input Challenge

## Overview

In this exercise, the user will enter a number, and the program will check whether that number should be classified as:

- `Fizz`
- `Buzz`
- `FizzBuzz`
- Or simply the number itself

This exercise is useful for practicing:

- `input()`
- Type conversion with `int()`
- `if`, `elif`, and `else`
- The modulo operator `%`

---

## Problem Statement

Write a Python program that asks the user to enter a number.

Example:

```text
Enter a number: 15
```

The program should then check the number using the following rules:

- If the number is divisible by both `3` and `5`, print:

```text
FizzBuzz
```

- If the number is divisible by `3`, print:

```text
Fizz
```

- If the number is divisible by `5`, print:

```text
Buzz
```

- Otherwise, print the number itself.

---

## Example 1

### Input

```text
Enter a number: 9
```

### Output

```text
Fizz
```

---

## Example 2

### Input

```text
Enter a number: 10
```

### Output

```text
Buzz
```

---

## Example 3

### Input

```text
Enter a number: 15
```

### Output

```text
FizzBuzz
```

---

## Example 4

### Input

```text
Enter a number: 7
```

### Output

```text
7
```

---

## Requirements

Your program should:

1. Ask the user to enter a number.
2. Convert the user input into an integer.
3. Check whether the number is divisible by both `3` and `5`.
4. Check whether it is divisible by only `3`.
5. Check whether it is divisible by only `5`.
6. Print the number if none of the conditions match.

---

## Starter Code

Use the following code as a starting point:

```python
number = int(input("Enter a number: "))

# Add your FizzBuzz logic here
```

---

## Hint

You can check divisibility using the modulo operator:

```python
number % 3 == 0
```

For example:

```python
12 % 3 == 0
```

returns:

```text
True
```

To check whether a number is divisible by both `3` and `5`, you can combine two conditions using `and`.

---

## Important

Think carefully about the order of your conditions.

For example, `15` is divisible by both `3` and `5`.

If you check divisibility by `3` first, your program may incorrectly print:

```text
Fizz
```

instead of:

```text
FizzBuzz
```

So the condition for divisibility by both numbers should be checked first.

---

## Bonus Challenge

Add input validation so the program does not crash when the user enters something that is not a number.

For example:

```text
Enter a number: hello
```

Instead of crashing, the program could display:

```text
Please enter a valid integer.
```

---

## Learning Objectives

After completing this exercise, you should understand:

- How to accept user input in Python
- How to convert a string into an integer
- How to use the `%` operator
- How to combine conditions
- Why condition order matters
