import random

import spacy

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_masked_token_batch_six_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_six_example_paragraph()
        for paragraph in paragraphs:
            masked_data = Utility.create_masked_input_output_example(paragraph, nlp)
            examples.extend(masked_data)
    return examples


def create_next_token_batch_six_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_six_example_paragraph()
        for paragraph in paragraphs:
            next_token_data = Utility.create_next_word_input_output_example(
                paragraph, nlp
            )
            examples.extend(next_token_data)
    return examples


def __get_batch_six_example_paragraph():
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
        #     f"Deep in the heart of the Enchanted Mathematica Forest, two intrepid explorers, Alex and Morgan, embarked on a quest to unlock the secrets of mathematical wonders.",
        #     f"Alex, the fearless adventurer, took on the challenge of unraveling the mysteries of negative numbers. Their first task involved calculating -2 times {random_int_one} times {random_int_two}, which yielded the result: ##negative_2ab({random_int_one}, {random_int_two}).",
        #     f"Morgan, a keen observer of positive phenomena, decided to explore the other side of the coin. They delved into the world of positive numbers, finding that 2 times {random_int_three} times {random_int_four} equaled: ##positive_2ab({random_int_three}, {random_int_four}).",
        #     f"The journey led Alex to quadratic landscapes, where they encountered the expression {random_int_one}x + ({random_int_two}x + {random_int_three}). With deft calculations, Alex simplified it to: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"Morgan, however, set their sights on a realm of polynomial wonders. Substituting x = {random_int_one} into {random_int_four}x^2 + {random_int_two}x + {random_int_three}x, they uncovered: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"Yet, the true magic occurred when Alex and Morgan united their powers to solve puzzles involving cubes. The sum of cubes of {random_int_two} and {random_int_three} revealed itself as: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
        #     f"Collaborating further, they faced a cube difference riddle. Combining the cube of the sum of {random_int_one} and {random_int_four}, minus three times their product, led to: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
        #     f"The intrepid duo's journey through mathematical landscapes extended to expressions involving squares. Expanding ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2 revealed: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
        #     f"Yet another enchanting twist awaited them – cube differences. The difference between the cube of {random_int_one} and the cube of {random_int_four} unfolded as: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
        #     f"At last, their expedition reached a crescendo with the ultimate cube challenge. The cube of the difference between {random_int_two} and {random_int_three}, plus three times their product, emerged as: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
        #     f"As the sun set on their adventure, Alex and Morgan marveled at the mathematical landscapes they had traversed. Their shared journey had unlocked new realms of knowledge, reinforcing their belief that the Enchanted Mathematica Forest held endless wonders waiting to be discovered."
        # ],
        # [
        #     f"Once upon a mathematical odyssey, there was a young explorer named Max.",
        #     f"Max embarked on a quest to decipher the language of numbers. His journey began by adding {random_int_one} and {random_int_two}, unveiling the hidden sum through ##addition({random_int_one},{random_int_two}).",
        #     f"Guided by the stars, Max encountered the enigma of subtraction. The dance between {random_int_two} and {random_int_three} was unveiled through ##subtraction({random_int_two},{random_int_three}).",
        #     f"In the grand symphony of multiplication, Max composed a masterpiece. The universe revealed the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
        #     f"As dawn illuminated the path, Max ventured into the realm of division. With a spark of insight, he uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
        #     f"Max's thirst for knowledge led him to the cosmic realm of exponents. He raised {random_int_three} to the power of {random_int_four}, unleashing the universe's secrets through ##exponentiation({random_int_three},{random_int_four}).",
        #     f"Beneath the moon's gentle glow, Max found himself drawn to the mystical domain of square roots. The universe whispered its secrets as he revealed the square root of {random_int_four} through ##square_root({random_int_four}).",
        #     f"As the day's first light appeared, Max faced the puzzle of floor division. With determination, he solved the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
        #     f"In the intricate dance of numbers, Max discovered the rhythm of remainders. The universe unveiled the dance between {random_int_three} and {random_int_one} through ##modulus({random_int_three},{random_int_one}).",
        #     f"Inscribed in the cosmic tapestry were the secrets of logarithms. Max pondered the harmonious symphony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
        #     f"Nestled in the embrace of the cosmos, Max embraced the celestial sine wave. With a profound connection to the universe, he unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        # ],
        # [
        #     f"Welcome to Arctopia, a realm where numbers compose the symphony of existence. Among the vibrant community, each with their unique attributes ({random_list}), the allure of mathematics resonates.",
        #     f"A day of destiny arrived as a curious mathematician embarked on a quest, armed with the enigma of an angle: {random_float}. This angle led them through the corridors of trigonometry, where the cosmic choreography of cosine awaited.",
        #     f"From the cosmic canvas, the mathematician extracted the essence of the unknown: the cosine of {random_float} radians, whispered by the universe itself: ##cosine({random_float}). The next step beckoned — the discovery of its tangent.",
        #     f"The whisper of angles guided the mathematician to unveil the enigmatic tangent of ##arccosine({random_float}). The revelation held not only a numerical value but a profound revelation within its folds.",
        #     f"Elsewhere in the realm, another mathematical spirit was captivated by hyperbolic mysteries. Their fascination centered on the hyperbolic sine of {random_int_one}, a formula that seemed to echo through time.",
        #     f"As twilight painted the sky with hues of contemplation, young minds gathered to decode the enigma of logarithms. Among them, the base-10 logarithm of {random_int_two} unfolded, revealing patterns that transcended the mundane.",
        #     f"Amid this assembly, a prodigious child pondered the riddle of the cube root of ##hyperbolic_tangent({random_int_three}). A question that resonated with the essence of numbers and the boundless realm of possibilities.",
        #     f"Lost in thought, a sage, a guardian of ancient wisdom, contemplated the profound convergence of numbers and angles: ##logarithm_base_2({random_int_four}) raised to the ethereal power of ##arcsine({random_float}).",
        #     f"As destiny entwined its threads, the two mathematicians united, weaving their insights to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
        #     f"After a symphony of calculations, the answer materialized: {random_int_two + random_int_four}. Arctopia rejoiced, a grand celebration of intellect and discovery. And so, the legacy of Arctopia's mathematical marvels illuminated the path forward."
        # ],
        # [
        #     f"Amidst the sprawling landscapes of Mathovia, a realm woven with numbers and enigmas, a young adventurer named Ava embarked on an exhilarating quest.",
        #     f"Equipped with an angle of {random_int_one} degrees, Ava embarked on a journey to translate it into the mystical language of radians, invoking the formula degrees_to_radians: ##degrees_to_radians({random_int_one}).",
        #     f"As she delved deeper into the heart of Mathovia, Ava stumbled upon a doorway guarded by the guardians of greatest common divisor. Unlocking the door with the sacred numbers {random_int_two} and {random_int_three}, she uncovered its secrets: ##gcd({random_int_two}, {random_int_three}).",
        #     f"Venturing further, Ava discovered the ancient manuscripts of least common multiples, unveiling the arcane wisdom that linked {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
        #     f"Guided by her passion, Ava encountered an ancient tree deep within the Forest of Numbers. The tree's age was revealed to her through the magic of isqrt, standing at ##isqrt({random_int_three}).",
        #     f"As twilight bathed Mathovia in hues of purple and gold, Ava embraced the power of congruence. By wielding the pow_mod enchantment, she raised {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, uncovering a hidden treasure: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
        #     f"In the realm where time flowed like a river, Ava navigated its currents using the incantations of ceil, floor, and round. The river's surface reflected the profound difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
        #     f"As Ava's journey drew to a close, she realized that each mathematical function was a key to unlocking the infinite mysteries of Mathovia. Armed with this wisdom, she returned to her homeland, sharing the tales of her adventures and inspiring others to embark on their own mathematical odysseys.",
        # ],
        # [
        #     f"Long ago, in a world where numbers held secrets, a curious mathematician's journey began.",
        #     f"This inquisitive mind delved into the mysteries of {random_int_one}, {random_int_two}, and {random_int_three}.",
        #     f"Their adventure commenced with the puzzle of the greatest value between {random_float} and {random_int_one}.",
        #     f"After moments of reflection, they revealed the answer: ##greatest_value({random_float}, {random_int_one}).",
        #     f"But the horizon of knowledge beckoned. Their attention turned to {random_list}, an array of arcane numbers.",
        #     f"The mathematician unraveled the hidden narrative, exposing the enigmatic product: ##product({random_list}).",
        #     f"Entranced by the magic of factorials, they journeyed into {random_int_one}!, discovering its mystical essence: ##factorial({random_int_one}).",
        #     f"Yet, another enigma awaited—the nature of {random_int_two}. Was it a prime number? The truth emerged as ##is_prime({random_int_two}).",
        #     f"Their quest persisted. They embarked on the ancient path of prime factors, unveiling the tale of {random_int_three}: ##prime_factors({random_int_three}).",
        #     f"Amidst their exploration, they stumbled upon {random_int_four}, a number with a secret—it was a perfect square: ##is_perfect_square({random_int_four}).",
        #     f"Their journey unveiled the truth of {random_int_three}, a hidden perfect cube: ##is_perfect_cube({random_int_three}).",
        #     f"A heart filled with numbers, the mathematician returned to {random_list}, deciphering the collective story through the lens of the mean: ##mean({random_list}).",
        #     f"Yet, a final mystery remained—the elusive median, the heartbeat of the numbers: ##median({random_list}).",
        #     f"And thus, the mathematician's odyssey through the realm of numbers endured, revealing the intricate tapestry woven by mathematics."
        # ],
        [
            f"Long ago, in a realm where numbers held the keys to mysteries...",
            f"An intrepid seeker stumbled upon an array of enigmatic numbers: {random_list}.",
            f"Unveiling the secrets of order, the seeker summoned: ##ascending_sort({random_list}).",
            f"Amidst them, a captivating integer stepped into the spotlight: {random_int_one}.",
            f"Questioning its nature, they wondered: Was it even or odd? The answer resonated: ##is_even({random_int_one}).",
            f"Drawing forth its hidden power, they uncovered its square: ##square_int({random_int_one}).",
            f"But amidst the enchantment, a spectral floating point number, {random_float}, emerged.",
            f"Venturing into the unknown, they conjured its squared form: ##square({random_float}).",
            f"Embarking on a mathematical odyssey, they harnessed the essence of ten: ##power_of_ten({random_float}).",
            f"Emerging from the shadows, another integer claimed their attention: {random_int_two}.",
            f"Delving into its enigma, they inquired: Was it odd or even? The truth emerged: ##is_odd({random_int_two}).",
            f"Revealing its absolute nature, they uncovered: ##absolute({random_int_two}).",
            f"Yet fate had more to unveil, an enigmatic integer took the stage: {random_int_three}.",
            f"Deciphering its mystery, the seeker discovered its cube: ##cube({random_int_three}).",
            f"Digging deeper, they unlocked the essence of its cube root: ##cube_root(##cube({random_int_three})).",
            f"But the tale had further twists! A binary enigma emerged: {random_bool}.",
            f"Reflecting on the cosmic order, they invoked the ReLU incantation for {random_float}: ##relu({random_float}).",
            f"Guided by curiosity, an unexpected integer made its entrance: {random_int_four}.",
            f"Drawn by the unknown, they orchestrated a descent: ##descending_sort([{random_int_four}, {random_int_two}, {random_int_one}]).",
            f"And so, the saga continued, a symphony of calculations and revelations...",
            f"Through twists and turns, the seeker's journey unfolded, guided by the timeless enchantment of mathematics.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    masked_example = create_masked_token_batch_six_example(1, Utility.get_spacy_nlp())
    print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example, PretrainTasks.MASKED_TOKEN_PREDICTION
    )
    print(sample)
#
#     next_token_example = create_next_token_batch_six_example(1, Utility.get_spacy_nlp())
#     print(len(next_token_example), next_token_example)
