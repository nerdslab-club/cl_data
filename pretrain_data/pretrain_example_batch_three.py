import random

import spacy

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_masked_token_batch_three_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_three_example_paragraph()
        for paragraph in paragraphs:
            masked_data = Utility.create_masked_input_output_example(paragraph, nlp)
            examples.extend(masked_data)
    return examples


def create_next_token_batch_three_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_three_example_paragraph()
        for paragraph in paragraphs:
            next_token_data = Utility.create_next_word_input_output_example(
                paragraph, nlp
            )
            examples.extend(next_token_data)
    return examples


def __get_batch_three_example_paragraph():
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
        #     f"Once upon a time in the land of Mathovia, there lived two curious friends, Alex and Emma.",
        #     f"Alex was fascinated by the power of mathematics, and Emma shared his enthusiasm. One day, they stumbled upon a mysterious equation: -2ab.",
        #     f"Alex, always seeking the negative side of things, pondered the value of -2ab for a = {random_int_one} and b = {random_int_two}. He concluded that it was ##negative_2ab({random_int_one},{random_int_two}).",
        #     f"Emma, on the other hand, embraced positivity. She wanted to find the positive side of -2ab, using the same values a = {random_int_one} and b = {random_int_two}. She gleefully discovered it as ##positive_2ab({random_int_one},{random_int_two}).",
        #     f"Curiosity guiding their steps, Alex and Emma embarked on a mathematical journey. They encountered a magical formula that involved expressions of the form x + a * x + b.",
        #     f"Alex, taking the lead, calculated the result of x + {random_int_one} * x + {random_int_two} for x = {random_int_three}. The answer was ##x_plus_a_times_x_plus_b({random_int_three},{random_int_one},{random_int_two}).",
        #     f"Emma, intrigued by the blend of squares and additions, decided to explore x^2 + a + b * x + ab. For x = {random_int_four}, she discovered the value as ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_four},{random_int_one},{random_int_two}).",
        #     f"Their journey continued, and they stumbled upon the enigma of a^3 + b^3. Emma, a lover of cubes, eagerly solved it for a = {random_int_one} and b = {random_int_two}. The solution was ##a_cubed_plus_b_cubed({random_int_one},{random_int_two}).",
        #     f"Alex, intrigued by the idea of cubes, took on the challenge of (a + b)^3 - 3ab(a + b). With a = {random_int_one} and b = {random_int_two}, he solved the equation as ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one},{random_int_two}).",
        #     f"Emma, enchanted by the art of multiplication, ventured into (a + b) * a^2 - ab + b^2. With a = {random_int_one} and b = {random_int_two}, she unraveled the answer as ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_one},{random_int_two}).",
        #     f"Their mathematical exploration led them to the intricacies of a^3 - b^3. Alex, with his analytical mind, calculated the value for a = {random_int_one} and b = {random_int_two} as ##a_cubed_minus_b_cubed({random_int_one},{random_int_two}).",
        #     f"Emma, ever the solver of puzzles, delved into (a - b)^3 + 3ab(a - b). She found the solution with a = {random_int_one} and b = {random_int_two} as ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_one},{random_int_two}).",
        #     f"Through their journey, Alex and Emma learned that mathematics was not just about numbers, but about the intricate dance of operations that brought the world of numbers to life.",
        #     f"United in their love for mathematical mysteries, they continued their exploration, unraveling the secrets hidden within the numbers and equations that shaped the fabric of Mathovia.",
        # ],
        # [
        #     f"Once upon a time in the realm of numbers, there was a young mathematician named Ava.",
        #     f"Ava embarked on a journey to unlock the secrets of addition. Her quest began by combining {random_int_one} and {random_int_two}, revealing the answer through ##addition({random_int_one},{random_int_two}).",
        #     f"As Ava ventured further, she encountered the enigma of subtraction. The difference between {random_int_two} and {random_int_three} was unveiled by ##subtraction({random_int_two},{random_int_three}).",
        #     f"In her pursuit of wisdom, Ava turned her attention to the mysteries of multiplication. The product of {random_float:.2f} and {random_int_four} was deciphered using ##multiplication({random_float},{random_int_four}).",
        #     f"Ava's quest for knowledge took her to the realm of division. The division of {random_float:.2f} by {random_int_one} revealed its hidden truth through ##division({random_float},{random_int_one}).",
        #     f"The path to empowerment led Ava to the realm of exponents. She raised {random_int_three} to the power of {random_int_four}, unlocking the solution with ##exponentiation({random_int_three},{random_int_four}).",
        #     f"One moonlit night, Ava faced the challenge of the square root. The square root of {random_int_four} was unveiled through ##square_root({random_int_four}).",
        #     f"As dawn broke, Ava encountered a puzzle - floor division of {random_int_two} by {random_int_one}. The answer emerged through ##floor_division({random_int_two},{random_int_one}).",
        #     f"In the labyrinth of numbers, Ava navigated the realm of remainders. The modulus of {random_int_three} divided by {random_int_one} was revealed through ##modulus({random_int_three},{random_int_one}).",
        #     f"Ava's insatiable curiosity led her to logarithms. She calculated the logarithm of {random_float:.2f} with base {random_int_two} using ##logarithm({random_float},{random_int_two}).",
        #     f"In the tranquil valley, Ava connected with trigonometry. The sine of an angle {random_float:.2f} degrees was unveiled through ##sine({random_float}).",
        #     f"With each revelation, Ava's understanding deepened, and the world of mathematics continued to unfold its mesmerizing wonders.",
        # ],
        # [
        #     f"In the enchanting realm of Arctopia, a land steeped in mathematical wonders, a town thrived with a population of {random_list} who were mesmerized by the mystical properties of numbers.",
        #     f"One fateful day, an inquisitive mathematician embarked on a quest to explore the hidden realms of trigonometry. Armed with a mysterious angle value, {random_float}, the mathematician delved into the realm of cosine.",
        #     f"The radiant cosmos revealed the secret of the cosine of {random_float} radians: ##cosine({random_float}). The enigma deepened as the mathematician sought the tangent of this revelation.",
        #     f"In the heart of mathematical exploration, the tangent of ##arccosine({random_float}) was unveiled, unraveling profound truths.",
        #     f"Across Arctopia, another mathematician delved into the realm of hyperbolic equations. Their focus was the hyperbolic sine of {random_int_one}, a number with untold significance.",
        #     f"As twilight painted long shadows, young scholars gathered to unlock the mysteries of logarithms. They unveiled the enigmatic base-10 logarithm of {random_int_two}, uncovering a pattern that defied convention.",
        #     f"Amid the curious minds, a prodigious child pondered the enigma of the cube root of ##hyperbolic_tangent({random_int_three}), a conundrum wrapped in the fabric of mathematics.",
        #     f"In a parallel pursuit of wisdom, a venerable sage contemplated the riddle: What happens when the potent essence of ##logarithm_base_2({random_int_four}) is raised to the celestial power of ##arcsine({random_float})?",
        #     f"As fate wove its tapestry, the paths of these two mathematicians intertwined. Together, they embarked on a journey to decipher the cryptic equation ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
        #     f"After arduous calculations, the answer was unveiled: {random_int_two + random_int_four}. The townsfolk rejoiced, celebrating the triumph of knowledge with a grand feast, and the legend of Arctopia's mathematical marvels reverberated through time."
        # ],
        # [
        #     f"In a land where the language was numbers and the air was filled with the scent of calculations, a young mathematician embarked on an extraordinary journey.",
        #     f"Armed with an angle of {random_int_one} degrees, the mathematician sought to translate it into the language of radians using the arcane formula of degrees_to_radians: ##degrees_to_radians({random_int_one}).",
        #     f"On their path, they stumbled upon an enigmatic door that could only be opened with the key of greatest common divisor. With {random_int_two} and {random_int_three} as the key's teeth, the door swung open: ##gcd({random_int_two}, {random_int_three}).",
        #     f"Venturing deeper, the mathematician uncovered the ancient scroll of least common multiple, revealing its secrets for {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
        #     f"In a forest shrouded in mystery, the mathematician encountered an age-old tree that grew only integer roots. They invoked the isqrt incantation to discover that the tree's age was ##isqrt({random_int_three}).",
        #     f"Stepping into a realm of congruence, the mathematician wielded the power of pow_mod, raising {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, yielding the answer: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
        #     f"Time flowed like a river, and the mathematician navigated the currents using the tools of ceil, floor, and round. The river's surface held the reflection of the absolute difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
        #     f"In the heart of this mathematical world, the mathematician realized that every function was a portal to a deeper realm, where patterns and truths awaited discovery.",
        #     f"And so, with a mind illuminated by the beauty of numbers, the mathematician returned to their people, sharing the story of their journey. Their tale ignited a passion for mathematics, inspiring generations to explore the endless landscapes of calculation and wonder.",
        # ],
        # [
        #     f"Once upon a time, in a world where math governed everything, there was a curious mathematician.",
        #     f"This mathematician wondered about the greatest value between {random_float} and {random_int_one}. After some calculations,",
        #     f"they found that the answer was ##greatest_value({random_float}, {random_int_one}).",
        #     f"Continuing their exploration, they pondered the smallest value between {random_int_two} and {random_float}.",
        #     f"After meticulous calculations, they uncovered that the answer was ##smallest_value({random_int_two}, {random_float}).",
        #     f"The mathematician then turned their attention to a mystical list of numbers: {random_list}.",
        #     f"They discovered that the product of these numbers was ##product({random_list}).",
        #     f"As their journey into the realm of numbers continued, they encountered the number {random_int_one}.",
        #     f"The mathematician delved into the factorial of this number, finding it to be ##factorial({random_int_one}).",
        #     f"Curious about prime numbers, they investigated whether {random_int_two} was a prime number.",
        #     f"The outcome was revealed to be ##is_prime({random_int_two}).",
        #     f"Next, they embarked on a quest to find the prime factors of {random_int_three}, uncovering ##prime_factors({random_int_three}).",
        #     f"As the sun set, the mathematician gazed at the night sky and contemplated {random_int_four}.",
        #     f"They realized that this number was a perfect square: ##is_perfect_square({random_int_four}).",
        #     f"But the mysteries were not over, for they also deduced that {random_int_three} was a perfect cube: ##is_perfect_cube({random_int_three}).",
        #     f"Equipped with their insights, the mathematician analyzed the numbers from the list again: {random_list}.",
        #     f"They determined that the mean of these numbers was ##mean({random_list}).",
        #     f"In the end, the mathematician's adventure led them to understand the median of the numbers as well: ##median({random_list}).",
        #     f"And so, their journey through the world of mathematics continued, always seeking new truths."
        # ],
        [
            f"Once upon a time, in the realm of numbers...",
            f"A bold explorer stumbled upon a list of mystic numbers: {random_list}.",
            f"Applying the magic of ascending sort, the explorer transformed them into: ##ascending_sort({random_list}).",
            f"Amidst these numbers, a curious integer appeared: {random_int_one}.",
            f"The explorer contemplated its essence. Was it even? The answer was revealed: ##is_even({random_int_one}).",
            f"The explorer then unlocked its hidden power, revealing its square: ##square_int({random_int_one}).",
            f"But wait, a shimmering floating point number, {random_float}, materialized.",
            f"Diving into the unknown, the explorer conjured its square: ##square({random_float}).",
            f"As curiosity grew, they harnessed the power of ten: ##power_of_ten({random_float}).",
            f"From the shadows, emerged another integer: {random_int_two}.",
            f"Questioning its nature, the explorer asked: Was it odd? The truth emerged: ##is_odd({random_int_two}).",
            f"And its absolute form was unveiled: ##absolute({random_int_two}).",
            f"Yet, destiny weaved a different tale with a new integer, {random_int_three}.",
            f"The explorer delved into its secrets, discovering its cube: ##cube({random_int_three}).",
            f"Seeking its essence, they unveiled the cube root: ##cube_root(##cube({random_int_three})).",
            f"But the adventure held even more surprises! A binary enigma emerged: {random_bool}.",
            f"The explorer pondered the ReLU transformation of {random_float}: ##relu({random_float}).",
            f"Venturing further, an unforeseen integer crossed their path: {random_int_four}.",
            f"Feeling the call of the unknown, they arranged its descent: ##descending_sort([{random_int_four}, {random_int_two}, {random_int_one}]).",
            f"Thus, the saga continued, a tapestry woven with calculations and revelations...",
            f"Through twists and turns, the explorer's journey unfurled, guided by the enchantment of mathematics.",
        ]

    ]

    return random.choice(examples)


if __name__ == "__main__":
    masked_example = create_masked_token_batch_three_example(1, Utility.get_spacy_nlp())
    print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example, PretrainTasks.MASKED_TOKEN_PREDICTION
    )
    print(sample)
#
#     next_token_example = create_next_token_batch_three_example(1, Utility.get_spacy_nlp())
#     print(len(next_token_example), next_token_example)
