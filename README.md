# Uncommon Python Bug: Empty List Average Calculation

This repository demonstrates a subtle bug that can occur when calculating the average of a list in Python, specifically when the input list is empty.  The bug lies in not explicitly handling the case of an empty list, which can lead to a `ZeroDivisionError`.

## The Bug

The `bug.py` file contains a function `calculate_average` that calculates the average of a list of numbers. However, it does not correctly handle the case where the input list is empty.  This leads to a `ZeroDivisionError` because the code attempts to divide by zero.

## The Solution

The `bugSolution.py` file provides a corrected version of the `calculate_average` function. This improved version includes a check to see if the list is empty. If it is, it returns 0 (or alternatively, it could raise a more informative exception).

This demonstrates the importance of considering edge cases and thoroughly testing your code to prevent unexpected errors.