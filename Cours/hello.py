#!/usr/bin/env python3
"""Ask the user's name and greet them."""
def greet(name):
    print("Hey, {}! I'm Python.".format(name))
def main():
    name = input("What is your name? ")
    greet(name)
if __name__ == '__main__':
    main()