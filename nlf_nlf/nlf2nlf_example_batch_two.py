import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_two_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        example = __get_batch_two_example_pair((None if identifier is None else identifier+i))
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
            f"If you have {random_int_one} groups and each group contains {random_int_four} items how many items do you have in total",
            f"You have ##multiplication({random_int_one},{random_int_four}) items in total",
        ),
        (
            f"You have {random_int_two} apples and {random_int_three} oranges how many fruits do you have altogether",
            f"The total number of fruits is ##addition({random_int_two},{random_int_three})",
        ),
        (
            f"If you have {random_int_three} dollars and spend {random_int_one} dollars how much money do you have left",
            f"The amount left after spending {random_int_one} dollars is ##subtraction({random_int_three},{random_int_one})",
        ),
        (
            f"If you have {random_int_two} pizzas and want to share them equally among {random_int_one} friends, how many pizzas will each friend get",
            f"Each friend will receive ##division({random_int_two},{random_int_one}) pizzas",
        ),
        (
            f"If you want to calculate the area of a rectangle with length {random_int_one} units and width {random_int_two} units, what is the total area",
            f"The area of the rectangle is ##exponentiation({random_int_one},{random_int_two})",
        ),
        (
            f"If you have a square plot of land with an area of {random_int_two} square meters what is the length of one side",
            f"The length of one side of the square plot is ##square_root({random_int_two})",
        ),
        (
            f"If you have {random_int_three} cookies and want to divide them into groups of {random_int_one} cookies each, how many full groups can you make",
            f"You can make ##floor_division({random_int_three},{random_int_one}) full groups of cookies",
        ),
        (
            f"If you have {random_int_four} apples and want to pack them into boxes of {random_int_two} apples each, how many apples will be left unpacked",
            f"The remainder of apples left unpacked is ##modulus({random_int_four},{random_int_two})",
        ),
        (
            f"If you want to find the logarithm of {random_int_three} to the base {random_int_one}, what is the result",
            f"The result of the logarithm is ##logarithm({random_int_three},{random_int_one})",
        ),
        (
            f"If you want to calculate the sine of an angle of {random_int_one} degrees, what is the sine value",
            f"The sine value of the angle is ##sine({random_int_one})",
        ),
        (
            f"If you want to calculate the cosine of an angle of {random_int_two} degrees, what is the cosine value",
            f"The cosine value of the angle is ##cosine({random_int_two})",
        ),
        (
            f"If you want to find the tangent of an angle of {random_int_three} degrees, what is the tangent value",
            f"The tangent value of the angle is ##tangent({random_int_three})",
        ),
        (
            f"If you want to find the arcsine of a random value, what is the arcsine value",
            f"The arcsine value of the random value is ##arcsine({random_arc_int})",
        ),
        (
            f"If you want to find the arccosine of a random value, what is the arccosine value",
            f"The arccosine value of the random value is ##arccosine({random_arc_int})",
        ),
        (
            f"If you want to find the arctangent of a random value, what is the arctangent value",
            f"The arctangent value of the random value is ##arctangent({random_arc_int})",
        ),
        (
            f"If you want to find the hyperbolic sine of {random_int_one}, what is the hyperbolic sine value",
            f"The hyperbolic sine value of {random_int_one} is ##hyperbolic_sine({random_int_one})",
        ),
        (
            f"If you want to find the hyperbolic cosine of {random_int_two}, what is the hyperbolic cosine value",
            f"The hyperbolic cosine value of {random_int_two} is ##hyperbolic_cosine({random_int_two})",
        ),
        (
            f"If you want to find the hyperbolic tangent of {random_int_three}, what is the hyperbolic tangent value",
            f"The hyperbolic tangent value of {random_int_three} is ##hyperbolic_tangent({random_int_three})",
        ),
        (
            f"If you want to find the base 10 logarithm of {random_int_three}, what is the result",
            f"The result of the base 10 logarithm is ##logarithm_base_10({random_int_three})",
        ),
        (
            f"If you want to find the base 2 logarithm of {random_int_two}, what is the result",
            f"The result of the base 2 logarithm is ##logarithm_base_2({random_int_two})",
        ),
        (
            f"If you have an angle of {random_degree} degrees, what is the equivalent value in radians",
            f"The conversion of {random_degree} degrees to radians is ##degrees_to_radians({random_degree})",
        ),
        (
            f"If you have an angle of {random_int_one} degrees, what is the equivalent value in radians",
            f"The conversion of {random_int_one} degrees to radians is ##radians_to_degrees({random_int_one})",
        ),
        (
            f"If you want to find the greatest common divisor of {random_int_one} and {random_int_two}, what is it",
            f"The greatest common divisor of {random_int_one} and {random_int_two} is ##gcd({random_int_one},{random_int_two})",
        ),
        (
            f"If you want to find the least common multiple of {random_int_three} and {random_int_four}, what is it",
            f"The least common multiple of {random_int_three} and {random_int_four} is ##lcm({random_int_three},{random_int_four})",
        ),
        (
            f"If you want to find the integer square root of {random_int_two}, what is it",
            f"The integer square root of {random_int_two} is ##isqrt({random_int_two})",
        ),
        (
            f"If you have a random value, what is the smallest integer greater than or equal to it",
            f"The ceiling of the random value is ##ceil({random_float})",
        ),
        (
            f"If you have a random value, what is the largest integer smaller than or equal to it",
            f"The floor of the random value is ##floor({random_float})",
        ),
        (
            f"If you have a random number, what is the closest integer to it",
            f"The rounded value of the random number is ##round({random_float})",
        ),
        (
            f"What is the absolute difference between {random_int_one} and {random_int_two}",
            f"The absolute difference between {random_int_one} and {random_int_two} is ##absolute_difference({random_int_one},{random_int_two})"
        ),
        (
            f"What is the greater value between {random_int_three} and {random_int_four}",
            f"The greater value between {random_int_three} and {random_int_four} is ##greatest_value({random_int_three},{random_int_four})"
        ),
        (
            f"What is the smaller value between {random_int_one} and {random_int_two}",
            f"The smaller value between {random_int_one} and {random_int_two} is ##smallest_value({random_int_one},{random_int_two})"
        ),
        (
            f"What is the product of the numbers {lst_str}",
            f"The product of the numbers {lst_str} is ##product({random_list})"
        ),
        (
            f"What is the factorial of {random_int_four}",
            f"The factorial of {random_int_four} is ##factorial({random_int_four})"
        ),
        (
            f"Is {random_int_two} a prime number",
            f"The primality check for {random_int_two} is ##is_prime({random_int_two})"
        ),
        (
            f"What are the prime factors of {random_int_three}",
            f"The prime factors of {random_int_three} are ##prime_factors({random_int_three})"
        ),
        (
            f"Is {random_int_four} a perfect square",
            f"Checking if {random_int_four} is a perfect square ##is_perfect_square({random_int_four})"
        ),
        (
            f"Is {random_int_one} a perfect cube",
            f"Checking if {random_int_one} is a perfect cube ##is_perfect_cube({random_int_one})"
        ),
        (
            f"What is the mean of the numbers {lst_str}",
            f"The mean of the numbers {lst_str} is ##mean({random_list})"
        ),
        (
            f"What is the median of the numbers {lst_str}",
            f"The median of the numbers {lst_str} is ##median({random_list})"
        ),
        (
            f"What is the rectified linear unit (ReLU) of a random value",
            f"The rectified linear unit (ReLU) of a random value is ##relu({random_float})"
        ),
        (
            f"What is the ascending sorted list of numbers {lst_str}",
            f"The ascending sorted list of numbers {lst_str} is ##ascending_sort({random_list})"
        ),
        (
            f"What is the descending sorted list of numbers {lst_str}",
            f"The descending sorted list of numbers {lst_str} is ##descending_sort({random_list})"
        ),
        (
            f"What is the square of {random_int_two}",
            f"The square of {random_int_two} is ##square_int({random_int_two})"
        ),
        (
            f"What is the square of a random value",
            f"The square of a random value is ##square({random_float})"
        ),
        (
            f"What is the absolute value of a random number",
            f"The absolute value of a random number is ##absolute({random_float})"
        ),
        (
            f"What is 10 to the power of {random_int_one}",
            f"10 to the power of {random_int_one} is ##power_of_ten({random_int_one})"
        ),
        (
            f"What is the cube of a random value",
            f"The cube of a random value is ##cube({random_float})"
        ),
        (
            f"What is the cube root of {random_int_four}",
            f"The cube root of {random_int_four} is ##cube_root({random_int_four})"
        ),
        (
            f"Is {random_int_two} an even number",
            f"Checking if {random_int_two} is an even number is ##is_even({random_int_two})"
        ),
        (
            f"Is {random_int_three} an odd number",
            f"Checking if {random_int_three} is an odd number is ##is_odd({random_int_three})"
        ),
        (
            f"What is the maximum value in the numbers {lst_str}",
            f"The maximum value in the numbers {lst_str} is ##max_value([{random_list}])"
        ),
        (
            f"What is the minimum value in the numbers {lst_str}",
            f"The minimum value in the numbers {lst_str} is ##min_value([{random_list}])"
        ),
        (
            f"What is the {random_int_one}-th root of {random_int_two}",
            f"The {random_int_one}-th root of {random_int_two} is ##nth_root({random_int_two},{random_int_one})"
        ),
        (
            f"What is the geometric mean of the numbers {lst_str}",
            f"The geometric mean of the numbers {lst_str} is ##geometric_mean([{random_list}])"
        ),
        (
            f"Is {random_int_two} a power of two",
            f"Checking if {random_int_two} is a power of two is ##is_power_of_two({random_int_two})"
        ),
        (
            f"What is the decimal equivalent of the binary number '1101'",
            f"The decimal equivalent of the binary number '1101' is ##binary_to_decimal('1101')"
        ),
        (
            f"What is the binary representation of the decimal number {random_int_one}",
            f"The binary representation of the decimal number {random_int_one} is ##decimal_to_binary({random_int_one})"
        ),
        (
            f"Is the string 'level' a palindrome",
            f"Checking if the string 'level' is a palindrome is ##is_palindrome('level')"
        ),
        (
            f"What is the sum of the digits in {random_int_four}",
            f"The sum of the digits in {random_int_four} is ##sum_of_digits({random_int_four})"
        ),
        (
            f"What is the area of a circle with radius {random_float}",
            f"The area of a circle with radius {random_float} is ##circle_area({random_float})"
        ),
        (
            f"What is the permutation of {random_int_four} items taken {random_int_two} at a time",
            f"The permutation of {random_int_four} items taken {random_int_two} at a time is ##permutation({random_int_four},{random_int_two})"
        ),
        (
            f"What is the combination of {random_int_three} items taken {random_int_one} at a time",
            f"The combination of {random_int_three} items taken {random_int_one} at a time is ##combination({random_int_three},{random_int_one})"
        ),
        (
            f"What is the inversion of the number {random_int_four}",
            f"The inversion of the number {random_int_four} is ##invert_number({random_int_four})"
        ),
        (
            f"What is the conversion of a float to an integer",
            f"The conversion of a float to an integer is ##float_to_int({random_float})"
        ),
        (
            f"What is the equivalent float value of the integer {random_int_two}",
            f"The conversion of an integer to a float is ##int_to_float({random_int_two})"
        ),
        (
            f"What is the sigmoid function value for {random_float}",
            f"The sigmoid function value for {random_float} is ##sigmoid({random_float})"
        ),
        (
            f"What is the Euler totient function value for {random_int_one}",
            f"The Euler totient function value for {random_int_one} is ##euler_totient({random_int_one})"
        ),
        (
            f"What is the L1 norm of the vector {lst_str}",
            f"The L1 norm of the vector {lst_str} is ##l1_norm({random_list})"
        ),
        (
            f"What is the L2 norm of the vector {lst_str}",
            f"The L2 norm of the vector {lst_str} is ##l2_norm({random_list})"
        ),
        (
            f"What is the average of the numbers {lst_str}",
            f"The average of {lst_str} is ##average({random_list})"
        ),
        (
            f"What is the sum of the numbers {lst_str}",
            f"The sum of {lst_str} is ##sum({random_list})"
        ),
        (
            f"What is the length of the vector {lst_str}",
            f"The length of the vector {lst_str} is ##length({random_list})"
        ),
        (
            f"What is the reverse of the string '{str1}'",
            f"The reverse of the string '{str1}' is ##reverse_string('{str1}')"
        ),
        (
            "What is the value of pi",
            "The value of pi is ##get_pi()"
        ),
        (
            "What is the value of e",
            "The value of e is ##get_e()"
        ),
        (
            f"What is the square of the sum of {random_int_one} and {random_int_two}",
            f"The square of the sum of {random_int_one} and {random_int_two} is ##a_plus_b_whole_square({random_int_one}, {random_int_two})"
        ),
        (
            f"What is the square of the difference of {random_int_one} and {random_int_two}",
            f"The square of the difference of {random_int_one} and {random_int_two} is ##a_minus_b_whole_squared({random_int_one}, {random_int_two})"
        ),
        (
            f"What is the sum of the squares of {random_int_one} and {random_int_two}",
            f"The sum of the squares of {random_int_one} and {random_int_two} is ##a_squared_plus_b_squared({random_int_one}, {random_int_two})"
        ),
        (
            f"What is -2 times {random_int_one} times {random_int_two}",
            f"Negative 2 times {random_int_one} times {random_int_two} is ##negative_2ab({random_int_one}, {random_int_two})"
        ),
        (
            f"What is 2 times {random_int_one} times {random_int_two}",
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
            create_nlf2nlf_batch_two_example(2, None), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )


