import pytest
from fixit.textutils import is_palindrome, reverse_words, slugify


def test_simple_palindrome():
    assert is_palindrome("level")


@pytest.mark.xfail(reason="Known bug: case-sensitive")
def test_palindrome_ignores_case():
    assert is_palindrome("Level")


@pytest.mark.xfail(reason="Known bug: spaces and punctuation are not ignored")
def test_palindrome_ignores_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama")


def test_reverse_words_extra_spaces():
    assert reverse_words("hello   world") == "world hello"

def test_slugify_basic():
    assert slugify("Hello World!") == "hello-world"


def test_slugify_punctuation_and_spaces():
    assert slugify("Open Source, Project!") == "open-source-project"