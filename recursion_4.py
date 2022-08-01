"""
Сhecking if a string is a palindrome.
"""


def palindrome(word) -> bool:
    """
    :param word: word to be tested
    :return: True of False
    """
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])
