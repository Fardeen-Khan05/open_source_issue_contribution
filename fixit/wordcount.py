"""Word, line and character counting."""

import re


def count_words(text: str) -> int:
    """Count the words in the given text.

    Example:
        count_words("hello world") returns 2.
        count_words("one two three") returns 3.
    """
    return len(re.split(r'\s+', text.strip()))


def count_lines(text: str) -> int:
    """Count the lines in the given text.

    Example:
        count_lines("hello\nworld") returns 2.
        count_lines("hello") returns 1.
    """
    return len(text.split("\n"))


def count_chars(text: str) -> int:
    """Count the characters in the given text.

    Example:
        count_chars("hello") returns 5.
        count_chars("hi!") returns 3.
    """
    return len(text)
