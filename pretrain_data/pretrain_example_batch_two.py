import random

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def get_batch_two_example_paragraph():
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
            f"In a mystical land, there were three wizards named X, A, and B. Each of them possessed unique powers.",
            f"Wizard X had the power to multiply any two numbers with his spell. Once, he used his magic to find {random_int_one} multiplied by {random_int_four}, which resulted in ##positive_2ab({random_int_one},{random_int_four}).",
            f"Meanwhile, Wizard B had the power to create intricate mathematical patterns. He discovered a pattern in the equation x^2 + {random_int_one} + {random_int_two} * x + {random_int_two} * {random_int_one}. This pattern could be rewritten as ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one},{random_int_two},{random_int_two}).",
            f"One day, the three wizards collaborated on a complex problem. They needed to calculate the sum of cubes: {random_int_one}^3 + {random_int_two}^3. With their combined efforts, they found the answer to be ##a_cubed_plus_b_cubed({random_int_one},{random_int_two}).",
            f"As they continued their journey, they encountered a magical equation: (A + B)^3 - 3 * A * B * (A + B). Wizard X used his multiplication spell to simplify it to ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one},{random_int_two}).",
            f"The wizards were intrigued by another equation: (A + B) * (A^2 - A * B + B^2). Wizard A transformed it into ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"Suddenly, they stumbled upon a mysterious artifact with the inscription: A^3 - B^3. After performing the calculation, they realized it equaled ##a_cubed_minus_b_cubed({random_int_one},{random_int_two}).",
            f"In the depths of their exploration, they encountered the equation (A - B)^3 + 3 * A * B * (A - B). With a touch of magic, it transformed into ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_one},{random_int_two}).",
            f"The wizards marveled at their mathematical journey, realizing that every challenge they faced could be conquered through the art of calculation.",
        ],
        [
            f"In a world where numbers held incredible power, there lived a young mathematician named Alex.",
            f"One day, Alex faced a challenge - to find the sum of {random_int_one} and {random_int_two}. With a swift calculation, the answer was ##addition({random_int_one},{random_int_two}).",
            f"As the sun set, Alex encountered a puzzle - the difference between {random_int_two} and {random_int_three}. The solution was revealed through ##subtraction({random_int_two},{random_int_three}).",
            f"Under a starlit sky, Alex's thoughts turned to the cosmos. How about the product of {random_float:.2f} and {random_int_four}? The answer shone through ##multiplication({random_float},{random_int_four}).",
            f"Amidst the mysteries of the universe, Alex wondered about the division of {random_float:.2f} by {random_int_one}. The secret was unveiled by ##division({random_float},{random_int_one}).",
            f"Empowered by knowledge, Alex contemplated raising {random_int_three} to the power of {random_int_four}. The solution gleamed with ##exponentiation({random_int_three},{random_int_four}).",
            f"One moonlit night, a mystical riddle emerged - the square root of {random_int_four}. The answer lay within ##square_root({random_int_four}).",
            f"As the dawn broke, Alex encountered a challenge - floor division of {random_int_two} by {random_int_one}. The answer surfaced through ##floor_division({random_int_two},{random_int_one}).",
            f"In the realm of remainders, Alex deciphered the modulus of {random_int_three} divided by {random_int_one}. The answer emerged through ##modulus({random_int_three},{random_int_one}).",
            f"The ancient scrolls spoke of logarithms. Alex contemplated the logarithm of {random_float:.2f} with base {random_int_two}. The answer revealed itself through ##logarithm({random_float},{random_int_two}).",
            f"In the tranquil valley, Alex connected with trigonometry. The sine of an angle {random_float:.2f} degrees was uncovered through ##sine({random_float}).",
            f"With each calculation, Alex's understanding deepened, and the world of mathematics unfolded new wonders at every turn.",
        ],
        [
            f"In a land where mathematical wonders abound, there was a town named Arctopia. The town's population, {random_list}, was fascinated by the mystical properties of numbers.",
            f"One day, a curious mathematician decided to explore the depths of trigonometry. Armed with a random angle value, {random_float}, the mathematician delved into the world of cosine.",
            f"The cosine of {random_float} radians was ##cosine({random_float}). This value intrigued the mathematician, who decided to find its tangent.",
            f"Calculating the tangent of ##arccosine({random_float}), the mathematician stumbled upon a hidden truth.",
            f"Meanwhile, on the other side of town, another mathematician was engrossed in hyperbolic equations. They pondered over the hyperbolic sine of {random_int_one}.",
            f"As the sun set, casting long shadows, a group of young students gathered to unravel logarithmic mysteries. They calculated the base-10 logarithm of {random_int_two}, discovering a peculiar pattern.",
            f"Among them, a prodigious child wondered about the cube root of ##hyperbolic_tangent({random_int_three}).",
            f"Lost in thought, a seasoned professor contemplated the profound question: What is the result of ##logarithm_base_2({random_int_four}) raised to the power of ##arcsine({random_float})?",
            f"In a twist of fate, the two mathematicians crossed paths and decided to combine their knowledge. They embarked on a journey to solve the equation ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
            f"After intense calculations, they found the solution: {random_int_two + random_int_four}. Overwhelmed by their success, the townspeople celebrated with a grand feast, and the legend of Arctopia's mathematical marvels lived on.",
        ],
        [
            f"In a realm where mathematics governed every aspect of life, a grand adventure was about to unfold.",
            f"A brave explorer set out on a journey to convert angles from degrees to radians. They began with an angle of {random_int_one} degrees, which is ##degrees_to_radians({random_int_one}).",
            f"Guided by the stars, the explorer ventured into the world of number theory. They encountered two mysterious numbers, {random_int_two} and {random_int_three}, and calculated their greatest common divisor: ##gcd({random_int_two}, {random_int_three}).",
            f"Continuing their quest, the explorer encountered a pair of ancient scrolls that spoke of the least common multiple. They performed the ritual of LCM and revealed the secret of {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
            f"As dawn broke, illuminating the path ahead, the explorer faced a mountain of challenges. They summoned the power of the isqrt function to find the integer square root of {random_int_three}, which turned out to be ##isqrt({random_int_three}).",
            f"With newfound confidence, the explorer harnessed the power of modular arithmetic. They raised {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, and the result was ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
            f"But the journey was not without its ups and downs. The explorer encountered a treacherous terrain of floating points. They used the ancient techniques of ceil, floor, and round to navigate through the obstacles.",
            f"In a moment of reflection, the explorer contemplated the absolute difference between two mystical numbers, {random_float} and {random_int_four}. The answer was revealed: ##absolute_difference({random_float}, {random_int_four}).",
            f"As the explorer's odyssey neared its end, they realized that every calculation, every function, was a step closer to unraveling the mysteries of the mathematical universe.",
            f"And so, with a heart full of knowledge and a mind teeming with mathematical wonders, the explorer returned to their homeland, sharing the tale of their extraordinary journey and inspiring generations to come.",
        ],
        [
            f"The greatest value between {random_float} and {random_int_one} is ##greatest_value({random_float}, {random_int_one}).",
            f"The smallest value between {random_int_two} and {random_float} is ##smallest_value({random_int_two}, {random_float}).",
            f"The product of the numbers {random_list} is ##product({random_list}).",
            f"The factorial of {random_int_one} is ##factorial({random_int_one}).",
            f"The statement '{random_int_two} is prime' is ##is_prime({random_int_two}).",
            f"The prime factors of {random_int_three} are ##prime_factors({random_int_three}).",
            f"The number {random_int_four} is a perfect square: ##is_perfect_square({random_int_four}).",
            f"The number {random_int_three} is a perfect cube: ##is_perfect_cube({random_int_three}).",
            f"The mean of the numbers {random_list} is ##mean({random_list}).",
            f"The median of the numbers {random_list} is ##median({random_list}).",
        ],
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
        ],
        [
            f"Once upon a time, there was a list of numbers: {random_list}.",
            f"The maximum value in the list was ##max_value({random_list}).",
            f"The minimum value in the list was ##min_value({random_list}).",
            f"Amidst the calculations, a random integer appeared: {random_int_one}.",
            f"It then combined with another random integer, resulting in {random_int_two}.",
            f"This new integer combined once more, forming {random_int_three}.",
            f"A random float, {random_float}, floated into the story as well.",
            f"Through the use of mathematical power, the cube root of {random_int_one} was calculated to be ##nth_root({random_int_one}, 3).",
            f"Geometrically, the mean of the numbers in the list was ##geometric_mean({random_list}).",
            f"A curious question arose: was {random_int_one} a power of two? The answer was ##is_power_of_two({random_int_one}).",
            f"Binary code entered the scene: ##decimal_to_binary({random_int_one}) represented {random_int_one} in binary.",
            f"Decimal magic followed: ##binary_to_decimal(##decimal_to_binary({random_int_one})) emerged as the result.",
            f"In a twist of characters, {random_int_one} revealed itself to be a palindrome: ##is_palindrome({random_int_one}).",
            f"Meanwhile, the digits of {random_int_two} added up to ##sum_of_digits({random_int_two}).",
            f"In the realm of right triangles, with sides {random_int_one} and {random_int_two}, the hypotenuse was ##hypotenuse({random_int_one}, {random_int_two}).",
            f"The story came to an end, leaving behind a trail of calculations and mathematical marvels.",
        ],
        [
            f"The area of a circle with radius {random_float} is ##circle_area({random_float}).",
            f"The permutation of {random_int_one} and {random_int_two} is ##permutation({random_int_one}, {random_int_two}).",
            f"The combination of {random_int_two} and {random_int_three} is ##combination({random_int_two}, {random_int_three}).",
            f"The inverted value of {random_float} is ##invert_number({random_float}).",
            f"The integer part of {random_float} is ##float_to_int({random_float}).",
            f"The float representation of {random_int_three} is ##int_to_float({random_int_three}).",
            f"The sum of a geometric series with initial term {random_float}, common ratio {random_float}, and {random_int_one} terms is ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"The sigmoid value of {random_float} is ##sigmoid({random_float}).",
            f"The cosine similarity between {random_list} and {random_list} is ##cosine_similarity(eval({random_list}), eval({random_list})).",
            f"The Euler's totient function value for {random_int_four} is ##euler_totient({random_int_four}).",
        ],
        [
            f"Once upon a time, in a land of numbers, there lived a vector with elements {random_list}.",
            f"This vector had a length of ##length({random_list}).",
            f"Its L1 norm was ##l1_norm({random_list}), and its L2 norm was ##l2_norm({random_list}).",
            f"Meanwhile, there were four integers in the kingdom: {random_int_one}, {random_int_two}, {random_int_three}, and {random_int_four}.",
            f"The sum of the first two integers was ##sum([{random_int_one}, {random_int_two}]), while the sum of all four was ##sum([{random_int_one}, {random_int_two}, {random_int_three}, {random_int_four}]).",
            f"An average ruler was calculated using the integers {random_int_one}, {random_int_two}, and {random_int_three}. The result was ##average([{random_int_one}, {random_int_two}, {random_int_three}]).",
            f"Randomness was afoot as a floating point number, {random_float}, entered the scene.",
            f"A Boolean dilemma was solved when it was determined that the value of truth was indeed {random_bool}.",
            f"The mystical value π was summoned, and its presence brought joy: ##get_pi().",
            f"Similarly, the constant e appeared as if by magic: ##get_e().",
            f"Two vectors with elements {random_list} and {random_list} embarked on a journey to find their dot product.",
            f"After a grand calculation, their dot product was revealed to be ##calculate_dot_product({random_list}, {random_list}).",
            f"In a surprising twist, strings were involved. 'Racecar' remained the same when reversed: ##check_same_string('racecar', ##reverse_string('racecar')).",
            f"The kingdom was full of mathematical wonders, where calculations and numbers ruled the day.",
        ],
        [
            f"In the land of Mathville, lived two friends named {random_list[0]} and {random_list[1]}.",
            f"They were always curious about numbers. One day, {random_list[0]} discovered that the square of the sum of two numbers can be calculated using a formula:",
            f"{random_int_one} plus {random_int_two} whole square equals ##a_plus_b_whole_square({random_int_one},{random_int_two}).",
            f"This formula can also be expanded as: ({random_int_one} squared) plus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared), which results in ##a_squared_plus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"Meanwhile, {random_list[1]} found another interesting formula. The square of the difference between two numbers plus 4 times their product has a formula:",
            f"({random_int_two} minus {random_int_three}) whole squared plus (4 times {random_int_two} times {random_int_three}), which is ##a_minus_b_whole_squared_plus_4ab({random_int_two},{random_int_three}).",
            f"Later, they learned that the square of the difference between two numbers also has a simplified form:",
            f"({random_int_one} minus {random_int_four}) whole squared equals ##a_minus_b_whole_squared({random_int_one},{random_int_four}).",
            f"As their exploration continued, they came across the formula for the difference of squares:",
            f"The difference between the squares of {random_int_one} and {random_int_two} can be computed as ({random_int_one} squared) minus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared), resulting in ##a_squared_minus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"They also learned that the square of the sum of two numbers minus 4 times their product can be expressed as:",
            f"({random_int_two} plus {random_int_three}) whole squared minus (4 times {random_int_two} times {random_int_three}), which equals ##a_plus_b_whole_squared_minus_4ab({random_int_two},{random_int_three}).",
            f"As the friends continued their journey, they encountered a simple yet beautiful relation:",
            f"The sum of the squares of {random_int_two} and {random_int_three} is given by ({random_int_two} squared) plus ({random_int_three} squared), which equals ##a_squared_plus_b_squared({random_int_two},{random_int_three}).",
            f"And so, their mathematical adventure in Mathville continued, fueled by their passion for numbers and calculations.",
        ],
    ]

    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator

    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_two_example_paragraph(),
        1,
    )
    # print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example,
        PretrainTasks.MASKED_TOKEN_PREDICTION,
    )
    print(sample)

    from next_token_sample_generator import NextTokenSamplesGenerator

    next_token_example = NextTokenSamplesGenerator.create_next_token_batches(
        get_batch_two_example_paragraph(),
        1,
    )
    sample = Utility.create_sample_from_example(
        next_token_example, PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
