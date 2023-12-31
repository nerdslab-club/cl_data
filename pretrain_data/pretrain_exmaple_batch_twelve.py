from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def get_batch_twelve_example_paragraph():
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
            f"The sum of {random_int_one} and {random_int_two} is ##addition({random_int_one}, {random_int_two}).",
            f"The result of subtracting {random_int_two} from {random_int_three} is ##subtraction({random_int_three}, {random_int_two}).",
            f"The product of {random_float} and {random_float} is ##multiplication({random_float}, {random_float}).",
            f"The quotient of {random_float} divided by {random_float} is ##division({random_float}, {random_float}).",
            f"The square of {random_float} is ##exponentiation({random_float}, 2).",
            f"The square root of {random_float} is ##square_root({random_float}).",
            f"The floor division of {random_int_four} by {random_int_two} is ##floor_division({random_int_four}, {random_int_two}).",
            f"The modulus of {random_int_four} by {random_int_two} is ##modulus({random_int_four}, {random_int_two}).",
            f"The logarithm of {random_float} with base {random_float} is ##logarithm({random_float}, {random_float}).",
            f"The sine of {random_float} is ##sine({random_float})."],
        [
            f"The cosine of {random_float} is ##cosine({random_float}).",
            f"The tangent of {random_float} is ##tangent({random_float}).",
            f"The arcsine of {random_float} is ##arcsine({random_float}).",
            f"The arccosine of {random_float} is ##arccosine({random_float}).",
            f"The arctangent of {random_float} is ##arctangent({random_float}).",
            f"The hyperbolic sine of {random_float} is ##hyperbolic_sine({random_float}).",
            f"The hyperbolic cosine of {random_float} is ##hyperbolic_cosine({random_float}).",
            f"The hyperbolic tangent of {random_float} is ##hyperbolic_tangent({random_float}).",
            f"The logarithm base 10 of {random_float} is ##logarithm_base_10({random_float}).",
            f"The logarithm base 2 of {random_float} is ##logarithm_base_2({random_float})."]
        , [
            f"The value of pi is ##get_pi().",
            f"The value of e is ##get_e().",
            f"The degrees equivalent of {random_float} radians is ##radians_to_degrees({random_float}).",
            f"The greatest common divisor of {random_int_one} and {random_int_two} is ##gcd({random_int_one}, {random_int_two}).",
            f"The least common multiple of {random_int_one} and {random_int_two} is ##lcm({random_int_one}, {random_int_two}).",
            f"The integer square root of {random_int_one} is ##isqrt({random_int_one}).",
            f"The result of raising {random_float} to the power of {random_int_one} is ##pow_mod({random_float}, {random_int_one}, {random_int_two}).",
            f"The ceiling value of {random_float} is ##ceil({random_float}).",
            f"The floor value of {random_float} is ##floor({random_float}).",
            f"The rounded value of {random_float} is ##round({random_float}).", ],
        [
            f"The absolute difference between {random_float} and {random_float} is ##absolute_difference({random_float}, {random_float}).",
            f"The greater value between {random_float} and {random_float} is ##greatest_value({random_float}, {random_float}).",
            f"The smaller value between {random_float} and {random_float} is ##smallest_value({random_float}, {random_float}).",
            f"The product of elements in the list {random_list} is ##product({random_list}).",
            f"The factorial of {random_int_one} is ##factorial({random_int_one}).",
            f"Is {random_int_one} a prime number? ##is_prime({random_int_one}).",
            f"The prime factors of {random_int_one} are ##prime_factors({random_int_one}).",
            f"Is {random_int_one} a perfect square? ##is_perfect_square({random_int_one}).",
            f"Is {random_int_one} a perfect cube? ##is_perfect_cube({random_int_one}).",
            f"The mean of elements in the list {random_list} is ##mean({random_list}).", ],
        [
            f"The median of elements in the list {random_list} is ##median({random_list}).",
            f"The Rectified Linear Unit (ReLU) applied to {random_float} is ##relu({random_float}).",
            f"The list {random_list} sorted in ascending order is ##ascending_sort({random_list}).",
            f"The list {random_list} sorted in descending order is ##descending_sort({random_list}).",
            f"The square of the integer {random_int_one} is ##square_int({random_int_one}).",
            f"The square of {random_float} is ##square({random_float}).",
            f"The absolute value of {random_float} is ##absolute({random_float}).",
            f"Ten raised to the power of {random_float} is ##power_of_ten({random_float}).",
            f"The cube of {random_float} is ##cube({random_float}).",
            f"The cube root of {random_float} is ##cube_root({random_float}).", ],
        [
            f"Is {random_int_one} an even number? ##is_even({random_int_one}).",
            f"Is {random_int_one} an odd number? ##is_odd({random_int_one}).",
            f"The maximum value in the list {random_list} is ##max_value({random_list}).",
            f"The minimum value in the list {random_list} is ##min_value({random_list}).",
            f"The {random_int_one}-th root of {random_float} is ##nth_root({random_float}, {random_int_one}).",
            f"The geometric mean of elements in the list {random_list} is ##geometric_mean({random_list}).",
            f"Is {random_int_one} a power of two? ##is_power_of_two({random_int_one}).",
            f"The binary representation of {random_int_one} is ##decimal_to_binary({random_int_one}).",
            f"The decimal representation of binary number {random_binary_str} is ##binary_to_decimal({random_binary_str}).",
            f"Is the string {random_list} a palindrome? ##is_palindrome('{random_list}')."],
        [
            f"The sum of digits in {random_int_one} is ##sum_of_digits({random_int_one}).",
            f"The hypotenuse of a right-angled triangle with sides {random_float} and {random_float} is ##hypotenuse({random_float}, {random_float}).",
            f"The area of a circle with radius {random_float} is ##circle_area({random_float}).",
            f"The permutation of {random_int_one} objects taken {random_int_two} at a time is ##permutation({random_int_one}, {random_int_two}).",
            f"The combination of {random_int_one} objects taken {random_int_two} at a time is ##combination({random_int_one}, {random_int_two}).",
            f"The inverted value of {random_float} is ##invert_number({random_float}).",
            f"The integer value of {random_float} is ##float_to_int({random_float}).",
            f"The float value of {random_int_one} is ##int_to_float({random_int_one}).",
            f"The sum of the first {random_int_one} terms of a geometric series with first term {random_float}, common ratio {random_float}, and {random_int_two} terms is ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"The sigmoid function applied to {random_float} is ##sigmoid({random_float}).", ],
        [
            f"The cosine similarity between vectors {random_list} and {random_list} is ##cosine_similarity({random_list}, {random_list}).",
            f"The Euler Totient function applied to {random_int_one} is ##euler_totient({random_int_one}).",
            f"The L1 norm of vector {random_list} is ##l1_norm({random_list}).",
            f"The L2 norm of vector {random_list} is ##l2_norm({random_list}).",
            f"The average of elements in the list {random_list} is ##average({random_list}).",
            f"The sum of elements in the list {random_list} is ##sum({random_list}).",
            f"The length of the list {random_list} is ##length({random_list}).",
            f"Are the strings '{random_list}' and '{random_list}' the same? ##check_same_string('{random_list}', '{random_list}').",
            f"The reverse of the string '{random_list}' is ##reverse_string('{random_list}').", ],
        [
            f"The sum of elements in the list {random_list} is ##sum({random_list}).",
            f"The length of the list {random_list} is ##length({random_list}).",
            f"Are the strings '{random_list}' and '{random_list}' the same? ##check_same_string('{random_list}', '{random_list}').",
            f"The reverse of the string '{random_list}' is ##reverse_string('{random_list}').",
            f"The dot product of vectors {random_list} and {random_list} is ##calculate_dot_product({random_list}, {random_list}).",
            f"The square of the sum of {random_int_one} and {random_int_two} is ##a_plus_b_whole_square({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} squared plus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_squared_plus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} minus {random_int_two} whole squared plus 4 times {random_int_one} times {random_int_two} is ##a_minus_b_whole_squared_plus_4ab({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} minus {random_int_two} whole squared is ##a_minus_b_whole_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} squared minus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_squared_minus_2ab_plus_b_squared({random_int_one}, {random_int_two}).", ],
        [
            f"The result of {random_int_one} plus {random_int_two} whole squared minus 4 times {random_int_one} times {random_int_two} is ##a_plus_b_whole_squared_minus_4ab({random_int_one}, {random_int_two}).",
            f"The sum of {random_int_one} squared plus {random_int_two} squared is ##a_squared_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The negative of 2 times {random_int_one} times {random_int_two} is ##negative_2ab({random_int_one}, {random_int_two}).",
            f"The positive of 2 times {random_int_one} times {random_int_two} is ##positive_2ab({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} plus the quantity {random_int_two} times {random_int_one} plus {random_int_two} is ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_two}).",
            f"The result of {random_int_one} squared plus {random_int_two} plus {random_int_two} times {random_int_one} plus {random_int_two} is ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_two}).",
            f"The sum of cubes {random_int_one} cubed plus {random_int_two} cubed is ##a_cubed_plus_b_cubed({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} plus {random_int_two} whole cubed minus 3 times {random_int_one} times {random_int_two} is ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} plus {random_int_two} times the quantity {random_int_one} squared minus {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} cubed minus {random_int_two} cubed is ##a_cubed_minus_b_cubed({random_int_one}, {random_int_two}).", ],
        [
            f"The result of {random_int_one} minus {random_int_two} whole cubed plus 3 times {random_int_one} times {random_int_two} is ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} minus {random_int_two} times the quantity {random_int_one} squared plus {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_minus_b_times_a_squared_plus_ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} squared plus {random_int_two} squared is ##a_squared_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The negative of 2 times {random_int_one} times {random_int_two} is ##negative_2ab({random_int_one}, {random_int_two}).",
            f"The positive of 2 times {random_int_one} times {random_int_two} is ##positive_2ab({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} plus the quantity {random_int_two} times {random_int_one} plus {random_int_two} is ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_two}).",
            f"The result of {random_int_one} squared plus {random_int_two} plus {random_int_two} times {random_int_one} plus {random_int_two} is ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_two}).",
            f"The sum of cubes {random_int_one} cubed plus {random_int_two} cubed is ##a_cubed_plus_b_cubed({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} plus {random_int_two} whole cubed minus 3 times {random_int_one} times {random_int_two} is ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} plus {random_int_two} times the quantity {random_int_one} squared minus {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} cubed minus {random_int_two} cubed is ##a_cubed_minus_b_cubed({random_int_one}, {random_int_two}).", ],
        [
            f"The result of {random_int_one} minus {random_int_two} whole cubed plus 3 times {random_int_one} times {random_int_two} is ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} minus {random_int_two} times the quantity {random_int_one} squared plus {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_minus_b_times_a_squared_plus_ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} minus {random_int_two} whole squared is ##a_minus_b_whole_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} squared plus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_squared_plus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} minus {random_int_two} whole squared plus 4 times {random_int_one} times {random_int_two} is ##a_minus_b_whole_squared_plus_4ab({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} minus {random_int_two} whole squared is ##a_minus_b_whole_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} squared minus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_squared_minus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} plus {random_int_two} whole squared minus 4 times {random_int_one} times {random_int_two} is ##a_plus_b_whole_squared_minus_4ab({random_int_one}, {random_int_two}).",
            f"The sum of squares {random_int_one} squared plus {random_int_two} squared is ##a_squared_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} squared plus {random_int_two} squared is ##a_squared_plus_b_squared({random_int_one}, {random_int_two}).", ],
        [
            f"The result of 2 times {random_int_one} times {random_int_two} is ##positive_2ab({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} plus {random_int_two} times the quantity {random_int_one} plus {random_int_two} is ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_two}).",
            f"The result of {random_int_one} squared plus {random_int_two} plus {random_int_two} times {random_int_one} plus {random_int_two} is ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_two}).",
            f"The sum of cubes {random_int_one} cubed plus {random_int_two} cubed is ##a_cubed_plus_b_cubed({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} plus {random_int_two} whole cubed minus 3 times {random_int_one} times {random_int_two} is ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} plus {random_int_two} times the quantity {random_int_one} squared minus {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} cubed minus {random_int_two} cubed is ##a_cubed_minus_b_cubed({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} minus {random_int_two} whole cubed plus 3 times {random_int_one} times {random_int_two} is ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_one}, {random_int_two}).",
            f"The result of {random_int_one} minus {random_int_two} times the quantity {random_int_one} squared plus {random_int_one} times {random_int_two} plus {random_int_two} squared is ##a_minus_b_times_a_squared_plus_ab_plus_b_squared({random_int_one}, {random_int_two}).", ]
    ]
    return examples[0]
    #return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator
    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_twelve_example_paragraph(),
    )
    sample = Utility.create_sample_from_example(
        masked_example,
        PretrainTasks.MASKED_TOKEN_PREDICTION,
    )
    print(sample)

    from next_token_sample_generator import NextTokenSamplesGenerator
    next_token_example = NextTokenSamplesGenerator.create_next_token_batches(
        get_batch_twelve_example_paragraph(),
    )
    sample = Utility.create_sample_from_example(
        next_token_example,
        PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
