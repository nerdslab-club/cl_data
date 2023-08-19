import random

import spacy

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_masked_token_batch_eight_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_eight_example_paragraph()
        for paragraph in paragraphs:
            masked_data = Utility.create_masked_input_output_example(paragraph, nlp)
            examples.extend(masked_data)
    return examples


def create_next_token_batch_eight_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_eight_example_paragraph()
        for paragraph in paragraphs:
            next_token_data = Utility.create_next_word_input_output_example(
                paragraph, nlp
            )
            examples.extend(next_token_data)
    return examples


def __get_batch_eight_example_paragraph():
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
        #     f"In the vibrant realm of Numerosia, where mathematical wonders held the key to unlocking extraordinary powers, two daring adventurers, Lily and Max, embarked on an epic quest to harness the mystique of numbers.",
        #     f"Lily, a scholar with an insatiable curiosity, chose to begin her journey by unraveling the enigma of negative numbers. Her calculation prowess uncovered the hidden truth behind -2 times {random_int_one} times {random_int_two}, yielding the result: ##negative_2ab({random_int_one}, {random_int_two}).",
        #     f"Meanwhile, Max, a fearless explorer of positivity, embarked on a parallel odyssey. He dived into the realm of positivity, wielding the mathematical forces to conquer 2 times {random_int_three} times {random_int_four}, unveiling: ##positive_2ab({random_int_three}, {random_int_four}).",
        #     f"Lily's path meandered through the intriguing landscape of quadratic equations. She ventured to simplify the enigmatic expression {random_int_one}x + ({random_int_two}x + {random_int_three}) into: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"Meanwhile, Max was drawn to the symphony of polynomials. He orchestrated the expression {random_int_four}x^2 + {random_int_two}x + {random_int_three}x, with x = {random_int_one}, to reveal its harmonious essence: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"As their journey unfolded, Lily and Max united their strengths to unravel the enchanting lore of cubes. The fusion of cubes, embodying the essence of {random_int_two} and {random_int_three}, unfolded its ancient secrets: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
        #     f"Undeterred by challenges, they pressed forward, encountering a profound cube conundrum. They harnessed the cube of the sum of {random_int_one} and {random_int_four}, meticulously subtracting thrice their cosmic union, revealing: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
        #     f"A harmonious synergy of intellect brought them to the realm of expressive expansions. The ethereal incantation of ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2, bore a mystic inscription: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
        #     f"Their journey then unfolded into the intricate tapestry of cube disparities. The enigma unfurled, laying bare the difference between the sacred cube of {random_int_one} and the elusive cube of {random_int_four}: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
        #     f"As twilight embraced Numerosia, Lily and Max stood before the pinnacle of their quest – a transcendental cube challenge. Their insight harmonized with cosmic melodies, revealing the cube of the difference between {random_int_two} and {random_int_three}, blessed by the trinity of unity, emerging as: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
        #     f"In the end, Lily and Max beheld the enchantment of mathematical exploration, realizing that in the realm of Numerosia, the magic of numbers held the promise of boundless discovery and awe-inspiring wisdom.",
        #     f"Their legacy echoed through time, inspiring generations to venture into the realm of numbers, where every equation was a portal to uncover the secrets of the universe itself."
        # ],
        # [
        #     f"Once in the land of Numerica, a young scholar named Sophia embarked on a journey through the mathematical tapestry.",
        #     f"Sophia's odyssey commenced with the art of addition, blending {random_int_one} and {random_int_two} into an exquisite union through ##addition({random_int_one},{random_int_two}).",
        #     f"As the sun dipped behind the horizon, Sophia found herself entwined in the dance of subtraction. The intricate choreography between {random_int_two} and {random_int_three} unfolded through ##subtraction({random_int_two},{random_int_three}).",
        #     f"Guided by the stars, Sophia's spirit resonated with the symphony of multiplication. She orchestrated the cosmos to unveil the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
        #     f"Like a dawn of revelation, Sophia embarked on the path of division. With grace, she uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
        #     f"Sophia's inquisitive mind led her to the cosmic dance of exponents. She raised {random_int_three} to the power of {random_int_four}, unraveling the universe's mysteries through ##exponentiation({random_int_three},{random_int_four}).",
        #     f"Beneath the shimmering moonlight, Sophia's heart stirred with curiosity for the mystic realm of square roots. She whispered the incantation, unveiling the secrets of {random_int_four}'s square root through ##square_root({random_int_four}).",
        #     f"As the first rays of sunlight painted the sky, Sophia faced the puzzle of floor division. With determination, she deciphered the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
        #     f"In the cosmic symphony of remainders, Sophia uncovered the hidden rhythm. The dance between {random_int_three} and {random_int_one} was unveiled through ##modulus({random_int_three},{random_int_one}).",
        #     f"Inscribed in the stars were the secrets of logarithms. Sophia contemplated the harmony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
        #     f"Embracing the cosmos, Sophia resonated with the celestial sine wave. With a profound connection to the universe, she unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        # ],
        # [
        #     f"Step into Arctopia, a realm where numbers orchestrate symphonies of discovery. Amidst this vibrant land, inhabited by diverse individuals like the digits themselves ({random_list}), the magic of mathematics flourishes.",
        #     f"An auspicious day beckoned a mathematician to embark on a quest, armed with an enigma: an angle, {random_float}. This angle became the key unlocking the gateway to the realm of trigonometry, where the beguiling dance of cosine awaited.",
        #     f"From the celestial canvas emerged the very essence of the unknown: the cosine of {random_float} radians, whispered by the cosmos itself: ##cosine({random_float}). The path of the mathematician now led to the revelation of its tangent.",
        #     f"The whisper of angles guided the mathematician to unravel the enigmatic tangent of ##arccosine({random_float}). This revelation held not merely a numerical value, but a profound insight etched within its mathematical essence.",
        #     f"Elsewhere in Arctopia, another soul was entranced by hyperbolic mysteries. Their fascination centered around the hyperbolic sine of {random_int_one}, a formula echoing through the corridors of time.",
        #     f"As twilight brushed the sky with hues of wonder, young minds converged to decode the riddles of logarithms. Among them, the base-10 logarithm of {random_int_two} revealed patterns transcending the mundane.",
        #     f"In the midst of this assembly, a prodigious child contemplated the enigma of the cube root of ##hyperbolic_tangent({random_int_three}). A question resonating with the essence of numbers and the boundless realm of possibilities.",
        #     f"Amid contemplation, a sage, guardian of ancient wisdom, pondered the profound union of numbers and angles: ##logarithm_base_2({random_int_four}) raised to the celestial power of ##arcsine({random_float}).",
        #     f"As destiny wove its intricate threads, the two mathematicians converged, blending their insights to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
        #     f"After an intricate choreography of calculations, the answer materialized: {random_int_two + random_int_four}. Arctopia rejoiced, a grand celebration of intellect and discovery. And thus, the legacy of Arctopia's mathematical marvels continued to inspire."
        # ],
        # [
        #     f"In the mesmerizing realm of Numerion, where numbers held the power to weave destinies, a spirited young mathematician named Mia embarked on a transformative journey.",
        #     f"Bearing an angle of {random_int_one} degrees, Mia embarked on an odyssey to translate it into the mystical tongue of radians. With the sacred incantation degrees_to_radians, the transformation was revealed: ##degrees_to_radians({random_int_one}).",
        #     f"Her path led her to an ancient door protected by the guardians of greatest common divisor. By invoking the spirits of {random_int_two} and {random_int_three}, Mia unlocked the door, unveiling its secrets: ##gcd({random_int_two}, {random_int_three}).",
        #     f"Continuing her voyage, Mia uncovered the ancient scrolls of least common multiples, discovering the hidden connections between {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
        #     f"In the heart of the enchanted Forest of Numbers, Mia encountered an ancient tree that stood as a testament to time. Through the magic of isqrt, she discerned the tree's age, finding it to be ##isqrt({random_int_three}).",
        #     f"As twilight painted Numerion with hues of amber and indigo, Mia harnessed the arcane powers of congruence. By invoking the pow_mod enchantment, she raised {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, revealing the hidden truth: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
        #     f"In a realm where time flowed like a river, Mia navigated its currents using the spells of ceil, floor, and round. The river's surface reflected the profound difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
        #     f"As Mia's journey unfolded, she realized that each mathematical function was a key to unlocking a new chamber of insight. Armed with this wisdom, Mia returned to Numerion, sharing her tale to inspire others to embark on their own quests of numerical discovery.",
        # ],
        # [
        #     f"Amidst a world where numbers held secrets like stars in the night sky, a quest was undertaken by a curious mathematician.",
        #     f"In their pursuit of understanding, they embarked on a journey to unravel the mysteries surrounding {random_int_one}, {random_int_two}, and {random_int_three}.",
        #     f"Their voyage commenced with the enigma of the greatest value between {random_float} and {random_int_one}.",
        #     f"After profound contemplation, they unveiled the answer: ##greatest_value({random_float}, {random_int_one}).",
        #     f"Yet, the allure of numbers beckoned further. Their focus turned to {random_list}, an ensemble of cryptic numbers.",
        #     f"The mathematician uncovered the hidden narrative within, illuminating the elusive product: ##product({random_list}).",
        #     f"Fueled by curiosity, they delved into the realm of factorials, revealing the enchantment of {random_int_one}!: ##factorial({random_int_one}).",
        #     f"However, another enigma awaited—the essence of {random_int_two}. Was it a prime number? The revelation materialized as ##is_prime({random_int_two}).",
        #     f"Undaunted, they embarked on the age-old quest for prime factors, unearthing the story of {random_int_three}: ##prime_factors({random_int_three}).",
        #     f"In their journey, they stumbled upon {random_int_four}, a number holding a secret—it was a perfect square: ##is_perfect_square({random_int_four}).",
        #     f"Continuing their odyssey, they unveiled the hidden truth of {random_int_three}, a concealed perfect cube: ##is_perfect_cube({random_int_three}).",
        #     f"With a heart ignited by numbers, the mathematician returned to {random_list}, deciphering their collective story through the prism of the mean: ##mean({random_list}).",
        #     f"Yet, one final enigma lingered—the elusive median, the rhythmic heartbeat of the numbers: ##median({random_list}).",
        #     f"And thus, the mathematician's epic journey through the realm of numbers continued, unveiling the intricate tapestry woven by the language of mathematics."
        # ],
        [
            f"Amidst a realm where numbers held the keys to ancient truths...",
            f"A daring seeker stumbled upon an array of enigmatic numbers: {random_list}.",
            f"Invoking the dance of order, the seeker called forth: ##ascending_sort({random_list}).",
            f"Among them, a captivating integer took its place: {random_int_one}.",
            f"Contemplating its essence, a question emerged: Even or odd? The answer whispered: ##is_even({random_int_one}).",
            f"Revealing its hidden power, they unveiled its square: ##square_int({random_int_one}).",
            f"But amidst this enchantment, a spectral floating point number, {random_float}, appeared.",
            f"Venturing into the unknown, they conjured its squared form: ##square({random_float}).",
            f"With a leap of understanding, they tapped into the power of ten: ##power_of_ten({random_float}).",
            f"Emerging from shadows, another integer stepped into the light: {random_int_two}.",
            f"Exploring its nature, the seeker inquired: Odd or even? The answer echoed: ##is_odd({random_int_two}).",
            f"And its absolute truth emerged: ##absolute({random_int_two}).",
            f"But destiny had more in store, an enigmatic integer took the center stage: {random_int_three}.",
            f"Unraveling its mystery, the seeker discovered its cube: ##cube({random_int_three}).",
            f"Venturing deeper, they unlocked the essence of its cube root: ##cube_root(##cube({random_int_three})).",
            f"But the tale was far from over! A binary enigma emerged: {random_bool}.",
            f"Reflecting on the cosmic dance, they invoked the ReLU magic for {random_float}: ##relu({random_float}).",
            f"Continuing the journey, an unexpected integer came into focus: {random_int_four}.",
            f"Drawn by the unknown, they orchestrated a descent: ##descending_sort([{random_int_four}, {random_int_two}, {random_int_one}]).",
            f"And so, the saga unfolded, a tapestry woven with calculations and revelations...",
            f"Through twists and turns, the seeker's journey continued, guided by the timeless enchantment of mathematics.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    masked_example = create_masked_token_batch_eight_example(1, Utility.get_spacy_nlp())
    print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example, PretrainTasks.MASKED_TOKEN_PREDICTION
    )
    print(sample)
#
#     next_token_example = create_next_token_batch_eight_example(1, Utility.get_spacy_nlp())
#     print(len(next_token_example), next_token_example)
