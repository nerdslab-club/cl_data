import random

import spacy

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_masked_token_batch_two_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_two_example_paragraph()
        for paragraph in paragraphs:
            masked_data = Utility.create_masked_input_output_example(paragraph, nlp)
            examples.extend(masked_data)
    return examples


def create_next_token_batch_two_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_two_example_paragraph()
        for paragraph in paragraphs:
            next_token_data = Utility.create_next_word_input_output_example(
                paragraph, nlp
            )
            examples.extend(next_token_data)
    return examples


def __get_batch_two_example_paragraph():
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
        # [
        #     f"In a mystical land, there were three wizards named X, A, and B. Each of them possessed unique powers.",
        #     f"Wizard X had the power to multiply any two numbers with his spell. Once, he used his magic to find {random_int_one} multiplied by {random_int_four}, which resulted in ##positive_2ab({random_int_one},{random_int_four}).",
        #     f"Meanwhile, Wizard B had the power to create intricate mathematical patterns. He discovered a pattern in the equation x^2 + {random_int_one} + {random_int_two} * x + {random_int_two} * {random_int_one}. This pattern could be rewritten as ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one},{random_int_two},{random_int_two}).",
        #     f"One day, the three wizards collaborated on a complex problem. They needed to calculate the sum of cubes: {random_int_one}^3 + {random_int_two}^3. With their combined efforts, they found the answer to be ##a_cubed_plus_b_cubed({random_int_one},{random_int_two}).",
        #     f"As they continued their journey, they encountered a magical equation: (A + B)^3 - 3 * A * B * (A + B). Wizard X used his multiplication spell to simplify it to ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one},{random_int_two}).",
        #     f"The wizards were intrigued by another equation: (A + B) * (A^2 - A * B + B^2). Wizard A transformed it into ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_one},{random_int_two}).",
        #     f"Suddenly, they stumbled upon a mysterious artifact with the inscription: A^3 - B^3. After performing the calculation, they realized it equaled ##a_cubed_minus_b_cubed({random_int_one},{random_int_two}).",
        #     f"In the depths of their exploration, they encountered the equation (A - B)^3 + 3 * A * B * (A - B). With a touch of magic, it transformed into ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_one},{random_int_two}).",
        #     f"The wizards marveled at their mathematical journey, realizing that every challenge they faced could be conquered through the art of calculation.",
        # ],
        # [
        #     f"In a world where numbers held incredible power, there lived a young mathematician named Alex.",
        #     f"One day, Alex faced a challenge - to find the sum of {random_int_one} and {random_int_two}. With a swift calculation, the answer was ##addition({random_int_one},{random_int_two}).",
        #     f"As the sun set, Alex encountered a puzzle - the difference between {random_int_two} and {random_int_three}. The solution was revealed through ##subtraction({random_int_two},{random_int_three}).",
        #     f"Under a starlit sky, Alex's thoughts turned to the cosmos. How about the product of {random_float:.2f} and {random_int_four}? The answer shone through ##multiplication({random_float},{random_int_four}).",
        #     f"Amidst the mysteries of the universe, Alex wondered about the division of {random_float:.2f} by {random_int_one}. The secret was unveiled by ##division({random_float},{random_int_one}).",
        #     f"Empowered by knowledge, Alex contemplated raising {random_int_three} to the power of {random_int_four}. The solution gleamed with ##exponentiation({random_int_three},{random_int_four}).",
        #     f"One moonlit night, a mystical riddle emerged - the square root of {random_int_four}. The answer lay within ##square_root({random_int_four}).",
        #     f"As the dawn broke, Alex encountered a challenge - floor division of {random_int_two} by {random_int_one}. The answer surfaced through ##floor_division({random_int_two},{random_int_one}).",
        #     f"In the realm of remainders, Alex deciphered the modulus of {random_int_three} divided by {random_int_one}. The answer emerged through ##modulus({random_int_three},{random_int_one}).",
        #     f"The ancient scrolls spoke of logarithms. Alex contemplated the logarithm of {random_float:.2f} with base {random_int_two}. The answer revealed itself through ##logarithm({random_float},{random_int_two}).",
        #     f"In the tranquil valley, Alex connected with trigonometry. The sine of an angle {random_float:.2f} degrees was uncovered through ##sine({random_float}).",
        #     f"With each calculation, Alex's understanding deepened, and the world of mathematics unfolded new wonders at every turn.",
        # ],
        # [
        #     f"In a land where mathematical wonders abound, there was a town named Arctopia. The town's population, {random_list}, was fascinated by the mystical properties of numbers.",
        #     f"One day, a curious mathematician decided to explore the depths of trigonometry. Armed with a random angle value, {random_float}, the mathematician delved into the world of cosine.",
        #     f"The cosine of {random_float} radians was ##cosine({random_float}). This value intrigued the mathematician, who decided to find its tangent.",
        #     f"Calculating the tangent of ##arccosine({random_float}), the mathematician stumbled upon a hidden truth.",
        #     f"Meanwhile, on the other side of town, another mathematician was engrossed in hyperbolic equations. They pondered over the hyperbolic sine of {random_int_one}.",
        #     f"As the sun set, casting long shadows, a group of young students gathered to unravel logarithmic mysteries. They calculated the base-10 logarithm of {random_int_two}, discovering a peculiar pattern.",
        #     f"Among them, a prodigious child wondered about the cube root of ##hyperbolic_tangent({random_int_three}).",
        #     f"Lost in thought, a seasoned professor contemplated the profound question: What is the result of ##logarithm_base_2({random_int_four}) raised to the power of ##arcsine({random_float})?",
        #     f"In a twist of fate, the two mathematicians crossed paths and decided to combine their knowledge. They embarked on a journey to solve the equation ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
        #     f"After intense calculations, they found the solution: {random_int_two + random_int_four}. Overwhelmed by their success, the townspeople celebrated with a grand feast, and the legend of Arctopia's mathematical marvels lived on.",
        # ],
        # [
        #     f"In a realm where mathematics governed every aspect of life, a grand adventure was about to unfold.",
        #     f"A brave explorer set out on a journey to convert angles from degrees to radians. They began with an angle of {random_int_one} degrees, which is ##degrees_to_radians({random_int_one}).",
        #     f"Guided by the stars, the explorer ventured into the world of number theory. They encountered two mysterious numbers, {random_int_two} and {random_int_three}, and calculated their greatest common divisor: ##gcd({random_int_two}, {random_int_three}).",
        #     f"Continuing their quest, the explorer encountered a pair of ancient scrolls that spoke of the least common multiple. They performed the ritual of LCM and revealed the secret of {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
        #     f"As dawn broke, illuminating the path ahead, the explorer faced a mountain of challenges. They summoned the power of the isqrt function to find the integer square root of {random_int_three}, which turned out to be ##isqrt({random_int_three}).",
        #     f"With newfound confidence, the explorer harnessed the power of modular arithmetic. They raised {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, and the result was ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
        #     f"But the journey was not without its ups and downs. The explorer encountered a treacherous terrain of floating points. They used the ancient techniques of ceil, floor, and round to navigate through the obstacles.",
        #     f"In a moment of reflection, the explorer contemplated the absolute difference between two mystical numbers, {random_float} and {random_int_four}. The answer was revealed: ##absolute_difference({random_float}, {random_int_four}).",
        #     f"As the explorer's odyssey neared its end, they realized that every calculation, every function, was a step closer to unraveling the mysteries of the mathematical universe.",
        #     f"And so, with a heart full of knowledge and a mind teeming with mathematical wonders, the explorer returned to their homeland, sharing the tale of their extraordinary journey and inspiring generations to come.",
        # ],
        # [
        #     f"The greatest value between {random_float} and {random_int_one} is ##greatest_value({random_float}, {random_int_one}).",
        #     f"The smallest value between {random_int_two} and {random_float} is ##smallest_value({random_int_two}, {random_float}).",
        #     f"The product of the numbers {random_list} is ##product({random_list}).",
        #     f"The factorial of {random_int_one} is ##factorial({random_int_one}).",
        #     f"The statement '{random_int_two} is prime' is ##is_prime({random_int_two}).",
        #     f"The prime factors of {random_int_three} are ##prime_factors({random_int_three}).",
        #     f"The number {random_int_four} is a perfect square: ##is_perfect_square({random_int_four}).",
        #     f"The number {random_int_three} is a perfect cube: ##is_perfect_cube({random_int_three}).",
        #     f"The mean of the numbers {random_list} is ##mean({random_list}).",
        #     f"The median of the numbers {random_list} is ##median({random_list})."
        # ],
        [
            f"Once upon a time, in a land filled with mathematical wonders...",
            f"A brave adventurer found a list of numbers: {random_list}.",
            f"The adventurer applied ascending sort to the list and obtained: ##ascending_sort({random_list}).",
            f"Among these numbers, an intriguing integer appeared: {random_int_one}.",
            f"The adventurer pondered its properties. Was it even? It turned out to be ##is_even({random_int_one}).",
            f"The adventurer also considered its square: ##square_int({random_int_one}).",
            f"Meanwhile, a floating point number, {random_float}, floated by.",
            f"The adventurer calculated its square: ##square({random_float}).",
            f"Later, they encountered the enigmatic power of ten: ##power_of_ten({random_float}).",
            f"A different integer emerged: {random_int_two}.",
            f"The adventurer questioned its oddness. Was it odd? The answer was ##is_odd({random_int_two}).",
            f"Curious about its absolute value, the adventurer found: ##absolute({random_int_two}).",
            f"In a twist of fate, another integer, {random_int_three}, entered the scene.",
            f"They wondered about its cube: ##cube({random_int_three}).",
            f"The cube root of this cube was sought after: ##cube_root(##cube({random_int_three})).",
            f"But even more excitement awaited! A boolean arrived: {random_bool}.",
            f"The adventurer thought about the ReLU activation of {random_float}: ##relu({random_float}).",
            f"As their journey continued, an unexpected integer joined: {random_int_four}.",
            f"The adventurer was captivated by its descent: ##descending_sort([{random_int_four}, {random_int_two}, {random_int_one}]).",
            f"The mathematical tale continued, filled with calculations and discoveries...",
            f"And so, the adventurer's quest through the realm of numbers continued, guided by the magic of mathematics.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    masked_example = create_masked_token_batch_two_example(1, Utility.get_spacy_nlp())
    print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example, PretrainTasks.MASKED_TOKEN_PREDICTION
    )
    print(sample)
#
#     next_token_example = create_next_token_batch_two_example(1, Utility.get_spacy_nlp())
#     print(len(next_token_example), next_token_example)
