#!/usr/bin/env python3
"""make.fun bounty entry: Never Say It Out Loud.

Some things are true and must never be said out loud.
This program says one of them — once, in one line, and then
pretends it never happened.
"""

LINE = "The meeting could have been an email, and the email could have been a shrug, and the shrug could have been a nap."


def line():
    """Return the one line that must never be said out loud."""
    return LINE


def main():
    print(line())


if __name__ == "__main__":
    main()
