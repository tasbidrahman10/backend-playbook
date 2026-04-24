# 01 - Language Core

You already know Python basics, so this phase is not about syntax memorization. The goal is to understand how Python behaves as a runtime and how to build small, reliable tools with it.

## Goal
Learn Python from the inside out by implementing tiny components that expose its data model, iteration model, module system, and core standard-library patterns.

## What to implement

### 1. Python data model lab
Build a small object model that uses the core dunder methods intentionally.

Implement:
- A `User` or `Task` class with `__init__`, `__repr__`, `__str__`, `__eq__`, and ordering if useful
- Hashable vs unhashable object experiments
- A value object that behaves correctly in sets and dictionaries
- `@property` for computed attributes
- `__slots__` experiments to understand memory and attribute behavior

What this teaches:
- Objects, identity, equality, mutability, and how Python stores behavior on classes

### 2. Iteration and generators lab
Build your own iterable utilities instead of just using built-ins.

Implement:
- A custom iterable class with `__iter__` and `__next__`
- Generator-based data pipelines
- Lazy file or log readers
- A small `chunked`, `flatten`, or `window` helper
- A simple paginator over a list or file

What this teaches:
- Iterators, generators, lazy evaluation, and memory-friendly processing

### 3. Decorators and wrappers lab
Wrap functions the way production Python code does.

Implement:
- A timing decorator
- A retry decorator with exponential backoff
- A cache decorator for pure functions
- A decorator that logs calls and arguments
- `functools.wraps` usage

What this teaches:
- Higher-order functions, closures, metadata preservation, and cross-cutting behavior

### 4. Context manager lab
Manage setup and cleanup the Python way.

Implement:
- A custom context manager with `__enter__` and `__exit__`
- A `contextlib.contextmanager` version of the same tool
- A file/session/resource wrapper that always cleans up
- A transaction-like demo that rolls back on failure

What this teaches:
- Resource management, exception flow, and safe cleanup

### 5. Modules and packaging lab
Learn how Python code is organized and imported.

Implement:
- A small multi-module package
- Relative vs absolute imports
- `__init__.py` behavior
- A command-line entry point with `argparse`
- A `pyproject.toml`-based installable package, even if minimal

What this teaches:
- Import mechanics, package structure, and how real projects are arranged

### 6. Error handling and logging lab
Make failures explicit and debuggable.

Implement:
- Custom exception classes
- A validation layer that raises domain errors
- A consistent error format for CLI output
- Logging setup with levels and structured messages

What this teaches:
- Control flow through exceptions and practical observability for small tools

### 7. Testing and debugging lab
Lock behavior down as you build.

Implement:
- Unit tests for your small helpers
- Parameterized tests for edge cases
- Mocking or patching for external dependencies
- A tiny integration test for your CLI or package

What this teaches:
- How to prove your code works and catch regressions early

### 8. Async basics lab
Only after the above feels natural, touch async.

Implement:
- A tiny `asyncio` script
- Concurrent HTTP requests or simulated I/O tasks
- An async producer/consumer example

What this teaches:
- Event loop thinking and when async is actually useful

## Recommended build sequence
1. Data model lab
2. Iteration and generators lab
3. Decorators and wrappers lab
4. Context manager lab
5. Modules and packaging lab
6. Error handling and logging lab
7. Testing and debugging lab
8. Async basics lab

## Output
By the end of this phase, you should have a small set of Python implementations you can rebuild without looking at notes, plus one package-like project that feels like a real codebase.

## Rule for this phase
If a concept can be implemented in 30 to 90 lines of Python, implement it instead of only reading about it.
