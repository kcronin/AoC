#!/usr/bin/env python3

import sys

def greet(name):
    """Print a greeting to the given name."""
    print(f"hello, {name}!")
    print("Nice to meet you.")

def goodbye(name):
    """Print a goodbye message to the given name."""
    print(f"goodbye, {name}!")
    print("See ya later, alligator!")

def ask_how_are_you():
    """Ask the user how they are doing and respond."""
    response = input("How are you doing today? ")
    print("cool.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        action = sys.argv[2] if len(sys.argv) > 2 else "greet"

        if action == "goodbye":
            goodbye(name)
        else:
            greet(name)
            ask_how_are_you()
    else:
        print("Please provide a name as an argument.")
        print("Usage: hello.py <name> [greet|goodbye]")
