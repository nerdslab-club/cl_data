import random

import spacy

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_masked_token_batch_ten_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_ten_example_paragraph()
        for paragraph in paragraphs:
            masked_data = Utility.create_masked_input_output_example(paragraph, nlp)
            examples.extend(masked_data)
    return examples


def create_next_token_batch_ten_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_ten_example_paragraph()
        for paragraph in paragraphs:
            next_token_data = Utility.create_next_word_input_output_example(
                paragraph, nlp
            )
            examples.extend(next_token_data)
    return examples


def __get_batch_ten_example_paragraph():
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
        #     f"Amid the mystical realm of Mathoria, where numbers held the key to extraordinary feats, two intrepid scholars, Sophia and Oliver, embarked on an awe-inspiring journey to uncover the profound magic of mathematics.",
        #     f"Sophia, a brilliant mathematician, chose to begin her exploration by deciphering the enigmatic world of negative numbers. Her calculations unveiled the truth behind -2 times {random_int_one} times {random_int_two}, yielding the result: ##negative_2ab({random_int_one}, {random_int_two}).",
        #     f"Meanwhile, Oliver, a curious seeker of positivity, ventured into the realm of positive forces. Guided by his mathematical instincts, he harnessed the energy of 2 times {random_int_three} times {random_int_four}, revealing: ##positive_2ab({random_int_three}, {random_int_four}).",
        #     f"Sophia's path then led her through the labyrinth of quadratic expressions. With careful precision, she unraveled the complexity of {random_int_one}x + ({random_int_two}x + {random_int_three}), simplifying it to: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"Oliver, driven by curiosity, sought the symphony of polynomials. He harmoniously orchestrated {random_int_four}x^2 + {random_int_two}x + {random_int_three}x, with x = {random_int_one}, revealing its musical essence: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"As their journey unfolded, Sophia and Oliver united their strengths to unlock the profound mysteries of cubes. The fusion of their efforts, embracing {random_int_two} and {random_int_three}, revealed its concealed truths: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
        #     f"Undaunted by challenges, they delved deeper, encountering a captivating cube difference puzzle. They harnessed the cube of the sum of {random_int_one} and {random_int_four}, meticulously subtracting thrice their cosmic connection, revealing: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
        #     f"Their journey then led them to the world of expressive expansions. The ethereal incantation of ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2 bore a spellbinding inscription: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
        #     f"Their expedition then unraveled the enigma of cube disparities. The riddle unfurled, revealing the intricate difference between the sacred cube of {random_int_one} and the elusive cube of {random_int_four}: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
        #     f"At the zenith of their journey, Sophia and Oliver faced the ultimate cube challenge. Their insight resonated with cosmic harmonies, unveiling the cube of the difference between {random_int_two} and {random_int_three}, touched by the unity of three, emerging as: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
        #     f"In the end, Sophia and Oliver discovered that Mathoria's tapestry of numbers held the key to unlocking the secrets of the universe. Their journey became an enduring testament to the eternal allure of mathematical exploration.",
        #     f"Their legacy reverberated through the ages, inspiring future generations of Mathoria to embark on their own quests, driven by the endless wonder of numbers and the boundless realms they unveiled."
        # ],
        # [
        #     f"Embark on a mathematical voyage to Numaria, a realm where numbers weave the fabric of reality, and meet Jasper, a young mathematician.",
        #     f"Jasper's quest unfurled with the art of addition, merging {random_int_one} and {random_int_two} in a harmonious embrace through ##addition({random_int_one},{random_int_two}).",
        #     f"As twilight painted the sky, Jasper found himself entwined in the intricate dance of subtraction. The enigma between {random_int_two} and {random_int_three} revealed itself through ##subtraction({random_int_two},{random_int_three}).",
        #     f"Guided by the cosmic symphony, Jasper's spirit resonated with the allure of multiplication. He conjured the universe to unveil the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
        #     f"Like the dawn's first light, Jasper embarked on the path of division. With a flourish, he uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
        #     f"Jasper's insatiable curiosity propelled him to the cosmic dance of exponents. He raised {random_int_three} to the power of {random_int_four}, illuminating the universe's mysteries through ##exponentiation({random_int_three},{random_int_four}).",
        #     f"Beneath the silvery moonlight, Jasper's heart was drawn to the mystic realm of square roots. He whispered the incantation, unveiling the secrets of {random_int_four}'s square root through ##square_root({random_int_four}).",
        #     f"As the sun's rays graced the horizon, Jasper faced the enigma of floor division. With resolve, he deciphered the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
        #     f"In the cosmic tapestry of remainders, Jasper unraveled the hidden rhythm. The dance between {random_int_three} and {random_int_one} was unveiled through ##modulus({random_int_three},{random_int_one}).",
        #     f"Inscribed in the celestial heavens were the secrets of logarithms. Jasper contemplated the harmony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
        #     f"Embracing the cosmic ebb and flow, Jasper resonated with the celestial sine wave. With a profound connection to the universe, he unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        # ],
        # [
        #     f"Step into Arctopia, where numbers compose the very melodies of existence. Amidst this vibrant realm, inhabited by individuals as diverse as the digits themselves ({random_list}), the allure of mathematics thrives.",
        #     f"On an auspicious day, a mathematician embarked on a quest armed with an enigma: an angle, {random_float}. This angle, a key to unlocking the boundless chambers of trigonometry, revealed the cosmic choreography of cosine.",
        #     f"From the cosmic canvas emerged the essence of the unknown: the cosine of {random_float} radians, whispered by the universe itself: ##cosine({random_float}). The mathematician's journey now led to the revelation of its tangent.",
        #     f"The whisper of angles guided the mathematician to unravel the enigmatic tangent of ##arccosine({random_float}). This revelation held not only a numerical value, but also a profound insight etched within its mathematical essence.",
        #     f"Elsewhere in Arctopia, another soul was captivated by hyperbolic enigmas. Their fascination centered on the hyperbolic sine of {random_int_one}, a formula that seemed to reverberate through the corridors of time.",
        #     f"As twilight painted the sky with hues of curiosity, young minds gathered to decode the riddles of logarithms. Among them, the base-10 logarithm of {random_int_two} unveiled patterns that transcended the ordinary.",
        #     f"In the midst of this assembly, a prodigious child pondered the enigma of the cube root of ##hyperbolic_tangent({random_int_three}). A question that resonated with the essence of numbers and the limitless realm of possibilities.",
        #     f"Amid contemplation, a sage, guardian of ancient wisdom, contemplated the profound union of numbers and angles: ##logarithm_base_2({random_int_four}) raised to the celestial power of ##arcsine({random_float}).",
        #     f"As destiny wove its intricate threads, the two mathematicians converged, weaving their insights to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
        #     f"After a symphony of calculations, the answer was unveiled: {random_int_two + random_int_four}. Arctopia rejoiced, a grand celebration of intellect and discovery. And thus, the legacy of Arctopia's mathematical marvels continued to inspire."
        # ],
        # [
        #     f"Step into the enchanting world of Arithmos, a realm where numbers weave the tapestry of existence. Amidst its magic, a young seeker named Nora embarked on a journey of discovery and equations.",
        #     f"Bearing an angle of {random_int_one} degrees, Nora embarked on her quest to translate it into the cryptic language of radians. With the incantation degrees_to_radians, the transformation was unveiled: ##degrees_to_radians({random_int_one}).",
        #     f"As Nora ventured deeper, she stumbled upon an ancient gateway guarded by the sentinels of greatest common divisor. By invoking the spirits of {random_int_two} and {random_int_three}, she unlocked the gateway, revealing its hidden truths: ##gcd({random_int_two}, {random_int_three}).",
        #     f"Continuing her expedition, Nora unveiled the ancient scrolls of least common multiples, discovering the hidden unity between {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
        #     f"In the heart of Arithmos' sacred Numerical Grove, Nora encountered an ancient tree, a living testament to the passage of time. Through the art of isqrt, the tree's age was revealed to be ##isqrt({random_int_three}).",
        #     f"As twilight painted Arithmos with hues of amethyst and gold, Nora harnessed the essence of congruence. By invoking the pow_mod enchantment, she elevated {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, unveiling a hidden gem: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
        #     f"In a realm where time flowed like a river, Nora navigated its currents with the wisdom of ceil, floor, and round. The river's surface reflected the profound difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
        #     f"As Nora's journey unfolded, she realized that each mathematical function was a key to unlock a new dimension of understanding. Armed with this insight, she returned to Arithmos, sharing the tales of her adventure, inspiring others to embark on their own quests to unravel the mystique of numbers.",
        # ],
        # [
        #     f"In a realm where the language of numbers held sway, a relentless mathematician embarked on a voyage of discovery.",
        #     f"With unyielding curiosity, they set out to unravel the enigmas surrounding {random_int_one}, {random_int_two}, and {random_int_three}.",
        #     f"Their expedition commenced with the riddle of the greatest value between {random_float} and {random_int_one}.",
        #     f"After moments of contemplation, they revealed the answer: ##greatest_value({random_float}, {random_int_one}).",
        #     f"Yet, the allure of numbers beckoned them further. Their gaze turned to {random_list}, an array of cryptic numbers.",
        #     f"The mathematician brought to light the hidden story within, illuminating the elusive product: ##product({random_list}).",
        #     f"Fueled by an insatiable thirst for understanding, they ventured into the realm of factorials, revealing the enchantment of {random_int_one}!: ##factorial({random_int_one}).",
        #     f"Still, another mystery lay ahead—the essence of {random_int_two}. Was it a prime number? The truth emerged as ##is_prime({random_int_two}).",
        #     f"Undeterred, they embarked on the timeless pursuit of prime factors, unearthing the epic saga of {random_int_three}: ##prime_factors({random_int_three}).",
        #     f"In their journey, they stumbled upon {random_int_four}, a number that hid a secret—it was a perfect square: ##is_perfect_square({random_int_four}).",
        #     f"Continuing their odyssey, they unveiled the concealed truth of {random_int_three}, a hidden perfect cube: ##is_perfect_cube({random_int_three}).",
        #     f"With a heart ignited by the power of numbers, the mathematician returned to {random_list}, deciphering their collective story through the prism of the mean: ##mean({random_list}).",
        #     f"Yet, a final enigma remained—the elusive median, the rhythmic pulse of the numbers: ##median({random_list}).",
        #     f"And so, the mathematician's expedition through the realm of numbers persevered, revealing the intricate tapestry woven by the language of mathematics."
        # ],
        [
            f"In a distant land where numbers held the keys to the unknown...",
            f"An intrepid voyager stumbled upon an array of enigmatic numbers: {random_list}.",
            f"Eliciting the magic of order, the voyager summoned: ##ascending_sort({random_list}).",
            f"Among them, a captivating integer took its place: {random_int_one}.",
            f"Contemplating its nature, a question arose: Even or odd? The answer emerged: ##is_even({random_int_one}).",
            f"Unveiling its dormant power, they unraveled its square: ##square_int({random_int_one}).",
            f"But amidst this enchantment, a spectral floating point number, {random_float}, appeared.",
            f"Embarking on a journey into the unknown, they invoked its squared form: ##square({random_float}).",
            f"With a leap of insight, they harnessed the essence of ten: ##power_of_ten({random_float}).",
            f"Emerging from the shadows, another integer stepped into the light: {random_int_two}.",
            f"Exploring its nature, the voyager pondered: Odd or even? The truth emerged: ##is_odd({random_int_two}).",
            f"And its absolute truth was unveiled: ##absolute({random_int_two}).",
            f"But destiny had more to reveal, an enigmatic integer took center stage: {random_int_three}.",
            f"Delving into its mystery, the voyager discovered its cube: ##cube({random_int_three}).",
            f"Venturing deeper, they unlocked the essence of its cube root: ##cube_root(##cube({random_int_three})).",
            f"But the tale held more wonders! A binary enigma emerged: {random_bool}.",
            f"Reflecting on the cosmic dance, they invoked the ReLU magic for {random_float}: ##relu({random_float}).",
            f"Continuing the journey, an unexpected integer entered the scene: {random_int_four}.",
            f"Drawn by the allure of the unknown, they orchestrated a descent: ##descending_sort([{random_int_four}, {random_int_two}, {random_int_one}]).",
            f"And so, the saga continued, a tapestry woven with calculations and revelations...",
            f"Through twists and turns, the voyager's journey marched on, guided by the enduring enchantment of mathematics.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    masked_example = create_masked_token_batch_ten_example(1, Utility.get_spacy_nlp())
    print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example, PretrainTasks.MASKED_TOKEN_PREDICTION
    )
    print(sample)
#
#     next_token_example = create_next_token_batch_ten_example(1, Utility.get_spacy_nlp())
#     print(len(next_token_example), next_token_example)
