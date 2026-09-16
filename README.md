# Lab: Linked Lists and Recursion
**Completed Sept 16, 2026**

## Overview

This project implements a singly linked list of integer IDs with recursive
operations for summing, reversing, and searching the list, built as a small
prototype for managing something like an employee ID roster.

## Project structure

- `linked_list.py`→ `Node` and `LinkedList` classes
- `main.py`→ demonstrates creating a list, inserting data, and running each
  recursive operation
- `tests/test_linked_list.py`→ provided test suite

## How to run

1. (Optional) Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
```
2. Install test dependencies:
```bash
   pip install pytest
```
3. Run the demo:
```bash
   python3 main.py
```
4. Run the test suite:
```bash
   python3 -m pytest tests/test_linked_list.py
```

## Implementation notes

- **`insert_at_front(data)`** → O(1) insertion at the head.
- **`insert_at_end(data)`** → O(n), traverses to the last node before linking
  the new one.
- **`recursive_sum()`** → base case returns `0` at `None`; each call adds its
  node's `data` to the recursive sum of the rest of the list.
- **`recursive_search(target)`** → base cases are `None` (not found, `False`)
  or a matching node (`True`); otherwise it recurses on `next`.
- **`recursive_reverse()`** → walks the list with two pointers (`prev` and
  `current`), flipping each node's `next` to point backward, until `current`
  is `None`; `prev` becomes the new head.

## Interpreting output

Running `main.py` prints:
- The list contents after insertion, formatted as `val -> val -> ... -> None`
- The sum of all node values
- The result of two searches (one for a value that exists, one that does not)
- The list contents again after being reversed, to visually confirm the
  reverse worked

Running the test suite prints a pass or fail count for each test in
`tests/test_linked_list.py`. A successful run ends with something like
`5 passed`, confirming `Node`, `LinkedList`, and each recursive method behave
as expected.