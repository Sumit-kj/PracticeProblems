"""
Given an array Arr[] of size N, print all the subsets of the array.

Subset: A subset of an array is a tuple that can be obtained from the array by removing some (possibly all) elements of
it

Input: N = 3, Arr = [1, 2, 3]
Output: {}
               {1}
               {1, 2}
               {1, 2, 3}
               {1, 3}
               {2}
               {2, 3}
               {3}
Explanation: These are all the subsets that can be formed from the given array, it can be proven that no other subset
exists other than the given output.


Input: N = 2, Arr = [2, 4]
Output: {}
               {2}
               {2, 4}
               {4}
Explanation: These are all the subsets that can be formed from the given array, it can be proven that no other subset
exists other than the given output.
"""
from src.res.Backtracking.letter_combination_keypad_phone import input as ip, output as op
import validator


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(letter_combination_keypad_phone(n))
    print(results)

    if not validator.are_two_arrays_same(op.o_p, results):
        print()
        print('Wrong answer')
        print('Expected output pattern:', op.o_p)
        print('Your output:', results)


def letter_combination_keypad_phone(digits):
    """
    This function returns the possible text that can be composed using these digits on keypad
    :param digits: The string with all the digits pressed in order
    :return: The list of all possible texts that can be sent using the keypad digits
    """
    if len(digits) == 0:
        return []
    digit_letters = []
    for digit in digits:
        letters = get_letters_from_digits(int(digit))
        digit_letters.append(letters)
    result = digit_letters[0]
    for i in range(1, len(digits)):
        inter = result
        result = []
        for j in inter:
            for k in digit_letters[i]:
                result.append(j + k)
    return result


def get_letters_from_digits(digit):
    digit_letter_map = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }
    if digit not in digit_letter_map.keys():
        return []
    return digit_letter_map[digit]
