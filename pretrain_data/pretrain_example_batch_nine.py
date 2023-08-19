import random

import spacy

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_masked_token_batch_nine_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_nine_example_paragraph()
        for paragraph in paragraphs:
            masked_data = Utility.create_masked_input_output_example(paragraph, nlp)
            examples.extend(masked_data)
    return examples


def create_next_token_batch_nine_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_nine_example_paragraph()
        for paragraph in paragraphs:
            next_token_data = Utility.create_next_word_input_output_example(
                paragraph, nlp
            )
            examples.extend(next_token_data)
    return examples


def __get_batch_nine_example_paragraph():
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
        #     f"In the realm of Arithmos, a land where numbers held the secrets of magic, two intrepid seekers, Maya and Eli, set forth on a quest to unveil the mysteries of mathematical marvels.",
        #     f"Maya, a fearless mathematician, embarked on her journey by delving into the enigmatic realm of negative numbers. Through intricate calculations, she unveiled the hidden truth behind -2 times {random_int_one} times {random_int_two}, yielding the result: ##negative_2ab({random_int_one}, {random_int_two}).",
        #     f"Meanwhile, Eli, an inquisitive explorer, turned his attention to the world of positivity. Guided by curiosity, he harnessed the mathematical forces to master 2 times {random_int_three} times {random_int_four}, revealing: ##positive_2ab({random_int_three}, {random_int_four}).",
        #     f"Maya's path then led her through the maze of quadratic equations. She skillfully simplified the intricate expression {random_int_one}x + ({random_int_two}x + {random_int_three}) into a more elegant form: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"Eli, on the other hand, was drawn to the captivating symphony of polynomials. He harmonized the elements of {random_int_four}x^2 + {random_int_two}x + {random_int_three}x, with x = {random_int_one}, revealing its melodious essence: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"As their journey unfolded, Maya and Eli united their strengths to unlock the ancient wisdom of cubes. The fusion of cubical energies, embracing {random_int_two} and {random_int_three}, revealed its arcane secrets: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
        #     f"Undaunted by challenges, they advanced further, encountering a profound puzzle involving cube differences. They harnessed the cube of the sum of {random_int_one} and {random_int_four}, meticulously subtracting thrice their cosmic connection, revealing: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
        #     f"Their journey then led them to unravel expressive expansions. The mystical incantation of ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2, bore an intricate inscription: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
        #     f"Their expedition then ventured into the enigma of cube disparities. The riddle unraveled, revealing the profound difference between the sacred cube of {random_int_one} and the elusive cube of {random_int_four}: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
        #     f"At the zenith of their journey, Maya and Eli faced the ultimate cube challenge. Their insight harmonized with cosmic vibrations, unveiling the cube of the difference between {random_int_two} and {random_int_three}, touched by the trinity of unity, emerging as: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
        #     f"In the end, Maya and Eli discovered that in Arithmos, the language of numbers held the power to reveal the secrets of the universe, and their quest became an eternal testament to the beauty of mathematical exploration.",
        #     f"Their legacy echoed through generations, inspiring the curious minds of Arithmos to embark on their own quests, guided by the enchanting allure of numbers and the infinite worlds they unveiled."
        # ],
        # [
        #     f"Venture into the realm of Equatia, where the young scholar, Oliver, sought to unlock the language of numbers.",
        #     f"Oliver's journey commenced with the elegant art of addition, merging {random_int_one} and {random_int_two} in perfect harmony through ##addition({random_int_one},{random_int_two}).",
        #     f"As the sun dipped below the horizon, Oliver found himself entwined in the intricate dance of subtraction. The enigmatic rhythm between {random_int_two} and {random_int_three} revealed itself through ##subtraction({random_int_two},{random_int_three}).",
        #     f"Guided by the constellations, Oliver's spirit resonated with the symphony of multiplication. He conducted the universe to unveil the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
        #     f"Like the first light of dawn, Oliver embarked on the path of division. With grace, he uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
        #     f"Oliver's insatiable curiosity led him to the cosmic dance of exponents. He elevated {random_int_three} to the power of {random_int_four}, revealing the universe's mysteries through ##exponentiation({random_int_three},{random_int_four}).",
        #     f"Beneath the enchanting moonlight, Oliver's heart was drawn to the mystic realm of square roots. He whispered the incantation, unveiling the secrets of {random_int_four}'s square root through ##square_root({random_int_four}).",
        #     f"As the first rays of sunlight graced the sky, Oliver faced the puzzle of floor division. With determination, he deciphered the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
        #     f"In the cosmic symphony of remainders, Oliver uncovered the hidden rhythm. The dance between {random_int_three} and {random_int_one} was unveiled through ##modulus({random_int_three},{random_int_one}).",
        #     f"Inscribed in the constellations were the secrets of logarithms. Oliver contemplated the harmony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
        #     f"Embracing the cosmos, Oliver resonated with the celestial sine wave. With a profound connection to the universe, he unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        # ],
        # [
        #     f"Journey into Arctopia, where numbers dance in harmony and equations tell tales of wonder. Amidst this vibrant realm, home to a diverse community reminiscent of the digits themselves ({random_list}), the enchantment of mathematics reigns.",
        #     f"Amidst the stars, a mathematician embarked on a quest with an enigma in hand: an angle, {random_float}. This angle, a key to unlocking the treasure troves of trigonometry, unveiled the cosmic rhythm of cosine.",
        #     f"From the celestial canvas emerged the very essence of the unknown: the cosine of {random_float} radians, whispered by the cosmos itself: ##cosine({random_float}). The mathematician's odyssey now led to the unraveling of its tangent.",
        #     f"The whisper of angles guided the mathematician to reveal the enigmatic tangent of ##arccosine({random_float}). This revelation held not just a value, but a profound insight etched within the tapestry of mathematics.",
        #     f"Across Arctopia, another soul was entranced by hyperbolic mysteries. Their fascination centered around the hyperbolic sine of {random_int_one}, a formula resonating with the echoes of time.",
        #     f"As twilight cast its hues of curiosity, young minds gathered to decode the riddles of logarithms. Among them, the base-10 logarithm of {random_int_two} unveiled patterns transcending the ordinary.",
        #     f"In this gathering, a prodigious child pondered the enigma of the cube root of ##hyperbolic_tangent({random_int_three}). A question that resonated with the essence of numbers and the limitless expanse of possibilities.",
        #     f"Amid contemplation, a sage, guardian of ancient wisdom, pondered the profound union of numbers and angles: ##logarithm_base_2({random_int_four}) raised to the celestial power of ##arcsine({random_float}).",
        #     f"As destiny's threads wove intricate patterns, the two mathematicians converged, merging their insights to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
        #     f"After a symphony of calculations, the answer was revealed: {random_int_two + random_int_four}. Arctopia celebrated, a grand gala honoring intellect and discovery. Thus, the legacy of Arctopia's mathematical marvels continued to illuminate paths ahead."
        # ],
        # [
        #     f"Welcome to the mystical land of Mathoria, a realm where numbers hold the keys to secrets beyond imagination. In this land, a spirited adventurer named Max embarked on a journey of numbers and magic.",
        #     f"Armed with an angle of {random_int_one} degrees, Max set out to unlock the secrets of radians through the enchantment of degrees_to_radians: ##degrees_to_radians({random_int_one}).",
        #     f"Continuing the adventure, Max encountered an ancient gate guarded by the sentinels of greatest common divisor. By invoking the sacred numbers {random_int_two} and {random_int_three}, Max unsealed the gate and uncovered its hidden knowledge: ##gcd({random_int_two}, {random_int_three}).",
        #     f"Stepping further into Mathoria's depths, Max discovered the scrolls of least common multiples, revealing the intricate links between {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
        #     f"Amidst the enchanting flora of the Numerical Grove, Max stumbled upon an ancient tree, a symbol of time's flow. The tree's age whispered through the power of isqrt, revealing itself as ##isqrt({random_int_three}).",
        #     f"As the sun painted the skies in hues of gold and lavender, Max harnessed the arcane powers of congruence. By invoking the pow_mod enchantment, {random_int_two} was raised to the power of {random_int_one}, modulo {random_int_four}, revealing a hidden gem: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
        #     f"In the river of time that flowed through Mathoria, Max rode its currents using the incantations of ceil, floor, and round. The river's surface reflected the profound difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
        #     f"As Max's adventure unfolded, the realization dawned that each mathematical function held the potential to unlock a new dimension of understanding. Armed with this insight, Max returned to Mathoria, sharing the tales of their journey, and inspiring others to explore the limitless wonders of numbers and magic.",
        # ],
        # [
        #     f"In the realm where numbers held the keys to the universe, a relentless mathematician embarked on a profound quest.",
        #     f"Their insatiable curiosity led them to unravel the enigmas woven around {random_int_one}, {random_int_two}, and {random_int_three}.",
        #     f"Their journey began with the enigmatic puzzle of the greatest value between {random_float} and {random_int_one}.",
        #     f"After deep contemplation, they unveiled the answer: ##greatest_value({random_float}, {random_int_one}).",
        #     f"But the allure of numbers beckoned further. Their focus shifted to {random_list}, an array of mystic numbers.",
        #     f"The mathematician revealed the concealed tale within, illuminating the secret product: ##product({random_list}).",
        #     f"Driven by a thirst for knowledge, they delved into the realm of factorials, exposing the enchantment of {random_int_one}!: ##factorial({random_int_one}).",
        #     f"Another puzzle awaited—the essence of {random_int_two}. Was it a prime number? The revelation emerged as ##is_prime({random_int_two}).",
        #     f"Undeterred, they embarked on the timeless journey for prime factors, unearthing the epic tale of {random_int_three}: ##prime_factors({random_int_three}).",
        #     f"In their exploration, they stumbled upon {random_int_four}, a number holding a secret—it was a perfect square: ##is_perfect_square({random_int_four}).",
        #     f"Continuing their odyssey, they unveiled the hidden truth of {random_int_three}, a concealed perfect cube: ##is_perfect_cube({random_int_three}).",
        #     f"With a heart ignited by the power of numbers, the mathematician returned to {random_list}, deciphering their collective story through the prism of the mean: ##mean({random_list}).",
        #     f"Yet, one last puzzle remained—the elusive median, the rhythmic pulse of the numbers: ##median({random_list}).",
        #     f"And thus, the mathematician's odyssey through the realm of numbers pressed on, revealing the intricate tapestry woven by the language of mathematics."
        # ],
        [
            f"In an age where numbers held the secrets of the universe...",
            f"A curious explorer stumbled upon an array of mysterious numbers: {random_list}.",
            f"Summoning the magic of order, the explorer invoked: ##ascending_sort({random_list}).",
            f"Amidst them, a captivating integer took center stage: {random_int_one}.",
            f"Pondering its essence, a question arose: Even or odd? The answer whispered: ##is_even({random_int_one}).",
            f"Revealing its dormant power, they unraveled its square: ##square_int({random_int_one}).",
            f"But within this enchantment, a spectral floating point number, {random_float}, appeared.",
            f"Venturing into the unknown, they conjured its squared form: ##square({random_float}).",
            f"With a leap of insight, they harnessed the magic of ten: ##power_of_ten({random_float}).",
            f"Emerging from the shadows, another integer emerged: {random_int_two}.",
            f"Exploring its essence, the explorer questioned: Odd or even? The answer emerged: ##is_odd({random_int_two}).",
            f"And its absolute truth was revealed: ##absolute({random_int_two}).",
            f"But fate had more in store, an enigmatic integer took the spotlight: {random_int_three}.",
            f"Delving into its enigma, the explorer discovered its cube: ##cube({random_int_three}).",
            f"Venturing deeper, they unlocked the essence of its cube root: ##cube_root(##cube({random_int_three})).",
            f"But the adventure had more surprises! A binary enigma emerged: {random_bool}.",
            f"Contemplating the cosmic dance, they invoked the ReLU magic for {random_float}: ##relu({random_float}).",
            f"Continuing the journey, an unexpected integer emerged: {random_int_four}.",
            f"Drawn by the unknown, they orchestrated a descent: ##descending_sort([{random_int_four}, {random_int_two}, {random_int_one}]).",
            f"And thus, the saga unfolded, a tapestry woven with calculations and revelations...",
            f"Through twists and turns, the explorer's journey continued, guided by the timeless allure of mathematics.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    masked_example = create_masked_token_batch_nine_example(1, Utility.get_spacy_nlp())
    print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example, PretrainTasks.MASKED_TOKEN_PREDICTION
    )
    print(sample)
#
#     next_token_example = create_next_token_batch_nine_example(1, Utility.get_spacy_nlp())
#     print(len(next_token_example), next_token_example)
