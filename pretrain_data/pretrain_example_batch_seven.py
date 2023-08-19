import random

import spacy

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_masked_token_batch_seven_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_seven_example_paragraph()
        for paragraph in paragraphs:
            masked_data = Utility.create_masked_input_output_example(paragraph, nlp)
            examples.extend(masked_data)
    return examples


def create_next_token_batch_seven_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_seven_example_paragraph()
        for paragraph in paragraphs:
            next_token_data = Utility.create_next_word_input_output_example(
                paragraph, nlp
            )
            examples.extend(next_token_data)
    return examples


def __get_batch_seven_example_paragraph():
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
        #     f"In the realm of Numarctica, where numbers held mystical powers, two valiant scholars, Ava and Leo, embarked on a quest to decipher the ancient scrolls of mathematical magic.",
        #     f"Ava, a curious enchantress, decided to first explore the enigmatic realm of negative numbers. Her incantation revealed the hidden truth behind -2 times {random_int_one} times {random_int_two}, conjuring the result: ##negative_2ab({random_int_one}, {random_int_two}).",
        #     f"Meanwhile, Leo, a sage of positivity, sought illumination from positive forces. Delving into the cosmic arithmetic, he harnessed 2 times {random_int_three} times {random_int_four}, revealing: ##positive_2ab({random_int_three}, {random_int_four}).",
        #     f"Ava's path then led her to unravel the arcane secrets of quadratic formations. She gazed upon the equation {random_int_one}x + ({random_int_two}x + {random_int_three}), weaving her powers to simplify it to: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"Yet, it was in the constellation of polynomials that Leo sought inspiration. Guided by the celestial muse, he manifested the essence of {random_int_one}x^2 + {random_int_two}x + {random_int_three}x, with x = {random_int_one}, uncovering: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"As their journey continued, Ava and Leo united their energies to fathom the mystical realm of cubes. The combined essence of cubes, embracing {random_int_two} and {random_int_three}, revealed its true nature: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
        #     f"Undeterred by challenges, they ventured deeper into mathematical mysteries. Their pursuit led them to a profound cube enigma, where the cube of the sum of {random_int_one} and {random_int_four}, minus thrice their ethereal union, transformed into: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
        #     f"As Ava and Leo traversed through the labyrinthine expressions, they stumbled upon the eldritch expansion of ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2, revealing an intricate sigil: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
        #     f"Yet, their saga held a transcendental twist - a tale of cube disparities. The riddle unraveled, exposing the gap between the sacred cube of {random_int_one} and the mystic cube of {random_int_four}: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
        #     f"At the pinnacle of their journey, Ava and Leo encountered the zenith of cube conundrums. Their insight resonated with the cosmos, deciphering the cube of the difference between {random_int_two} and {random_int_three}, enriched by threefold cosmic fusion, ultimately emerging as: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
        #     f"With newfound wisdom and a sense of unity, Ava and Leo realized that the sacred art of mathematics was a universal language that transcended time and space, connecting all realms in Numarctica.",
        #     f"Their legacy lived on, reminding future generations that the quest for knowledge was a voyage of endless discovery, forever intertwined with the captivating mysteries of numbers."
        # ],
        # [
        #     f"Amidst the pages of an ancient tome, the story of a young mathemagician named Maya unfolded.",
        #     f"Maya's journey through the realm of numbers began with the art of addition. She delicately added {random_int_one} and {random_int_two}, conjuring the answer through ##addition({random_int_one},{random_int_two}).",
        #     f"In her quest for mathematical enlightenment, Maya encountered the enigma of subtraction. The dance between {random_int_two} and {random_int_three} was revealed through ##subtraction({random_int_two},{random_int_three}).",
        #     f"Guided by the celestial patterns, Maya's mind ignited with the allure of multiplication. She orchestrated the universe's symphony to reveal the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
        #     f"As dawn kissed the horizon, Maya ventured into the realm of division. With grace, she uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
        #     f"Maya's insatiable curiosity led her to the cosmic dance of exponents. She raised {random_int_three} to the power of {random_int_four}, unraveling the universe's mysteries through ##exponentiation({random_int_three},{random_int_four}).",
        #     f"Beneath the shimmering moonlight, Maya's gaze was drawn to the mystic realm of square roots. She whispered the enchanting incantation, unveiling the secrets of {random_int_four}'s square root through ##square_root({random_int_four}).",
        #     f"As the first rays of sunlight emerged, Maya faced the puzzle of floor division. With determination, she decoded the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
        #     f"In the cosmic tapestry of remainders, Maya uncovered the hidden rhythm. The dance between {random_int_three} and {random_int_one} was unveiled through ##modulus({random_int_three},{random_int_one}).",
        #     f"Inscribed in the fabric of the universe were the secrets of logarithms. Maya contemplated the symphony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
        #     f"Nestled in the embrace of cosmic harmony, Maya embraced the celestial sine wave. With a profound connection to the cosmos, she unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        # ],
        # [
        #     f"Step into Arctopia, a realm where numbers whisper secrets and equations weave tales. Amidst this vibrant land, inhabited by individuals as diverse as the digits themselves ({random_list}), the magic of mathematics thrives.",
        #     f"On a day painted with curiosity, a mathematician set forth on a quest with an angle, a mystical key: {random_float}. This key unlocked the gateway to trigonometry, where the enchanting choreography of cosine awaited.",
        #     f"From the celestial stage emerged the essence of the unknown: the cosine of {random_float} radians, whispered by the universe itself: ##cosine({random_float}). The mathematician's journey now led to the discovery of its tangent.",
        #     f"The symphony of angles guided the mathematician to reveal the enigmatic tangent of ##arccosine({random_float}). This revelation held not only a numerical value but a profound insight within its mathematical embrace.",
        #     f"Elsewhere, another soul in Arctopia was captivated by hyperbolic enigmas. Their fascination revolved around the hyperbolic sine of {random_int_one}, a formula that seemed to echo across time.",
        #     f"As twilight painted the sky with shades of wonder, young minds converged to decipher the riddles of logarithms. Among them, the base-10 logarithm of {random_int_two} unveiled patterns transcending the ordinary.",
        #     f"Within this assembly, a prodigious child contemplated the enigma of the cube root of ##hyperbolic_tangent({random_int_three}). A question resonating with the essence of numbers and the vast realm of possibilities.",
        #     f"Amid contemplation, a sage, a custodian of ancient wisdom, pondered the profound synergy of numbers and angles: ##logarithm_base_2({random_int_four}) elevated to the ethereal power of ##arcsine({random_float}).",
        #     f"As destiny wove its threads, the two mathematicians united, their insights converging to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
        #     f"After a symphony of calculations, the answer materialized: {random_int_two + random_int_four}. Arctopia rejoiced, a grand celebration of intellect and discovery. And thus, the legacy of Arctopia's mathematical marvels illuminated the path forward."
        # ],
        # [
        #     f"Within the realm of Numaria, where numbers held the key to all mysteries, a young mathematician named Eli set forth on a journey of discovery.",
        #     f"With {random_int_one} degrees in hand, Eli embarked on a quest to transform them into the esoteric language of radians. Through the power of degrees_to_radians, the transformation was ##degrees_to_radians({random_int_one}).",
        #     f"Venturing deeper into the land, Eli stumbled upon an ancient doorway guarded by the sentinels of greatest common divisor. The sacred numbers {random_int_two} and {random_int_three} revealed the path: ##gcd({random_int_two}, {random_int_three}).",
        #     f"Continuing the expedition, Eli deciphered the scrolls of least common multiples, uncovering the connection between {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
        #     f"Guided by the stars, Eli encountered a mystical tree deep within the Enchanted Forest of Numbers. The tree's age was unveiled through the power of isqrt, and the age was ##isqrt({random_int_three}).",
        #     f"As the sun dipped below the horizon, bathing Numaria in a warm glow, Eli harnessed the magic of congruence. By invoking the pow_mod enchantment, {random_int_two} was raised to the power of {random_int_one}, modulo {random_int_four}, revealing the secret: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
        #     f"In a realm where time flowed like a river, Eli rode its currents with the spells of ceil, floor, and round. The river's surface reflected the profound difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
        #     f"As Eli's odyssey neared its end, the realization dawned that each mathematical function was a key to unlock a new chamber of understanding. Armed with this wisdom, Eli returned to Numaria to share their journey, inspiring others to embark on their own mathematical quests.",
        # ],
        # [
        #     f"Legend whispers of a land where numbers held ancient truths, and in that land, a curious mathematician roamed.",
        #     f"In their pursuit of wisdom, they unveiled the enigmas surrounding {random_int_one}, {random_int_two}, and {random_int_three}.",
        #     f"Their journey unfolded with the mystery of the greatest value between {random_float} and {random_int_one}.",
        #     f"After deep contemplation, they revealed the answer: ##greatest_value({random_float}, {random_int_one}).",
        #     f"But the allure of numbers persisted. Their gaze turned to {random_list}, a collection of mystical numbers.",
        #     f"The mathematician unearthed the cryptic tale within, exposing the elusive product: ##product({random_list}).",
        #     f"Driven by curiosity, they ventured into the realm of factorials, unravelling the enchantment of {random_int_one}!: ##factorial({random_int_one}).",
        #     f"Yet, another enigma beckoned—the nature of {random_int_two}. Was it a prime number? The revelation emerged as ##is_prime({random_int_two}).",
        #     f"Undeterred, they embarked on the age-old quest of prime factors, unearthing the saga of {random_int_three}: ##prime_factors({random_int_three}).",
        #     f"In their journey, they stumbled upon {random_int_four}, a number with a secret—it was a perfect square: ##is_perfect_square({random_int_four}).",
        #     f"Their odyssey continued, revealing the hidden truth of {random_int_three}, a concealed perfect cube: ##is_perfect_cube({random_int_three}).",
        #     f"With a heart aflame with numbers, the mathematician returned to {random_list}, decoding their collective story through the prism of the mean: ##mean({random_list}).",
        #     f"Yet, a final enigma lingered—the elusive median, the heartbeat of the numbers: ##median({random_list}).",
        #     f"And so, the mathematician's epic journey through the realm of numbers endured, unravelling the intricate tapestry woven by the language of mathematics."
        # ],
        [
            f"In an ancient realm where numbers held the threads of destiny...",
            f"A curious voyager stumbled upon an array of enigmatic numbers: {random_list}.",
            f"Unleashing the magic of order, the voyager summoned: ##ascending_sort({random_list}).",
            f"Amidst them, a captivating integer took the stage: {random_int_one}.",
            f"Contemplating its essence, a question emerged: Even or odd? The answer echoed: ##is_even({random_int_one}).",
            f"Unveiling its latent potency, they unraveled its square: ##square_int({random_int_one}).",
            f"But amidst this enchantment, a spectral floating point number, {random_float}, appeared.",
            f"Diving into the unknown, they conjured its squared form: ##square({random_float}).",
            f"With a leap of understanding, they harnessed the essence of ten: ##power_of_ten({random_float}).",
            f"Emerging from shadows, another integer stepped into the light: {random_int_two}.",
            f"Exploring its nature, the voyager questioned: Odd or even? The answer revealed: ##is_odd({random_int_two}).",
            f"And its absolute truth surfaced: ##absolute({random_int_two}).",
            f"But destiny had more in store, an enigmatic integer took center stage: {random_int_three}.",
            f"Unraveling its mystery, the voyager discovered its cube: ##cube({random_int_three}).",
            f"Venturing deeper, they unlocked the essence of its cube root: ##cube_root(##cube({random_int_three})).",
            f"But the tale was not yet done! A binary enigma emerged: {random_bool}.",
            f"Contemplating the cosmic balance, they invoked the ReLU enchantment for {random_float}: ##relu({random_float}).",
            f"Continuing the journey, an unexpected integer made its entrance: {random_int_four}.",
            f"Drawn by the unknown, they orchestrated a descent: ##descending_sort([{random_int_four}, {random_int_two}, {random_int_one}]).",
            f"And so, the saga unfolded, a tapestry woven with calculations and revelations...",
            f"Through twists and turns, the voyager's journey continued, guided by the timeless magic of mathematics.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    masked_example = create_masked_token_batch_seven_example(1, Utility.get_spacy_nlp())
    print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example, PretrainTasks.MASKED_TOKEN_PREDICTION
    )
    print(sample)
#
#     next_token_example = create_next_token_batch_seven_example(1, Utility.get_spacy_nlp())
#     print(len(next_token_example), next_token_example)
