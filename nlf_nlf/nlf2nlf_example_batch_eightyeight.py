

import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_eightyeight_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        example = __get_batch_two_example_pair((None if identifier is None else identifier + i))
        examples.append({"inputStr": example[0], "outputStr": example[1]})
    return examples


def __get_batch_two_example_pair(identifier: int | None):
    random_list = RandomValueGenerator.generate_random_list()
    lst_str = " , ".join(str(num) for num in random_list)
    random_int_one = RandomValueGenerator.generate_random_integer()
    random_int_two = random_int_one + RandomValueGenerator.generate_random_integer()
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer()
    random_int_four = RandomValueGenerator.generate_random_integer()
    random_float = RandomValueGenerator.generate_random_float()
    random_arc_int = RandomValueGenerator.generate_random_integer(-1, 1)
    random_degree = round(random.uniform(0, 2 * 3.14159), 1)
    str1 = RandomValueGenerator.generate_random_string()

    examples = [
        (
            f"descending_sort({random_list})",
            f"The descending sorted list of numbers {lst_str} is  ##descending_sort({random_list})",
        ),
        (
            f"square_int({random_int_two})",
            f"The square of {random_int_two} is ##square_int({random_int_two})",
        ),
        (
            f"square({random_float})",
            f"The square of a random value is ##square({random_float})",
        ),
        (
            f"abs({random_float})",
            f"The absolute value of a random number is ##absolute({random_float})",
        ),
        (
            f"10**{random_int_one}",
            f"10 to the power of {random_int_one} is ##power_of_ten({random_int_one})",
        ),
        (
            f"{random_float}**3",
            f"The cube of a random value is ##cube({random_float})",
        ),
        (
            f"cbrt({random_int_four})",
            f"The cube root of {random_int_four} is ##cube_root({random_int_four})",
        ),
        (
            f"is_even({random_int_two})",
            f"Checking if {random_int_two} is an even number is ##is_even({random_int_two})",
        ),
        (
            f"is_odd({random_int_three})",
            f"Checking if {random_int_three} is an odd number is ##is_odd({random_int_three})",
        ),
        (
            f"max_value([{random_list}])",
            f"The maximum value in the numbers {lst_str} is ##max_value([{random_list}])",
        ),
        (
            f"min_value([{random_list}])",
            f"The minimum value in the numbers {lst_str} is ##min_value([{random_list}])",
        ),
        (
            f"nth_root({random_int_two},{random_int_one})",
            f"The {random_int_one}-th root of {random_int_two} is ##nth_root({random_int_two},{random_int_one})",
        ),
        (
            f"geometric_mean([{random_list}])",
            f"The geometric mean of the numbers {lst_str} is ##geometric_mean([{random_list}])",
        ),
        (
            f"is_power_of_two({random_int_two})",
            f"Checking if {random_int_two} is a power of two is ##is_power_of_two({random_int_two})",
        ),
        (
            f"binary_to_decimal('1101')",
            f"The decimal equivalent of the binary number '1101' is ##binary_to_decimal('1101')",
        ),
        (
            f"decimal_to_binary({random_int_one})",
            f"The binary representation of the decimal number {random_int_one} is ##decimal_to_binary({random_int_one})",
        ),
        (
            f"is_palindrome('level')",
            f"Checking if the string 'level' is a palindrome is ##is_palindrome('level')",
        ),
        (
            f"sum_of_digits({random_int_four})",
            f"The sum of the digits in {random_int_four} is ##sum_of_digits({random_int_four})",
        ),
        (
            f"circle_area({random_float})",
            f"The area of a circle with radius {random_float} is ##circle_area({random_float})",
        ),
        (
            f"permutation({random_int_four},{random_int_two})",
            f"The permutation of {random_int_four} items taken {random_int_two} at a time is ##permutation({random_int_four},{random_int_two})",
        ),
        (
            f"combination({random_int_three},{random_int_one})",
            f"The combination of {random_int_three} items taken {random_int_one} at a time is ##combination({random_int_three},{random_int_one})",
        ),
        (
            f"invert_number({random_int_four})",
            f"The inversion of the number {random_int_four} is ##invert_number({random_int_four})",
        ),
        (
            f"float_to_int({random_float})",
            f"The conversion of a float to an integer is ##float_to_int({random_float})",
        ),
        (
            f"int_to_float({random_int_two})",
            f"The conversion of an integer to a float is ##int_to_float({random_int_two})",
        ),
        (
            f"sigmoid({random_float})",
            f"The sigmoid function value for {random_float} is ##sigmoid({random_float})"
        ),
        (
            f"euler_totient({random_int_one})",
            f"The Euler totient function value for {random_int_one} is ##euler_totient({random_int_one})"
        ),
        (
            f"l1_norm({random_list})",
            f"The L1 norm of the vector {lst_str} is ##l1_norm({random_list})"
        ),
        (
            f"l2_norm({random_list})",
            f"The L2 norm of the vector {lst_str} is ##l2_norm({random_list})"
        ),
        (
            f"average({random_list})",
            f"The average of {lst_str} is ##average({random_list})"
        ),
        (
            f"sum({random_list})",
            f"The sum of {lst_str} is ##sum({random_list})"
        ),
        (
            f"length({random_list})",
            f"The length of the vector {lst_str} is ##length({random_list})"
        ),
        (
            f"reverse_string('{str1}')",
            f"The reverse of the string '{str1}' is ##reverse_string('{str1}')"
        ),
        (
            "get_pi()",
            "The value of pi is ##get_pi()"
        ),
        (
            "get_e()",
            "The value of e is ##get_e()"
        ),
        (
            f"a_plus_b_whole_square({random_int_one}, {random_int_two})",
            f"The square of the sum of {random_int_one} and {random_int_two} is ##a_plus_b_whole_square({random_int_one}, {random_int_two})"
        ),
        (
            f"a_minus_b_whole_squared({random_int_one}, {random_int_two})",
            f"The square of the difference of {random_int_one} and {random_int_two} is ##a_minus_b_whole_squared({random_int_one}, {random_int_two})"
        ),
        (
            f"a_squared_plus_b_squared({random_int_one}, {random_int_two})",
            f"The sum of {random_int_one} squared and {random_int_two} squared is ##a_squared_plus_b_squared({random_int_one}, {random_int_two})"
        ),
        (
            f"negative_2ab({random_int_one}, {random_int_two})",
            f"Negative 2 times {random_int_one} times {random_int_two} is ##negative_2ab({random_int_one}, {random_int_two})"
        ),
        (
            f"positive_2ab({random_int_one}, {random_int_two})",
            f"Positive 2 times {random_int_one} times {random_int_two} is ##positive_2ab({random_int_one}, {random_int_two})"
        ),
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_eightyeight_example(2, None), TaskTypes.NL_TO_NL_TRANSLATION
        )

    )


