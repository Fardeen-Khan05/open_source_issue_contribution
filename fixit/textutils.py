"""Small text helpers."""


def is_palindrome(text: str) -> bool:
    """Check whether text reads the same forwards and backwards.

    Example:
        is_palindrome("madam") returns True.
        is_palindrome("hello") returns False.
    """
    return text == text[::-1]


def reverse_words(text: str) -> str:
    """Reverse the order of words in text.

    Example:
        reverse_words("hello world") returns "world hello".
    """
    return " ".join(reversed(text.split()))

    
def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug.

    Example:
        slugify("Hello World!") returns "hello-world".
    """
    import re

    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")