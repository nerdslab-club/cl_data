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
    random_degree =random.uniform(0, 2 * 3.14159)
    str1 = RandomValueGenerator.generate_random_string()
    if random_int_one % 2:
        str2 = RandomValueGenerator.generate_random_string()
    else:
        str2 = str1

    examples = [
        (
            f"{random_int_one} * {random_int_four}",
            f"The result of multiplying {random_int_one} by {random_int_four} is ##multiplication({random_int_one},{random_int_four})",
        ),
        (
            f"{random_int_two} + {random_int_three}",
            f"The result of adding {random_int_two} and {random_int_three} is ##addition({random_int_two},{random_int_three})",
        ),
        (
            f"{random_int_three} - {random_int_one}",
            f"The result of subtracting {random_int_three} from {random_int_one} is ##subtraction({random_int_one},{random_int_three})",
        ),
        (
            f"{random_int_two} / {random_int_one}",
            f"The result of dividing {random_int_two} by {random_int_one} is ##division({random_int_two},{random_int_one})",
        ),
        (
            f"{random_int_one} ** {random_int_two}",
            f"The result of exponentiation {random_int_one} to the power of {random_int_two} is ##exponentiation({random_int_one},{random_int_two})",
        ),
        (
            f"sqrt({random_int_two})",
            f"The square root of {random_int_two} is ##square_root({random_int_two})",
        ),
        (
            f"{random_int_three} // {random_int_one}",
            f"The result of floor division {random_int_three} by {random_int_one} is ##floor_division({random_int_three},{random_int_one})",
        ),
        (
            f"{random_int_four} % {random_int_two}",
            f"The remainder of dividing {random_int_four} by {random_int_two} is ##modulus({random_int_four},{random_int_two})",
        ),
        (
            f"log({random_int_three},{random_int_one})",
            f"The logarithm of {random_int_three} to the base {random_int_one} is ##logarithm({random_int_three},{random_int_one})",
        ),
        (
            f"sin({random_int_one})",
            f"The sine of {random_int_one} is ##sine({random_int_one})",
        ),
        (
            f"cos({random_int_two})",
            f"The cosine of {random_int_two} is ##cosine({random_int_two})",
        ),
        (
            f"tan({random_int_three})",
            f"The tangent of {random_int_three} is ##tangent({random_int_three})",
        ),
        (
            f"asin({random_arc_int})",
            f"The arcsine of a random value is ##arcsine({random_arc_int})",
        ),
        (
            f"acos({random_arc_int})",
            f"The arccosine of a random value is ##arccosine({random_arc_int})",
        ),
        (
            f"atan({random_arc_int})",
            f"The arctangent of a random value is ##arctangent({random_arc_int})",
        ),
        (
            f"sinh({random_int_one})",
            f"The hyperbolic sine of {random_int_one} is ##hyperbolic_sine({random_int_one})",
        ),
        (
            f"cosh({random_int_two})",
            f"The hyperbolic cosine of {random_int_two} is ##hyperbolic_cosine({random_int_two})",
        ),
        (
            f"tanh({random_int_three})",
            f"The hyperbolic tangent of {random_int_three} is ##hyperbolic_tangent({random_int_three})",
        ),
        (
            f"log10({random_int_three})",
            f"The logarithm base 10 of {random_int_three} is ##logarithm_base_10({random_int_three})",
        ),
        (
            f"log2({random_int_two})",
            f"The logarithm base 2 of {random_int_two} is ##logarithm_base_2({random_int_two})",
        ),
        (
            f"degrees({random_degree})",
            f"The conversion of radians to degrees is ##degrees_to_radians({random_degree})",
        ),
        (
            f"radians({random_int_one})",
            f"The conversion of degrees to radians is ##radians_to_degrees({random_int_one})",
        ),
        (
            f"gcd({random_int_one},{random_int_two})",
            f"The greatest common divisor of {random_int_one} and {random_int_two} is ##gcd({random_int_one},{random_int_two})",
        ),
        (
            f"lcm({random_int_three},{random_int_four})",
            f"The least common multiple of {random_int_three} and {random_int_four} is ##lcm({random_int_three},{random_int_four})",
        ),
        (
            f"isqrt({random_int_two})",
            f"The integer square root of {random_int_two} is ##isqrt({random_int_two})",
        ),
        (
            f"pow_mod({random_int_one},{random_int_two},{random_int_three})",
            f"The modular exponentiation of {random_int_one} to the power of {random_int_two} modulo {random_int_three} is ##pow_mod({random_int_one},{random_int_two},{random_int_three})",
        ),
        (
            f"ceil({random_float})",
            f"The ceiling of a random value is ##ceil({random_float})",
        ),
        (
            f"floor({random_float})",
            f"The floor of a random value is ##floor({random_float})",
        ),
        (
            f"round({random_float})",
            f"The rounded value of a random number is ##round({random_float})",
        ),
        (
            f"abs({random_int_one - random_int_two})",
            f"The absolute difference between {random_int_one} and {random_int_two} is ##absolute_difference({random_int_one},{random_int_two})",
        ),
        (
            f"max({random_int_three},{random_int_four})",
            f"The greater value between {random_int_three} and {random_int_four} is ##greatest_value({random_int_three},{random_int_four})",
        ),
        (
            f"min({random_int_one},{random_int_two})",
            f"The smaller value between {random_int_one} and {random_int_two} is ##smallest_value({random_int_one},{random_int_two})",
        ),
        (
            f"product({random_list})",
            f"The product of the numbers {lst_str} is ##product({random_list})",
        ),
        (
            f"factorial({random_int_four})",
            f"The factorial of {random_int_four} is ##factorial({random_int_four})",
        ),
        (
            f"is_prime({random_int_two})",
            f"The primality check for {random_int_two} is ##is_prime({random_int_two})",
        ),
        (
            f"prime_factors({random_int_three})",
            f"The prime factors of {random_int_three} are ##prime_factors({random_int_three})",
        ),
        (
            f"is_perfect_square({random_int_four})",
            f"Checking if {random_int_four} is a perfect square ##is_perfect_square({random_int_four})",
        ),
        (
            f"is_perfect_cube({random_int_one})",
            f"Checking if {random_int_one} is a perfect cube ##is_perfect_cube({random_int_one})",
        ),
        (
            f"mean({random_list})",
            f"The mean of the numbers {lst_str} is ##mean({random_list})",
        ),
        (
            f"median({random_list})",
            f"The median of the numbers {lst_str} is ##median({random_list})",
        ),
        (
            f"relu({random_float})",
            f"The rectified linear unit (ReLU) of a random value is ##relu({random_float})",
        ),
        (
            f"ascending_sort({random_list})",
            f"The ascending sorted list of numbers {lst_str} is ##ascending_sort({random_list})",
        ),
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
            f"check_same_string('{str1}', '{str2}')",
            f"Are '{str1}' and '{str2}' the same string? ##check_same_string('{str1}', '{str2}')"
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
            f"a_squared_plus_2ab_plus_b_squared({random_int_one}, {random_int_two})",
            f"The expression {random_int_one} squared plus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_squared_plus_2ab_plus_b_squared({random_int_one}, {random_int_two})"
        ),
        (
            f"a_minus_b_whole_squared_plus_4ab({random_int_one}, {random_int_two})",
            f"The square of the difference of {random_int_one} and {random_int_two} plus 4 times {random_int_one} times {random_int_two} is ##a_minus_b_whole_squared_plus_4ab({random_int_one}, {random_int_two})"
        ),
        (
            f"a_minus_b_whole_squared({random_int_one}, {random_int_two})",
            f"The square of the difference of {random_int_one} and {random_int_two} is ##a_minus_b_whole_squared({random_int_one}, {random_int_two})"
        ),
        (
            f"a_squared_minus_2ab_plus_b_squared({random_int_one}, {random_int_two})",
            f"The expression {random_int_one} squared minus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_squared_minus_2ab_plus_b_squared({random_int_one}, {random_int_two})"
        ),
        (
            f"a_plus_b_whole_squared_minus_4ab({random_int_one}, {random_int_two})",
            f"The square of the sum of {random_int_one} and {random_int_two} minus 4 times {random_int_one} times {random_int_two} is ##a_plus_b_whole_squared_minus_4ab({random_int_one}, {random_int_two})"
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
        (
            f"x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three})",
            f"The result of {random_int_one} plus {random_int_two} times {random_int_three} is ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three})"
        ),
        (
            f"x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three})",
            f"The result of {random_int_one} squared plus {random_int_two} plus {random_int_three} times the sum of {random_int_one} and {random_int_two} is ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three})"
        ),
        (
            f"a_cubed_plus_b_cubed({random_int_one}, {random_int_two})",
            f"The sum of {random_int_one} cubed and {random_int_two} cubed is ##a_cubed_plus_b_cubed({random_int_one}, {random_int_two})"
        ),
        (
            f"a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_two})",
            f"The cube of the sum of {random_int_one} and {random_int_two} minus 3 times the product of {random_int_one} and {random_int_two} is ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_two})"
        ),
        (
            f"a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_one}, {random_int_two})",
            f"The product of the sum of {random_int_one} and {random_int_two} and the difference of {random_int_one} squared plus {random_int_two} squared is ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_one}, {random_int_two})"
        ),
        (
            f"a_cubed_minus_b_cubed({random_int_one}, {random_int_two})",
            f"The difference of {random_int_one} cubed minus {random_int_two} cubed is ##a_cubed_minus_b_cubed({random_int_one}, {random_int_two})"
        ),
        (
            f"a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_one}, {random_int_two})",
            f"The cube of the difference of {random_int_one} and {random_int_two} plus 3 times the product of {random_int_one} and {random_int_two} is ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_one}, {random_int_two})"
        ),
        (
            f"a_minus_b_times_a_squared_plus_ab_plus_b_squared({random_int_one}, {random_int_two})",
            f"The product of the difference of {random_int_one} and {random_int_two} and the sum of {random_int_one} squared plus {random_int_two} squared is ##a_minus_b_times_a_squared_plus_ab_plus_b_squared({random_int_one}, {random_int_two})"
        ),
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_two_example(2), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )


