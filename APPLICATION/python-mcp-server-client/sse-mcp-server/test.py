#!/usr/bin/env python3
"""
Test script for the MCP server tools.
"""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the tools
from web.AppWeb import add_numbers, subtract_numbers, multiply_numbers, divide_numbers, compare_numbers

def test_add_numbers():
    result = add_numbers(5, 3)
    expected = "8"
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ add_numbers test passed")

def test_subtract_numbers():
    result = subtract_numbers(10, 4)
    expected = "6"
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ subtract_numbers test passed")

def test_multiply_numbers():
    result = multiply_numbers(6, 7)
    expected = "42"
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ multiply_numbers test passed")

def test_divide_numbers():
    result = divide_numbers(20, 4)
    expected = "5.0"
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ divide_numbers test passed")

def test_divide_by_zero():
    result = divide_numbers(10, 0)
    expected = "Error: Cannot divide by zero."
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ divide_by_zero test passed")

def test_compare_numbers():
    # Test greater
    result = compare_numbers(10, 5)
    expected = "10 is greater than 5."
    assert result == expected, f"Expected {expected}, got {result}"

    # Test lesser
    result = compare_numbers(3, 8)
    expected = "8 is greater than 3."
    assert result == expected, f"Expected {expected}, got {result}"

    # Test equal
    result = compare_numbers(7, 7)
    expected = "Both numbers are equal."
    assert result == expected, f"Expected {expected}, got {result}"

    print("✓ compare_numbers test passed")

def main():
    print("Testing MCP server tools...")
    print()

    try:
        test_add_numbers()
        test_subtract_numbers()
        test_multiply_numbers()
        test_divide_numbers()
        test_divide_by_zero()
        test_compare_numbers()

        print()
        print("All tests passed! ✓")

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()