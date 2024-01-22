import random

from cl_data.src.constants import PretrainTasks
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def get_batch_thirteen_example_paragraph():
    random_int_one = RandomValueGenerator.generate_random_integer()
    random_int_two = random_int_one + RandomValueGenerator.generate_random_integer()
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer()
    random_int_four = RandomValueGenerator.generate_random_integer()
    random_float = RandomValueGenerator.generate_random_float()
    random_bool = RandomValueGenerator.generate_random_boolean()
    random_list = Utility.remove_spaces(
        str(RandomValueGenerator.generate_random_list())
    )
    random_binary_str = RandomValueGenerator.generate_random_binary_string()

    examples = [
        [
            f"Once upon a time, there were four friends named {random_int_one}, {random_int_two}, {random_int_three}, and {random_int_four}. They decided to embark on a mathematical adventure.",
            f"First, they encountered a challenge. They needed to find the sum of {random_int_one} and {random_int_two}. After careful consideration, they performed the operation and discovered that the result was ##addition({random_int_one}, {random_int_two}).",
            f"Eager to explore more, they moved on to the next task. This time, they faced the challenge of subtracting {random_int_two} from {random_int_three}. The result of this subtraction was ##subtraction({random_int_three}, {random_int_two}).",
            f"As they continued their journey, they stumbled upon a mysterious land where floating numbers roamed freely. Curious, they decided to multiply {random_float} by {random_float}. The magical result was revealed through the operation ##multiplication({random_float}, {random_float}).",
            f"Their adventure took an unexpected turn when they reached a crossroads, and they had to divide {random_float} by {random_float}. The operation of ##division({random_float}, {random_float}) provided the solution to their dilemma.",
            f"In their quest for knowledge, the friends encountered a magical square. Intrigued, they calculated the square of {random_float} using the power of ##exponentiation({random_float}, 2).",
            f"Continuing their journey, they delved into the world of advanced functions. They decided to explore the realm of sine and calculated the sine of {random_float}. The result was ##sine({random_float}).",
            f"Moving further, they encountered a challenge involving logarithms. They needed to find the logarithm of {random_float} to the base 2. The magical result was revealed through the operation ##logarithm_base_2({random_float}).",
            f"As the friends progressed, they faced a geometric puzzle. They needed to find the hypotenuse of a right-angled triangle with sides {random_float} and {random_float}. The solution was found using the operation ##hypotenuse({random_float}, {random_float}).",
            f"Their journey led them to a circle, and they calculated the area of a circle with a radius of {random_float}. The result was obtained through the operation ##circle_area({random_float}).",
        ], [
            f"Curiosity guiding them, the friends explored permutations. They calculated the permutation of {random_int_one} objects taken {random_int_two} at a time. The result was revealed through the operation ##permutation({random_int_one}, {random_int_two}).",
            f"Further into their adventure, combinations presented a challenge. They calculated the combination of {random_int_one} objects taken {random_int_two} at a time. The result was revealed through the operation ##combination({random_int_one}, {random_int_two}).",
            f"In a moment of reflection, they pondered the inverted value of {random_float}. The result was obtained through the operation ##invert_number({random_float}).",
            f"The friends continued their exploration, switching between numeric worlds. They converted the float value of {random_float} to an integer using the operation ##float_to_int({random_float}).",
            f"In another transformation, they converted the integer value of {random_int_one} to a float using the operation ##int_to_float({random_int_one}).",
            f"The friends then ventured into the world of series. They calculated the sum of the first {random_int_one} terms of a geometric series with a first term of {random_float}, a common ratio of {random_float}, and {random_int_two} terms. The result was revealed through the operation ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"Their journey took a sigmoid turn as they explored the realm of mathematical functions. They applied the sigmoid function to {random_float}, and the result was obtained through the operation ##sigmoid({random_float}).",
            f"In the realm of vectors, they explored cosine similarity. They calculated the cosine similarity between two vectors: [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was revealed through the operation ##cosine_similarity([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their adventure reached a moment of totient reflection as they encountered Euler's Totient function. They applied the Euler Totient function to {random_int_one}, and the result was obtained through the operation ##euler_totient({random_int_one}).",
            f"The friends navigated through vector spaces, exploring the concept of norms. They calculated the L1 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l1_norm([{random_float}, {random_float}]).",
        ], [
            f"Continuing their exploration of norms, they calculated the L2 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l2_norm([{random_float}, {random_float}]).",
            f"In the quest for averages, they calculated the average of elements in the list [{random_float}, {random_float}]. The result was obtained through the operation ##average([{random_float}, {random_float}]).",
            f"Their mathematical journey embraced the concept of summation. They calculated the sum of elements in the list [{random_float}, {random_float}]. The result was revealed through the operation ##sum([{random_float}, {random_float}]).",
            f"As the friends dived into the depths of lists, they calculated the length of the list [{random_float}, {random_float}]. The result was obtained through the operation ##length([{random_float}, {random_float}]).",
            f"In a moment of symmetry, they compared strings. They checked if the strings '{random_float} {random_float}' and '{random_float} {random_float}' were the same using the operation ##check_same_string('{random_float} {random_float}', '{random_float} {random_float}').",
            f"To add a twist to their adventure, they explored the concept of reversal. They calculated the reverse of the string '{random_float} {random_float}' using the operation ##reverse_string('{random_float} {random_float}').",
            f"The mathematical odyssey continued as the friends explored the dot product of two vectors. They calculated the dot product of vectors [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was obtained through the operation ##calculate_dot_product([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their journey reached new heights as they explored the square of the sum of {random_int_one} and {random_int_two}. The result was obtained through the operation ##a_plus_b_whole_square({random_int_one}, {random_int_two}).",
            f"In a moment of mathematical poetry, they calculated the result of {random_int_one} squared plus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_squared_plus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The friends faced the challenge of {random_int_one} minus {random_int_two} whole squared plus 4 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_minus_b_whole_squared_plus_4ab({random_int_one}, {random_int_two}).",
        ], [
            f"The adventure continued as they explored the result of {random_int_one} minus {random_int_two} whole squared. The result was obtained through the operation ##a_minus_b_whole_squared({random_int_one}, {random_int_two}).",
            f"In a moment of mathematical expression, they calculated the result of {random_int_one} squared minus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_squared_minus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The friends faced the challenge of the sum of {random_int_one} squared plus {random_int_two} squared minus 4 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_plus_b_whole_squared_minus_4ab({random_int_one}, {random_int_two}).",
            f"The mathematical tapestry continued as they explored the sum of {random_int_one} squared plus {random_int_two} squared. The result was obtained through the operation ##a_squared_plus_b_squared({random_int_one}, {random_int_two}).",
            f"In a moment of inversion, they calculated the negative of 2 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##negative_2ab({random_int_one}, {random_int_two}).",
            f"To add positivity to their journey, they explored the positive of 2 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##positive_2ab({random_int_one}, {random_int_two}).",
            f"In a symphony of expressions, they calculated the result of {random_int_one} plus the quantity {random_int_two} times {random_int_one} plus {random_int_two}. The result was obtained through the operation ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_two}).",
            f"The friends experienced the magic of expressions as they explored the result of {random_int_one} squared plus {random_int_two} plus {random_int_two} times {random_int_one} plus {random_int_two}. The result was obtained through the operation ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_two}).",
            f"In a moment of cubic wonder, they explored the sum of cubes: {random_int_one} cubed plus {random_int_two} cubed. The result was obtained through the operation ##a_cubed_plus_b_cubed({random_int_one}, {random_int_two}).",
            f"The friends faced the challenge of {random_int_one} plus {random_int_two} whole cubed minus 3 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_two}).",
        ], [
            f"The mathematical journey continued as they explored the result of {random_int_one} plus {random_int_two} times the quantity {random_int_one} squared minus {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"In a moment of cubic reflection, they calculated the result of {random_int_one} cubed minus {random_int_two} cubed. The result was obtained through the operation ##a_cubed_minus_b_cubed({random_int_one}, {random_int_two}).",
            f"To add a cubic twist to their adventure, they faced the challenge of {random_int_one} minus {random_int_two} whole cubed plus 3 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_one}, {random_int_two}).",
            f"The friends navigated through the mathematical maze as they explored the result of {random_int_one} minus {random_int_two} times the quantity {random_int_one} squared plus {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_minus_b_times_a_squared_plus_ab_plus_b_squared({random_int_one}, {random_int_two}).",

            f"In a moment of numerical evaluation, they calculated the greatest value between {random_float} and {random_float}. The result was obtained through the operation ##greatest_value({random_float}, {random_float}).",
            f"To explore the realm of minimalism, they calculated the smallest value between {random_float} and {random_float}. The result was obtained through the operation ##smallest_value({random_float}, {random_float}).",
            f"In a quest for productiveness, they calculated the product of the elements in the list {random_list}. The result was revealed through the operation ##product({random_list}).",
            f"The friends then faced the challenge of calculating the factorial of {random_int_one}. The result was obtained through the operation ##factorial({random_int_one}).",
            f"Curious about primality, they investigated whether {random_int_one} is a prime number. The result was revealed through the operation ##is_prime({random_int_one}).",
        ], [
            f"In their pursuit of prime factors, they unveiled the prime factors of {random_int_one}. The result was obtained through the operation ##prime_factors({random_int_one}).",
            f"As they explored the concept of perfect squares, they pondered whether {random_int_one} is a perfect square. The result was revealed through the operation ##is_perfect_square({random_int_one}).",
            f"In a moment of cubic contemplation, they questioned whether {random_int_one} is a perfect cube. The result was obtained through the operation ##is_perfect_cube({random_int_one}).",
            f"The friends then sought the middle ground, calculating the mean of the elements in the list {random_list}. The result was revealed through the operation ##mean({random_list}).",
            f"In a statistical quest, they explored the median of the elements in the list {random_list}. The result was obtained through the operation ##median({random_list}).",
            f"The friends delved into the world of rectified linear units (ReLUs). They applied the ReLU function to {random_float}, and the result was obtained through the operation ##relu({random_float}).",
            f"In the realm of sorting, they arranged the elements in ascending order in the list {random_list}. The result was revealed through the operation ##ascending_sort({random_list}).",
            f"Exploring the opposites, they sorted the elements in descending order in the list {random_list}. The result was obtained through the operation ##descending_sort({random_list}).",
            f"In a moment of mathematical symmetry, they squared the integer {random_int_one}. The result was obtained through the operation ##square_int({random_int_one}).",
            f"As they continued their journey, they calculated the square of {random_float}. The magical result was revealed through the operation ##square({random_float}).",
        ], [
            f"In an absolute revelation, they calculated the absolute value of {random_float}. The result was obtained through the operation ##absolute({random_float}).",
            f"The friends then ventured into the world of powers of ten. They calculated 10 raised to the power of {random_float}. The result was revealed through the operation ##power_of_ten({random_float}).",
            f"In a moment of cubic curiosity, they explored the cube of {random_float}. The result was obtained through the operation ##cube({random_float}).",
            f"To uncover the secrets of cubic roots, they calculated the cube root of {random_float}. The result was revealed through the operation ##cube_root({random_float}).",
            f"In a numerical dichotomy, they pondered whether {random_int_one} is an even number. The result was obtained through the operation ##is_even({random_int_one}).",
            f"Seeking balance, they questioned whether {random_int_one} is an odd number. The result was revealed through the operation ##is_odd({random_int_one}).",
            f"Amidst numerical extremities, they sought the maximum value in the list {random_list}. The result was obtained through the operation ##max_value({random_list}).",
            f"Yearning for simplicity, they sought the minimum value in the list {random_list}. The result was revealed through the operation ##min_value({random_list}).",
            f"In a moment of radical exploration, they calculated the {random_int_two}-th root of {random_float}. The result was obtained through the operation ##nth_root({random_float}, {random_int_two}).",
            f"The friends then delved into the world of geometric means. They calculated the geometric mean of the elements in the list {random_list}. The result was revealed through the operation ##geometric_mean({random_list}).",
        ], [
            f"In a binary revelation, they questioned whether {random_int_one} is a power of two. The result was obtained through the operation ##is_power_of_two({random_int_one}).",
            f"In the realm of binary conversion, they transformed the binary value {random_binary_str} to its decimal equivalent. The result was revealed through the operation ##binary_to_decimal('{random_binary_str}').",
            f"In a decimal metamorphosis, they converted the decimal value {random_int_one} to its binary equivalent. The result was obtained through the operation ##decimal_to_binary({random_int_one}).",
            f"Curiosity guiding them, the friends explored the concept of palindromes. They checked if the string '{random_int_one}' is a palindrome using the operation ##is_palindrome('{random_int_one}').",
            f"To uncover the secrets of digit sum, they calculated the sum of digits in the number {random_int_one}. The result was revealed through the operation ##sum_of_digits({random_int_one}).",
            f"In a moment of trigonometric curiosity, they calculated the hypotenuse of a right-angled triangle with sides {random_float} and {random_float}. The result was obtained through the operation ##hypotenuse({random_float}, {random_float}).",
            f"The friends then explored the concept of permutations in the mathematical realm. They calculated the permutation of {random_int_one} objects taken {random_int_two} at a time. The result was revealed through the operation ##permutation({random_int_one}, {random_int_two}).",
            f"In the realm of combinations, they faced the challenge of calculating the combination of {random_int_one} objects taken {random_int_two} at a time. The result was obtained through the operation ##combination({random_int_one}, {random_int_two}).",
            f"As they delved into the depths of numerical inversion, they calculated the inverted value of {random_float}. The result was revealed through the operation ##invert_number({random_float}).",
            f"In a numerical transformation, they converted the floating-point value of {random_float} to an integer. The result was obtained through the operation ##float_to_int({random_float}).",
        ], [
            f"In another mathematical metamorphosis, they transformed the integer value of {random_int_one} to a floating-point number. The result was revealed through the operation ##int_to_float({random_int_one}).",
            f"In a mathematical series, they calculated the sum of the first {random_int_one} terms of a geometric series with a first term of {random_float}, a common ratio of {random_float}, and {random_int_two} terms. The result was obtained through the operation ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"Their mathematical journey embraced the concept of the sigmoid function. They applied the sigmoid function to the value {random_float}, and the result was revealed through the operation ##sigmoid({random_float}).",
            f"In the realm of vector spaces, they explored cosine similarity. They calculated the cosine similarity between two vectors: [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was obtained through the operation ##cosine_similarity([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their adventure reached a moment of totient reflection as they encountered Euler's Totient function. They applied the Euler Totient function to the value {random_int_one}, and the result was obtained through the operation ##euler_totient({random_int_one}).",
            f"The friends navigated through vector spaces, exploring the concept of norms. They calculated the L1 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l1_norm([{random_float}, {random_float}]).",
            f"Continuing their exploration of norms, they calculated the L2 norm of the vector [{random_float}, {random_float}]. The result was obtained through the operation ##l2_norm([{random_float}, {random_float}]).",
            f"In the quest for averages, they calculated the average of elements in the list [{random_float}, {random_float}]. The result was revealed through the operation ##average([{random_float}, {random_float}]).",
            f"Their mathematical journey embraced the concept of summation. They calculated the sum of elements in the list [{random_float}, {random_float}]. The result was obtained through the operation ##sum([{random_float}, {random_float}]).",
            f"As the friends dived into the depths of lists, they calculated the length of the list [{random_float}, {random_float}]. The result was obtained through the operation ##length([{random_float}, {random_float}]).",
        ], [
            f"In a moment of symmetry, they compared strings. They checked if the strings '{random_float} {random_float}' and '{random_float} {random_float}' were the same using the operation ##check_same_string('{random_float} {random_float}', '{random_float} {random_float}').",
            f"To add a twist to their adventure, they explored the concept of reversal. They calculated the reverse of the string '{random_float} {random_float}' using the operation ##reverse_string('{random_float} {random_float}').",
            f"The mathematical odyssey continued as the friends explored the dot product of two vectors. They calculated the dot product of vectors [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was obtained through the operation ##calculate_dot_product([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their journey reached new heights as they explored the square of the sum of {random_int_one} and {random_int_two}. The result was obtained through the operation ##a_plus_b_whole_square({random_int_one}, {random_int_two}).",
            f"In a moment of mathematical poetry, they calculated the result of {random_int_one} squared plus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_squared_plus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The friends faced the challenge of {random_int_one} minus {random_int_two} whole squared. The result was obtained through the operation ##a_minus_b_whole_squared({random_int_one}, {random_int_two}).",
            f"In a moment of mathematical expression, they calculated the result of {random_int_one} squared minus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_squared_minus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The friends faced the challenge of the sum of {random_int_one} squared plus {random_int_two} squared minus 4 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_plus_b_whole_squared_minus_4ab({random_int_one}, {random_int_two}).",
            f"The mathematical tapestry continued as they explored the sum of {random_int_one} squared plus {random_int_two} squared. The result was obtained through the operation ##a_squared_plus_b_squared({random_int_one}, {random_int_two}).",
            f"In a moment of inversion, they calculated the negative of 2 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##negative_2ab({random_int_one}, {random_int_two}).",
        ], [
            f"To add positivity to their journey, they explored the positive of 2 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##positive_2ab({random_int_one}, {random_int_two}).",
            f"In a symphony of expressions, they calculated the result of {random_int_one} plus the quantity {random_int_two} times {random_int_one} plus {random_int_two}. The result was obtained through the operation ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_two}).",
            f"The friends experienced the magic of expressions as they explored the result of {random_int_one} squared plus {random_int_two} plus {random_int_two} times {random_int_one} plus {random_int_two}. The result was obtained through the operation ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_two}).",
            f"In a moment of cubic wonder, they explored the sum of cubes: {random_int_one} cubed plus {random_int_two} cubed. The result was obtained through the operation ##a_cubed_plus_b_cubed({random_int_one}, {random_int_two}).",
            f"The friends faced the challenge of {random_int_one} plus {random_int_two} whole cubed minus 3 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_two}).",
            f"The mathematical journey continued as they explored the result of {random_int_one} plus {random_int_two} times the quantity {random_int_one} squared minus {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"In a moment of cubic reflection, they calculated the result of {random_int_one} cubed minus {random_int_two} cubed. The result was obtained through the operation ##a_cubed_minus_b_cubed({random_int_one}, {random_int_two}).",
            f"To add a cubic twist to their adventure, they faced the challenge of {random_int_one} minus {random_int_two} whole cubed plus 3 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_one}, {random_int_two}).",
            f"The friends navigated through the mathematical maze as they explored the result of {random_int_one} minus {random_int_two} times the quantity {random_int_one} squared plus {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_minus_b_times_a_squared_plus_ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"Continuing their journey through mathematical permutations, they calculated the permutation of {random_int_one} objects taken {random_int_two} at a time. The result was revealed through the operation ##permutation({random_int_one}, {random_int_two}).",
        ], [
            f"In a combinatorial twist, they explored the combination of {random_int_one} objects taken {random_int_two} at a time. The result was obtained through the operation ##combination({random_int_one}, {random_int_two}).",
            f"In a moment of inversion, they pondered the inverted value of {random_float}. The result was obtained through the operation ##invert_number({random_float}).",
            f"The friends continued their exploration, switching between numeric worlds. They converted the float value of {random_float} to an integer using the operation ##float_to_int({random_float}).",
            f"In another transformation, they converted the integer value of {random_int_one} to a float using the operation ##int_to_float({random_int_one}).",
            f"The friends then ventured into the world of series. They calculated the sum of the first {random_int_one} terms of a geometric series with a first term of {random_float}, a common ratio of {random_float}, and {random_int_two} terms. The result was revealed through the operation ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"Their journey took a sigmoid turn as they explored the realm of mathematical functions. They applied the sigmoid function to {random_float}, and the result was obtained through the operation ##sigmoid({random_float}).",
            f"In the realm of vectors, they explored cosine similarity. They calculated the cosine similarity between two vectors: [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was revealed through the operation ##cosine_similarity([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their adventure reached a moment of totient reflection as they encountered Euler's Totient function. They applied the Euler Totient function to {random_int_one}, and the result was obtained through the operation ##euler_totient({random_int_one}).",
            f"The friends navigated through vector spaces, exploring the concept of norms. They calculated the L1 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l1_norm([{random_float}, {random_float}]).",
            f"Continuing their exploration of norms, they calculated the L2 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l2_norm([{random_float}, {random_float}]).",
        ], [
            f"In the quest for averages, they calculated the average of elements in the list [{random_float}, {random_float}]. The result was obtained through the operation ##average([{random_float}, {random_float}]).",
            f"Their mathematical journey embraced the concept of summation. They calculated the sum of elements in the list [{random_float}, {random_float}]. The result was revealed through the operation ##sum([{random_float}, {random_float}]).",
            f"As the friends dived into the depths of lists, they calculated the length of the list [{random_float}, {random_float}]. The result was obtained through the operation ##length([{random_float}, {random_float}]).",
            f"In a moment of symmetry, they compared strings. They checked if the strings '{random_float} {random_float}' and '{random_float} {random_float}' were the same using the operation ##check_same_string('{random_float} {random_float}', '{random_float} {random_float}').",
            f"To add a twist to their adventure, they explored the concept of reversal. They calculated the reverse of the string '{random_float} {random_float}' using the operation ##reverse_string('{random_float} {random_float}').",
            f"The mathematical odyssey continued as the friends explored the dot product of two vectors. They calculated the dot product of vectors [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was obtained through the operation ##calculate_dot_product([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their journey reached new heights as they explored the square of the sum of {random_int_one} and {random_int_two}. The result was obtained through the operation ##a_plus_b_whole_square({random_int_one}, {random_int_two}).",
            f"In a moment of mathematical poetry, they calculated the result of {random_int_one} squared plus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_squared_plus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The friends faced the challenge of {random_int_one} minus {random_int_two} whole squared plus 4 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_minus_b_whole_squared_plus_4ab({random_int_one}, {random_int_two}).",
            f"The adventure continued as they explored the result of {random_int_one} minus {random_int_two} whole squared."
        ]
    ]
    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator

    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_thirteen_example_paragraph(),
    )
    sample = Utility.create_sample_from_example(
        masked_example,
        PretrainTasks.MASKED_TOKEN_PREDICTION,
    )
    print(sample)

    from next_token_sample_generator import NextTokenSamplesGenerator

    next_token_example = NextTokenSamplesGenerator.create_next_token_batches(
        get_batch_thirteen_example_paragraph(),
    )
    sample = Utility.create_sample_from_example(
        next_token_example,
        PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
