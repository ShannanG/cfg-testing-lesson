
"""
This is a possible interview coding question. Let's check the task,
implement our solution and then write tests for it:

Task
Given an integer x perform the following conditional actions:

If x is odd, return 'Red'
If x is even and in the inclusive range of 2 to 5, return 'Blue'
If x is even and in the inclusive range of 6 to 20, return 'Red'
If x is even and greater than 20, return 'Blue'

Constraint notes:
an input integer is always withing the range 1 to 100 inclusive
"""
def is_within_range(num, _min, _max):
    if _min <= num <= _max:
        return True
    return False
'''

Use each of these once to complete the is_within_range function

'''


def is_even(num):
    return num % 2 == 0

#
def red_or_blue(num):
    if not is_even(num) or (is_even(num) and is_within_range(num, 6, 20)):
        return 'Red'

    if (is_even(num) and num > 20) or num in [2, 4]:
        return 'Blue'


'''
Use each of these once to complete the red_or_blue function

'''

# # # 4 should return 'blue'
# print(red_or_blue(4))
# # 101 should return False because it's out of range
# #print(is_within_range(101, 1, 100))
# # # 68 should return 'blue'
# print(red_or_blue(68))
# # and 17 should return 'red'
print(red_or_blue(17))
