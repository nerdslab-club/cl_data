import random

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def get_batch_fourteen_example_paragraph():
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
            f"In a cosmic exploration, they calculated the result of raising {random_float} to the power of {random_float}. The result was obtained through the operation ##exponentiation({random_float}, {random_float}).",
            f"As they ventured into the realm of cosmic energies, they calculated the hyperbolic sine of {random_float}. The result was revealed through the operation ##hyperbolic_sine({random_float}).",
            f"In a quest for celestial harmony, they explored the logarithm of {random_float} with base {random_float}. The result was obtained through the operation ##logarithm({random_float}, {random_float}).",
            f"The mathematical journey embraced trigonometry as they calculated the tangent of {random_float} radians. The result was revealed through the operation ##tangent({random_float}).",
            f"In a moment of angular exploration, they calculated the arccosine of {random_float}. The result was obtained through the operation ##arccosine({random_float}).",
            f"They embarked on a journey through geometric shapes, calculating the area of a circle with a radius of {random_float}. The result was revealed through the operation ##circle_area({random_float}).",
            f"As they traversed through permutations, they calculated the permutation of {random_int_one} objects taken {random_int_two} at a time. The result was obtained through the operation ##permutation({random_int_one}, {random_int_two}).",
            f"In a combinatorial twist, they explored the combination of {random_int_one} objects taken {random_int_two} at a time. The result was revealed through the operation ##combination({random_int_one}, {random_int_two}).",
            f"They encountered a moment of inversion, exploring the inverted value of {random_float}. The result was obtained through the operation ##invert_number({random_float}).",
            f"To add a dynamic shift to their exploration, they converted the float value of {random_float} to an integer using the operation ##float_to_int({random_float}).",
            f"In a transformational phase, they converted the integer value of {random_int_one} to a float using the operation ##int_to_float({random_int_one}).",
            f"The friends then delved into the concept of series, calculating the sum of the first {random_int_one} terms of a geometric series with a first term of {random_float}, a common ratio of {random_float}, and {random_int_two} terms. The result was obtained through the operation ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"Their journey took a sigmoid turn as they explored the realm of mathematical functions. They applied the sigmoid function to {random_float}, and the result was revealed through the operation ##sigmoid({random_float}).",
            f"In the cosmic landscape of vectors, they explored cosine similarity. They calculated the cosine similarity between two vectors: [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was obtained through the operation ##cosine_similarity([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their adventure reached a moment of totient reflection as they encountered Euler's Totient function. They applied the Euler Totient function to {random_int_one}, and the result was obtained through the operation ##euler_totient({random_int_one}).",
            f"The friends navigated through vector spaces, exploring the concept of norms. They calculated the L1 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l1_norm([{random_float}, {random_float}]).",
            f"Continuing their exploration of norms, they calculated the L2 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l2_norm([{random_float}, {random_float}]).",
            f"In the quest for harmonious averages, they calculated the average of elements in the list [{random_float}, {random_float}]. The result was obtained through the operation ##average([{random_float}, {random_float}]).",
            f"Their mathematical journey embraced the symphony of summation. They calculated the sum of elements in the list [{random_float}, {random_float}]. The result was revealed through the operation ##sum([{random_float}, {random_float}]).",
            f"As the friends dived into the cosmic depths of lists, they calculated the length of the list [{random_float}, {random_float}]. The result was obtained through the operation ##length([{random_float}, {random_float}]).",
            f"In a cosmic moment of symmetry, they compared strings. They checked if the strings '{random_float} {random_float}' and '{random_float} {random_float}' were the same using the operation ##check_same_string('{random_float} {random_float}', '{random_float} {random_float}').",
            f"To add a cosmic twist to their adventure, they explored the concept of cosmic reversal. They calculated the reverse of the string '{random_float} {random_float}' using the operation ##reverse_string('{random_float} {random_float}').",
            f"The cosmic odyssey continued as the friends explored the cosmic dot product of two vectors. They calculated the dot product of vectors [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was obtained through the operation ##calculate_dot_product([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their journey reached new cosmic heights as they explored the square of the cosmic sum of {random_int_one} and {random_int_two}. The result was obtained through the operation ##a_plus_b_whole_square({random_int_one}, {random_int_two}).",
            f"In a moment of cosmic poetry, they calculated the result of {random_int_one} squared plus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_squared_plus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The friends faced the cosmic challenge of {random_int_one} minus {random_int_two} whole squared plus 4 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_minus_b_whole_squared_plus_4ab({random_int_one}, {random_int_two}).",
            f"The cosmic adventure continued as they explored the cosmic result of {random_int_one} minus {random_int_two} whole squared."
        ],
        [
            f"In the mystical land of mathematics, they embarked on a journey of addition. They added {random_int_one} and {random_int_two}, and the result was obtained through the operation ##addition({random_int_one}, {random_int_two}).",
            f"As they navigated through numerical realms, they encountered the realm of subtraction. They subtracted {random_int_two} from {random_int_three}, revealing the result through the operation ##subtraction({random_int_three}, {random_int_two}).",
            f"Their mathematical expedition delved into the mysteries of multiplication. They multiplied {random_float} by {random_float}, uncovering the result through the operation ##multiplication({random_float}, {random_float}).",
            f"In a moment of mathematical division, they divided {random_float} by {random_float}, and the result was revealed through the operation ##division({random_float}, {random_float}).",
            f"As they soared into the mathematical skies, they explored the power of exponentiation. They raised {random_float} to the power of {random_float}, revealing the result through the operation ##exponentiation({random_float}, {random_float}).",
            f"Their mathematical senses tingled as they calculated the square root of {random_float}. The result was obtained through the operation ##square_root({random_float}).",
            f"In a journey through integer landscapes, they explored the realm of floor division. They divided {random_int_four} by {random_int_three}, revealing the result through the operation ##floor_division({random_int_four}, {random_int_three}).",
            f"As they unraveled the threads of modulo, they calculated the modulus of {random_int_one} modulo {random_int_two}. The result was obtained through the operation ##modulus({random_int_one}, {random_int_two}).",
            f"Their mathematical curiosity led them to the world of logarithms. They calculated the logarithm of {random_float} with base {random_float}, and the result was revealed through the operation ##logarithm({random_float}, {random_float}).",
            f"In a moment of trigonometric exploration, they calculated the sine of {random_float} radians. The result was obtained through the operation ##sine({random_float}).",
            f"In a cosmic exploration, they calculated the result of raising {random_float} to the power of {random_float}. The result was obtained through the operation ##exponentiation({random_float}, {random_float}).",
            f"As they ventured into the realm of cosmic energies, they calculated the hyperbolic sine of {random_float}. The result was revealed through the operation ##hyperbolic_sine({random_float}).",
            f"In a quest for celestial harmony, they explored the logarithm of {random_float} with base {random_float}. The result was obtained through the operation ##logarithm({random_float}, {random_float}).",
            f"The mathematical journey embraced trigonometry as they calculated the tangent of {random_float} radians. The result was revealed through the operation ##tangent({random_float}).",
            f"In a moment of angular exploration, they calculated the arccosine of {random_float}. The result was obtained through the operation ##arccosine({random_float}).",
            f"They embarked on a journey through geometric shapes, calculating the area of a circle with a radius of {random_float}. The result was revealed through the operation ##circle_area({random_float}).",
            f"As they traversed through permutations, they calculated the permutation of {random_int_one} objects taken {random_int_two} at a time. The result was obtained through the operation ##permutation({random_int_one}, {random_int_two}).",
            f"In a combinatorial twist, they explored the combination of {random_int_one} objects taken {random_int_two} at a time. The result was revealed through the operation ##combination({random_int_one}, {random_int_two}).",
            f"They encountered a moment of inversion, exploring the inverted value of {random_float}. The result was obtained through the operation ##invert_number({random_float}).",
            f"To add a dynamic shift to their exploration, they converted the float value of {random_float} to an integer using the operation ##float_to_int({random_float}).",
            f"In a transformational phase, they converted the integer value of {random_int_one} to a float using the operation ##int_to_float({random_int_one}).",
            f"The friends then delved into the concept of series, calculating the sum of the first {random_int_one} terms of a geometric series with a first term of {random_float}, a common ratio of {random_float}, and {random_int_two} terms. The result was obtained through the operation ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"Their journey took a sigmoid turn as they explored the realm of mathematical functions. They applied the sigmoid function to {random_float}, and the result was revealed through the operation ##sigmoid({random_float}).",
            f"In the cosmic landscape of vectors, they explored cosine similarity. They calculated the cosine similarity between two vectors: [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was obtained through the operation ##cosine_similarity([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their adventure reached a moment of totient reflection as they encountered Euler's Totient function. They applied the Euler Totient function to {random_int_one}, and the result was obtained through the operation ##euler_totient({random_int_one}).",
            f"The friends navigated through vector spaces, exploring the concept of norms. They calculated the L1 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l1_norm([{random_float}, {random_float}]).",
            f"Continuing their exploration of norms, they calculated the L2 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l2_norm([{random_float}, {random_float}]).",
            f"In the quest for harmonious averages, they calculated the average of elements in the list [{random_float}, {random_float}]. The result was obtained through the operation ##average([{random_float}, {random_float}]).",
            f"Their mathematical journey embraced the symphony of summation. They calculated the sum of elements in the list [{random_float}, {random_float}]. The result was revealed through the operation ##sum([{random_float}, {random_float}]).",
            f"As the friends dived into the cosmic depths of lists, they calculated the length of the list [{random_float}, {random_float}]. The result was obtained through the operation ##length([{random_float}, {random_float}]).",
            f"In a cosmic moment of symmetry, they compared strings. They checked if the strings '{random_float} {random_float}' and '{random_float} {random_float}' were the same using the operation ##check_same_string('{random_float} {random_float}', '{random_float} {random_float}').",
            f"To add a cosmic twist to their adventure, they explored the concept of cosmic reversal. They calculated the reverse of the string '{random_float} {random_float}' using the operation ##reverse_string('{random_float} {random_float}').",
            f"The cosmic odyssey continued as the friends explored the cosmic dot product of two vectors. They calculated the dot product of vectors [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was obtained through the operation ##calculate_dot_product([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their journey reached new cosmic heights as they explored the square of the cosmic sum of {random_int_one} and {random_int_two}. The result was obtained through the operation ##a_plus_b_whole_square({random_int_one}, {random_int_two}).",
            f"In a moment of cosmic poetry, they calculated the result of {random_int_one} squared plus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_squared_plus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The friends faced the cosmic challenge of {random_int_one} minus {random_int_two} whole squared plus 4 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_minus_b_whole_squared_plus_4ab({random_int_one}, {random_int_two}).",
            f"The cosmic adventure continued as they explored the cosmic result of {random_int_one} minus {random_int_two} whole squared.",
        ],
        [
            f"In the mystical realm of numerical exploration, they embarked on a quest to unravel the secrets of addition. Their journey began by adding {random_int_one} and {random_int_two}, bringing forth the result through the operation ##addition({random_int_one}, {random_int_two}).",
            f"As they traversed the enchanted landscape of mathematical mysteries, they encountered the ancient art of subtraction. In a dance of numbers, they subtracted {random_int_two} from {random_int_three}, revealing the result through the operation ##subtraction({random_int_three}, {random_int_two}).",
            f"Their expedition into the arcane depths of mathematics continued with the mystical art of multiplication. They multiplied the magical numbers {random_float} and {random_float}, unveiling the result through the operation ##multiplication({random_float}, {random_float}).",
            f"In a moment of mathematical harmony, they explored the essence of division. Dividing the ethereal value {random_float} by {random_float}, the result was gracefully revealed through the operation ##division({random_float}, {random_float}).",
            f"As they ascended to the celestial heights of mathematical power, they delved into the world of exponentiation. Raising {random_float} to the power of {random_float}, the result manifested through the operation ##exponentiation({random_float}, {random_float}).",
            f"Their senses tingled with enchantment as they sought the square root of {random_float}. The result, a mystical revelation, emerged through the operation ##square_root({random_float}).",
            f"In a journey through the ancient integers, they explored the sacred floor division. Dividing {random_int_four} by {random_int_three}, the result unfolded through the operation ##floor_division({random_int_four}, {random_int_three}).",
            f"As they unraveled the threads of the numerical fabric, they engaged with the enigmatic modulus operation. Calculating the modulus of {random_int_one} modulo {random_int_two}, the result became apparent through the operation ##modulus({random_int_one}, {random_int_two}).",
            f"Their journey through the mystical logarithmic realms led them to the calculation of the logarithm. With a base of {random_float}, they unveiled the logarithm of {random_float} through the operation ##logarithm({random_float}, {random_float}).",
            f"In a moment of trigonometric mystique, they calculated the sine of {random_float} radians. The result, a harmonious expression, was revealed through the operation ##sine({random_float}).",
            f"In a cosmic exploration, they calculated the result of raising {random_float} to the power of {random_float}. The result was obtained through the operation ##exponentiation({random_float}, {random_float}).",
            f"As they ventured into the realm of cosmic energies, they calculated the hyperbolic sine of {random_float}. The result was revealed through the operation ##hyperbolic_sine({random_float}).",
            f"In a quest for celestial harmony, they explored the logarithm of {random_float} with base {random_float}. The result was obtained through the operation ##logarithm({random_float}, {random_float}).",
            f"The mathematical journey embraced trigonometry as they calculated the tangent of {random_float} radians. The result was revealed through the operation ##tangent({random_float}).",
            f"In a moment of angular exploration, they calculated the arccosine of {random_float}. The result was obtained through the operation ##arccosine({random_float}).",
            f"They embarked on a journey through geometric shapes, calculating the area of a circle with a radius of {random_float}. The result was revealed through the operation ##circle_area({random_float}).",
            f"As they traversed through permutations, they calculated the permutation of {random_int_one} objects taken {random_int_two} at a time. The result was obtained through the operation ##permutation({random_int_one}, {random_int_two}).",
            f"In a combinatorial twist, they explored the combination of {random_int_one} objects taken {random_int_two} at a time. The result was revealed through the operation ##combination({random_int_one}, {random_int_two}).",
            f"They encountered a moment of inversion, exploring the inverted value of {random_float}. The result was obtained through the operation ##invert_number({random_float}).",
            f"To add a dynamic shift to their exploration, they converted the float value of {random_float} to an integer using the operation ##float_to_int({random_float}).",
            f"In a transformational phase, they converted the integer value of {random_int_one} to a float using the operation ##int_to_float({random_int_one}).",
            f"The friends then delved into the concept of series, calculating the sum of the first {random_int_one} terms of a geometric series with a first term of {random_float}, a common ratio of {random_float}, and {random_int_two} terms. The result was obtained through the operation ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"Their journey took a mystical turn as they explored the realm of mathematical functions. They applied the sigmoid function to {random_float}, and the result was revealed through the operation ##sigmoid({random_float}).",
            f"In the cosmic landscape of vectors, they explored cosine similarity. They calculated the cosine similarity between two vectors: [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was obtained through the operation ##cosine_similarity([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their adventure reached a moment of totient reflection as they encountered Euler's Totient function. They applied the Euler Totient function to {random_int_one}, and the result was obtained through the operation ##euler_totient({random_int_one}).",
            f"The friends navigated through vector spaces, exploring the concept of norms. They calculated the L1 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l1_norm([{random_float}, {random_float}]).",
            f"Continuing their exploration of norms, they calculated the L2 norm of the vector [{random_float}, {random_float}]. The result was revealed through the operation ##l2_norm([{random_float}, {random_float}]).",
            f"In the quest for harmonious averages, they calculated the average of elements in the list [{random_float}, {random_float}]. The result was obtained through the operation ##average([{random_float}, {random_float}]).",
            f"Their mathematical journey embraced the symphony of summation. They calculated the sum of elements in the list [{random_float}, {random_float}]. The result was revealed through the operation ##sum([{random_float}, {random_float}]).",
            f"As the friends dived into the cosmic depths of lists, they calculated the length of the list [{random_float}, {random_float}]. The result was obtained through the operation ##length([{random_float}, {random_float}]).",
            f"In a cosmic moment of symmetry, they compared strings. They checked if the strings '{random_float} {random_float}' and '{random_float} {random_float}' were the same using the operation ##check_same_string('{random_float} {random_float}', '{random_float} {random_float}').",
            f"To add a cosmic twist to their adventure, they explored the concept of cosmic reversal. They calculated the reverse of the string '{random_float} {random_float}' using the operation ##reverse_string('{random_float} {random_float}').",
            f"The cosmic odyssey continued as the friends explored the cosmic dot product of two vectors. They calculated the dot product of vectors [{random_float}, {random_float}] and [{random_float}, {random_float}]. The result was obtained through the operation ##calculate_dot_product([{random_float}, {random_float}], [{random_float}, {random_float}]).",
            f"Their journey reached new cosmic heights as they explored the square of the cosmic sum of {random_int_one} and {random_int_two}. The result was obtained through the operation ##a_plus_b_whole_square({random_int_one}, {random_int_two}).",
            f"In a moment of cosmic poetry, they calculated the result of {random_int_one} squared plus 2 times {random_int_one} times {random_int_two} plus {random_int_two} squared. The result was obtained through the operation ##a_squared_plus_2ab_plus_b_squared({random_int_one}, {random_int_two}).",
            f"The friends faced the cosmic challenge of {random_int_one} minus {random_int_two} whole squared plus 4 times {random_int_one} times {random_int_two}. The result was obtained through the operation ##a_minus_b_whole_squared_plus_4ab({random_int_one}, {random_int_two}).",
            f"The cosmic adventure continued as they explored the cosmic result of {random_int_one} minus {random_int_two} whole squared."
        ],
    ]
    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator

    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_fourteen_example_paragraph(),
    )
    sample = Utility.create_sample_from_example(
        masked_example,
        PretrainTasks.MASKED_TOKEN_PREDICTION,
    )
    print(sample)

    from next_token_sample_generator import NextTokenSamplesGenerator

    next_token_example = NextTokenSamplesGenerator.create_next_token_batches(
        get_batch_fourteen_example_paragraph(),
    )
    sample = Utility.create_sample_from_example(
        next_token_example,
        PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
