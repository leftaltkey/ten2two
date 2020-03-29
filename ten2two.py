import sys


def largest_power_of_two(value):
    '''
    Finds the largest power of two that is less than
    the input value
    '''
    i = 0
    while True:
        i += 1
        if 2**i > value:
            return i-1


class Base2:
    '''
    Holds a base 2 data type.
    Access through `value`.
    '''
    def __init__(self, value=0):
        self.value = value

    def add(self, power_of_2:int):
        self.value = self.value + 10**power_of_2


def ten2two(num10:int):
    '''
    Converts the input argument from base 10 to base 2
    returns the base 2 value
    '''
    num2 = Base2()
    rem = num10

    while rem > 0:
        base2_pow = largest_power_of_two(rem)
        num2.add(base2_pow)
        rem = rem - 2**base2_pow

    return num2.value


num10 = int(sys.argv[1])
print('The base 10 value is: {}'.format(num10))

num2 = ten2two(num10)
print('The base  2 value is: {}'.format(num2))