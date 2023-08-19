import random

import spacy

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_masked_token_batch_five_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_five_example_paragraph()
        for paragraph in paragraphs:
            masked_data = Utility.create_masked_input_output_example(paragraph, nlp)
            examples.extend(masked_data)
    return examples


def create_next_token_batch_five_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_five_example_paragraph()
        for paragraph in paragraphs:
            next_token_data = Utility.create_next_word_input_output_example(
                paragraph, nlp
            )
            examples.extend(next_token_data)
    return examples


def __get_batch_five_example_paragraph():
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
        #     f"Once upon a time, there were two mathematicians named Alice and Bob. They were given the task to solve various mathematical puzzles.",
        #     f"Alice decided to start with a puzzle involving negative numbers. She calculated -2 times {random_int_one} times {random_int_two} and got the result: ##negative_2ab({random_int_one}, {random_int_two}).",
        #     f"On the other hand, Bob wanted to work with positive numbers. He calculated 2 times {random_int_three} times {random_int_four} and found: ##positive_2ab({random_int_three}, {random_int_four}).",
        #     f"Alice then moved on to quadratic expressions. She took the expression {random_int_one}x + ({random_int_two}x + {random_int_three}) and simplified it to: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"Bob, however, was intrigued by polynomial expressions. He evaluated the expression {random_int_four}x^2 + {random_int_two}x + {random_int_three}x, with x = {random_int_one}, and found: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
        #     f"The two mathematicians then collaborated on some cube-related puzzles. They found the sum of cubes of {random_int_two} and {random_int_three} to be: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
        #     f"They also tackled a cube difference challenge. They calculated the cube of the sum of {random_int_one} and {random_int_four}, minus three times their product, resulting in: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
        #     f"As the puzzles continued, Alice and Bob encountered expressions involving squares. They expanded the expression ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2, leading to: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
        #     f"Their mathematical journey also included cube differences. They found the difference between the cube of {random_int_one} and the cube of {random_int_four} to be: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
        #     f"Finally, they tackled one last cube challenge. They computed the cube of the difference between {random_int_two} and {random_int_three}, plus three times their product, which resulted in: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
        #     f"In the end, Alice and Bob realized that their mathematical exploration had led them to a deeper understanding of these operations, and they were proud of their mathematical achievements."
        # ],
        # [
        #     f"Meet Lily, a young mathematician whose curiosity was as boundless as the universe itself.",
        #     f"Once, while wandering through the realm of numbers, Lily encountered a challenge - to find the sum of {random_int_one} and {random_int_two}. With a twinkle in her eye, she effortlessly unveiled the answer through ##addition({random_int_one},{random_int_two}).",
        #     f"In her quest for wisdom, Lily stumbled upon the riddle of subtraction. The difference between {random_int_two} and {random_int_three} was gracefully revealed through ##subtraction({random_int_two},{random_int_three}).",
        #     f"The symphony of multiplication beckoned to Lily's inquisitive mind. She danced with the universe, unlocking the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
        #     f"As the stars whispered their secrets, Lily's thoughts turned to the art of division. With a stroke of insight, she unraveled the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
        #     f"In the cosmic theater of exponents, Lily embarked on a journey of discovery. She raised {random_int_three} to the power of {random_int_four}, illuminating the cosmos through ##exponentiation({random_int_three},{random_int_four}).",
        #     f"Beneath the luminous moonlight, Lily encountered a hidden realm - the enchanting domain of square roots. With grace and precision, she unveiled the secrets of {random_int_four}'s square root through ##square_root({random_int_four}).",
        #     f"As dawn painted the horizon, Lily faced the enigmatic puzzle of floor division. With a heart full of wonder, she demystified the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
        #     f"Guided by the stars, Lily ventured into the labyrinth of remainders. The dance between {random_int_three} and {random_int_one} revealed its elegant rhythm through ##modulus({random_int_three},{random_int_one}).",
        #     f"Inscribed in the cosmic scrolls was the language of logarithms. Lily pondered the symphony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
        #     f"Nestled in the tranquil embrace of the universe, Lily embraced the cosmic sine wave. With a profound connection to the cosmos, she unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        # ],
        # [
        #     f"Welcome to Arctopia, a realm where the art of numbers weaves enchanting tales. Amidst the vibrant community with its unique inhabitants ({random_list}), the mystical charm of mathematics reigns supreme.",
        #     f"One auspicious day, a curious mathematician embarked on a journey, armed with the enigma of an angle: {random_float}. Their quest led them to the threshold of trigonometry, where the cosmic dance of cosine awaited.",
        #     f"The revelation of the cosmos unveiled the very essence of the unknown: the cosine of {random_float} radians, a secret whispered by the universe itself: ##cosine({random_float}). The mathematician's path now led to uncover the secrets of its tangent.",
        #     f"Intrigued by the whispering winds of trigonometric secrets, the mathematician ventured to reveal the enigmatic tangent of ##arccosine({random_float}). The answer held not just a value, but a profound realization.",
        #     f"Across the enchanting land, another mathematical soul was entranced by hyperbolic wonders. Their fascination centered on the hyperbolic sine of {random_int_one}, an equation etched into the very fabric of the realm.",
        #     f"As twilight painted the sky with hues of mystique, young minds gathered to decipher the riddles of logarithms. Among them, the base-10 logarithm of {random_int_two} was unveiled, revealing patterns that transcended the ordinary.",
        #     f"Amidst this gathering, a prodigious child pondered the enigma of the cube root of ##hyperbolic_tangent({random_int_three}). It was a question that resonated with the essence of both numbers and possibility.",
        #     f"Lost in contemplation, a sage immersed in ageless wisdom pondered the profound result when the whisper of numbers meets the dance of angles: ##logarithm_base_2({random_int_four}) raised to the celestial power of ##arcsine({random_float}).",
        #     f"As destiny wove its intricate threads, the two mathematicians converged, intertwining their wisdom to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
        #     f"After an intricate dance of calculations, the answer revealed itself: {random_int_two + random_int_four}. Arctopia erupted in celebration, a grand symphony of intellect and discovery. And thus, the legacy of Arctopia's mathematical marvels continued to inspire generations."
        # ],
        # [
        #     f"Once upon a numerical universe, where equations whispered and shapes danced, a young math enthusiast named Lily embarked on a journey of exploration.",
        #     f"Lily's first step was to translate {random_int_one} degrees into the enigmatic language of radians, invoking the powers of degrees_to_radians: ##degrees_to_radians({random_int_one}).",
        #     f"Lost in a forest of numbers, Lily stumbled upon a door that could only be unlocked with the mystical key of greatest common divisor. By unlocking {random_int_two} and {random_int_three}, she revealed the door's secrets: ##gcd({random_int_two}, {random_int_three}).",
        #     f"Venturing further, Lily discovered the ancient scrolls of least common multiples, which disclosed the cryptic truths behind {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
        #     f"Amidst a landscape of numerical wonders, Lily encountered an ancient tree that grew only integer roots. Invoking the power of isqrt, she unveiled the tree's age, which was ##isqrt({random_int_three}).",
        #     f"Exploring the realm of congruence, Lily harnessed the pow_mod enchantment. By raising {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, she discovered a hidden treasure: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
        #     f"As time flowed like a river, Lily rode its currents using the magic of ceil, floor, and round. The river's surface reflected the mysterious difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
        #     f"Guided by her passion, Lily realized that each function held the key to unlocking the universe's mathematical secrets. With each calculation, she drew closer to the heart of understanding.",
        #     f"With newfound wisdom and an unquenchable curiosity, Lily returned to her peers, sharing the tale of her journey. Her story ignited a spark, inspiring others to explore the boundless realms of numbers and imagination.",
        # ],
        # [
        #     f"Once in a realm ruled by numbers, a curious mathematician thrived.",
        #     f"This inquisitive mind pondered the enigmas of {random_int_one}, {random_int_two}, and {random_int_three}.",
        #     f"Their quest began with the riddle of the greatest value between {random_float} and {random_int_one}.",
        #     f"After deep contemplation, they unveiled the answer: ##greatest_value({random_float}, {random_int_one}).",
        #     f"Yet, their thirst for knowledge remained unquenched. They turned their gaze to {random_list}, an array of mystical numbers.",
        #     f"The mathematician unveiled the hidden tale within, revealing the secret product: ##product({random_list}).",
        #     f"Fascinated by the arcane power of factorials, they ventured into the realm of {random_int_one}! and found it to be ##factorial({random_int_one}).",
        #     f"A new mystery awaited them—{random_int_two}. Was it a prime number? The answer materialized as ##is_prime({random_int_two}).",
        #     f"But the journey persisted. They sought the age-old wisdom of prime factors for {random_int_three}, uncovering ##prime_factors({random_int_three}).",
        #     f"Amidst their exploration, they stumbled upon {random_int_four}, concealing a secret: it was a perfect square. ##is_perfect_square({random_int_four}).",
        #     f"Their odyssey continued as they unveiled the enigma of {random_int_three}, a hidden perfect cube: ##is_perfect_cube({random_int_three}).",
        #     f"A heart brimming with numbers, the mathematician returned to {random_list}, revealing the essence of their collective tale: the mean—##mean({random_list}).",
        #     f"Yet one enigma remained—the median, an elusive thread woven through the numbers: ##median({random_list}).",
        #     f"And so, the mathematician's journey through the numinous realm persisted, unraveling the mathematical tapestry's intricate beauty."
        # ],
        [
            f"Once in a realm where numbers danced like stars...",
            f"A daring explorer stumbled upon an array of mystical numbers: {random_list}.",
            f"With a wave of the mathematical wand, the explorer invoked: ##ascending_sort({random_list}).",
            f"Among them, a captivating integer took center stage: {random_int_one}.",
            f"Pondering its essence, a question arose: Even or odd? The answer resounded: ##is_even({random_int_one}).",
            f"Unlocking its hidden might, they revealed its square: ##square_int({random_int_one}).",
            f"But amidst the enchantment, a ethereal floating number, {random_float}, emerged.",
            f"Venturing into the unknown, they conjured its squared form: ##square({random_float}).",
            f"With a leap of imagination, they harnessed the power of ten: ##power_of_ten({random_float}).",
            f"Emerging from the shadows, a different integer took the spotlight: {random_int_two}.",
            f"Probing its nature, the explorer inquired: Odd or even? The truth was unveiled: ##is_odd({random_int_two}).",
            f"And its absolute nature revealed: ##absolute({random_int_two}).",
            f"Yet destiny had more in store, an enigmatic integer appeared: {random_int_three}.",
            f"Unraveling its puzzle, the explorer discovered its cube: ##cube({random_int_three}).",
            f"Peering deeper, they unearthed the essence of its cube root: ##cube_root(##cube({random_int_three})).",
            f"But the voyage held more wonders! A binary enigma appeared: {random_bool}.",
            f"Contemplating the universe, they invoked the ReLU magic for {random_float}: ##relu({random_float}).",
            f"Further along, an unexpected integer materialized: {random_int_four}.",
            f"Guided by curiosity, they orchestrated a descent: ##descending_sort([{random_int_four}, {random_int_two}, {random_int_one}]).",
            f"Thus, the saga continued, a symphony of calculations and revelations...",
            f"Through twists and turns, the explorer's journey danced, guided by the timeless magic of mathematics.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    masked_example = create_masked_token_batch_five_example(1, Utility.get_spacy_nlp())
    print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example, PretrainTasks.MASKED_TOKEN_PREDICTION
    )
    print(sample)
#
#     next_token_example = create_next_token_batch_five_example(1, Utility.get_spacy_nlp())
#     print(len(next_token_example), next_token_example)
