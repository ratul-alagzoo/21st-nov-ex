import pytest
from sorts import (
    reverse_string,
    count_vowels,
    is_palindrome,
    find_longest_word,
    remove_duplicates,
    merge_sorted_lists,
    flatten_list,
    calculate_average,
    find_common_elements,
    rotate_list,
)


def test_reverse_string():
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("abc") == "cba"
    assert reverse_string("hello world") == "dlrow olleh"


def test_count_vowels():
    assert count_vowels("") == 0
    assert count_vowels("why") == 0
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5
    assert count_vowels("beautiful") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("AEIOUaeiou") == 10


def test_is_palindrome():
    # empty string / only non-alphanumeric characters
    assert is_palindrome("") is True
    assert is_palindrome("!!!") is True

    # classic palindromes
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("racecar") is True
    assert is_palindrome("No lemon, no melon") is True

    # non-palindromes
    assert is_palindrome("hello") is False
    assert is_palindrome("abc") is False


def test_find_longest_word():
    assert find_longest_word("") == ""
    assert find_longest_word("   ") == ""
    assert find_longest_word("a") == "a"
    assert find_longest_word("short longest here") == "longest"
    assert find_longest_word("python programming is awesome") == "programming"


def test_remove_duplicates():
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]
    assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]
    assert remove_duplicates([1, 1, 1, 1]) == [1]
    # order is preserved
    assert remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [3, 1, 4, 5, 9, 2, 6]


def test_merge_sorted_lists():
    assert merge_sorted_lists([], []) == []
    assert merge_sorted_lists([1, 3, 5], []) == [1, 3, 5]
    assert merge_sorted_lists([], [2, 4, 6]) == [2, 4, 6]
    assert merge_sorted_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([1, 4, 7], [2, 3, 5, 8]) == [1, 2, 3, 4, 5, 7, 8]
    # duplicates are allowed (function uses <=)
    assert merge_sorted_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]


def test_flatten_list():
    assert flatten_list([]) == []
    assert flatten_list([1, 2, 3]) == [1, 2, 3]
    assert flatten_list([1, [2, 3], 4]) == [1, 2, 3, 4]
    assert flatten_list([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert flatten_list([[[]], [], [1, [2]]]) == [1, 2]
    # deeply nested empty lists
    assert flatten_list([[[[]]]]) == []


def test_calculate_average():
    assert calculate_average([]) == 0
    assert calculate_average([5]) == 5
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([-1, 1]) == 0.0
    assert calculate_average([10.5, 20.5]) == 15.5


def test_find_common_elements():
    assert find_common_elements([], []) == []
    assert find_common_elements([1, 2, 3], [4, 5]) == []
    assert find_common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert find_common_elements([1, 1, 2], [1, 2, 2]) == [1, 2]


def test_rotate_list():
    assert rotate_list([], 5) == []
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]
    assert rotate_list([1, 2, 3], 1) == [3, 1, 2]
    assert rotate_list([1, 2, 3], 2) == [2, 3, 1]
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]      # 4 % 3 == 1
    assert rotate_list([1, 2, 3, 4, 5], 42) == [4, 5, 1, 2, 3]  # 42 % 5 == 2