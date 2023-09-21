import random

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def get_batch_six_example_paragraph():
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
            f"Deep in the heart of the Enchanted Mathematica Forest, two intrepid explorers, Alex and Morgan, embarked on a quest to unlock the secrets of mathematical wonders.",
            f"Alex, the fearless adventurer, took on the challenge of unraveling the mysteries of negative numbers. Their first task involved calculating -2 times {random_int_one} times {random_int_two}, which yielded the result: ##negative_2ab({random_int_one}, {random_int_two}).",
            f"Morgan, a keen observer of positive phenomena, decided to explore the other side of the coin. They delved into the world of positive numbers, finding that 2 times {random_int_three} times {random_int_four} equaled: ##positive_2ab({random_int_three}, {random_int_four}).",
            f"The journey led Alex to quadratic landscapes, where they encountered the expression {random_int_one}x + ({random_int_two}x + {random_int_three}). With deft calculations, Alex simplified it to: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
            f"Morgan, however, set their sights on a realm of polynomial wonders. Substituting x = {random_int_one} into {random_int_four}x^2 + {random_int_two}x + {random_int_three}x, they uncovered: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
            f"Yet, the true magic occurred when Alex and Morgan united their powers to solve puzzles involving cubes. The sum of cubes of {random_int_two} and {random_int_three} revealed itself as: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
            f"Collaborating further, they faced a cube difference riddle. Combining the cube of the sum of {random_int_one} and {random_int_four}, minus three times their product, led to: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
            f"The intrepid duo's journey through mathematical landscapes extended to expressions involving squares. Expanding ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2 revealed: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
            f"Yet another enchanting twist awaited them – cube differences. The difference between the cube of {random_int_one} and the cube of {random_int_four} unfolded as: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
            f"At last, their expedition reached a crescendo with the ultimate cube challenge. The cube of the difference between {random_int_two} and {random_int_three}, plus three times their product, emerged as: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
            f"As the sun set on their adventure, Alex and Morgan marveled at the mathematical landscapes they had traversed. Their shared journey had unlocked new realms of knowledge, reinforcing their belief that the Enchanted Mathematica Forest held endless wonders waiting to be discovered."
        ],
        [
            f"Once upon a mathematical odyssey, there was a young explorer named Max.",
            f"Max embarked on a quest to decipher the language of numbers. His journey began by adding {random_int_one} and {random_int_two}, unveiling the hidden sum through ##addition({random_int_one},{random_int_two}).",
            f"Guided by the stars, Max encountered the enigma of subtraction. The dance between {random_int_two} and {random_int_three} was unveiled through ##subtraction({random_int_two},{random_int_three}).",
            f"In the grand symphony of multiplication, Max composed a masterpiece. The universe revealed the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
            f"As dawn illuminated the path, Max ventured into the realm of division. With a spark of insight, he uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
            f"Max's thirst for knowledge led him to the cosmic realm of exponents. He raised {random_int_three} to the power of {random_int_four}, unleashing the universe's secrets through ##exponentiation({random_int_three},{random_int_four}).",
            f"Beneath the moon's gentle glow, Max found himself drawn to the mystical domain of square roots. The universe whispered its secrets as he revealed the square root of {random_int_four} through ##square_root({random_int_four}).",
            f"As the day's first light appeared, Max faced the puzzle of floor division. With determination, he solved the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
            f"In the intricate dance of numbers, Max discovered the rhythm of remainders. The universe unveiled the dance between {random_int_three} and {random_int_one} through ##modulus({random_int_three},{random_int_one}).",
            f"Inscribed in the cosmic tapestry were the secrets of logarithms. Max pondered the harmonious symphony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
            f"Nestled in the embrace of the cosmos, Max embraced the celestial sine wave. With a profound connection to the universe, he unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        ],
        [
            f"Welcome to Arctopia, a realm where numbers compose the symphony of existence. Among the vibrant community, each with their unique attributes ({random_list}), the allure of mathematics resonates.",
            f"A day of destiny arrived as a curious mathematician embarked on a quest, armed with the enigma of an angle: {random_float}. This angle led them through the corridors of trigonometry, where the cosmic choreography of cosine awaited.",
            f"From the cosmic canvas, the mathematician extracted the essence of the unknown: the cosine of {random_float} radians, whispered by the universe itself: ##cosine({random_float}). The next step beckoned — the discovery of its tangent.",
            f"The whisper of angles guided the mathematician to unveil the enigmatic tangent of ##arccosine({random_float}). The revelation held not only a numerical value but a profound revelation within its folds.",
            f"Elsewhere in the realm, another mathematical spirit was captivated by hyperbolic mysteries. Their fascination centered on the hyperbolic sine of {random_int_one}, a formula that seemed to echo through time.",
            f"As twilight painted the sky with hues of contemplation, young minds gathered to decode the enigma of logarithms. Among them, the base-10 logarithm of {random_int_two} unfolded, revealing patterns that transcended the mundane.",
            f"Amid this assembly, a prodigious child pondered the riddle of the cube root of ##hyperbolic_tangent({random_int_three}). A question that resonated with the essence of numbers and the boundless realm of possibilities.",
            f"Lost in thought, a sage, a guardian of ancient wisdom, contemplated the profound convergence of numbers and angles: ##logarithm_base_2({random_int_four}) raised to the ethereal power of ##arcsine({random_float}).",
            f"As destiny entwined its threads, the two mathematicians united, weaving their insights to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
            f"After a symphony of calculations, the answer materialized: {random_int_two + random_int_four}. Arctopia rejoiced, a grand celebration of intellect and discovery. And so, the legacy of Arctopia's mathematical marvels illuminated the path forward."
        ],
        [
            f"Amidst the sprawling landscapes of Mathovia, a realm woven with numbers and enigmas, a young adventurer named Ava embarked on an exhilarating quest.",
            f"Equipped with an angle of {random_int_one} degrees, Ava embarked on a journey to translate it into the mystical language of radians, invoking the formula degrees_to_radians: ##degrees_to_radians({random_int_one}).",
            f"As she delved deeper into the heart of Mathovia, Ava stumbled upon a doorway guarded by the guardians of greatest common divisor. Unlocking the door with the sacred numbers {random_int_two} and {random_int_three}, she uncovered its secrets: ##gcd({random_int_two}, {random_int_three}).",
            f"Venturing further, Ava discovered the ancient manuscripts of least common multiples, unveiling the arcane wisdom that linked {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
            f"Guided by her passion, Ava encountered an ancient tree deep within the Forest of Numbers. The tree's age was revealed to her through the magic of isqrt, standing at ##isqrt({random_int_three}).",
            f"As twilight bathed Mathovia in hues of purple and gold, Ava embraced the power of congruence. By wielding the pow_mod enchantment, she raised {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, uncovering a hidden treasure: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
            f"In the realm where time flowed like a river, Ava navigated its currents using the incantations of ceil, floor, and round. The river's surface reflected the profound difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
            f"As Ava's journey drew to a close, she realized that each mathematical function was a key to unlocking the infinite mysteries of Mathovia. Armed with this wisdom, she returned to her homeland, sharing the tales of her adventures and inspiring others to embark on their own mathematical odysseys.",
        ],
        [
            f"Long ago, in a world where numbers held secrets, a curious mathematician's journey began.",
            f"This inquisitive mind delved into the mysteries of {random_int_one}, {random_int_two}, and {random_int_three}.",
            f"Their adventure commenced with the puzzle of the greatest value between {random_float} and {random_int_one}.",
            f"After moments of reflection, they revealed the answer: ##greatest_value({random_float}, {random_int_one}).",
            f"But the horizon of knowledge beckoned. Their attention turned to {random_list}, an array of arcane numbers.",
            f"The mathematician unraveled the hidden narrative, exposing the enigmatic product: ##product({random_list}).",
            f"Entranced by the magic of factorials, they journeyed into {random_int_one}!, discovering its mystical essence: ##factorial({random_int_one}).",
            f"Yet, another enigma awaited—the nature of {random_int_two}. Was it a prime number? The truth emerged as ##is_prime({random_int_two}).",
            f"Their quest persisted. They embarked on the ancient path of prime factors, unveiling the tale of {random_int_three}: ##prime_factors({random_int_three}).",
            f"Amidst their exploration, they stumbled upon {random_int_four}, a number with a secret—it was a perfect square: ##is_perfect_square({random_int_four}).",
            f"Their journey unveiled the truth of {random_int_three}, a hidden perfect cube: ##is_perfect_cube({random_int_three}).",
            f"A heart filled with numbers, the mathematician returned to {random_list}, deciphering the collective story through the lens of the mean: ##mean({random_list}).",
            f"Yet, a final mystery remained—the elusive median, the heartbeat of the numbers: ##median({random_list}).",
            f"And thus, the mathematician's odyssey through the realm of numbers endured, revealing the intricate tapestry woven by mathematics."
        ],
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
        ],
        [
            f"In a realm where numbers held both secrets and revelations,",
            f"an intriguing array of numbers unveiled itself: {random_list}.",
            f"From this array, the mightiest of numbers emerged: ##max_value({random_list}).",
            f"Yet, the most unassuming of them stepped forward: ##min_value({random_list}).",
            f"Amidst this domain of numbers, a lone integer took center stage:",
            f"{random_int_one}, an enigmatic figure with untold significance.",
            f"Soon after, another integer entered the stage, identified as",
            f"{random_int_two}, born from the fusion of {random_int_one} and another mysterious integer.",
            f"As the plot unfolded, another integer came into play:",
            f"{random_int_three}, the outcome of {random_int_two} merging with another cryptic value.",
            f"But this tale wasn't confined to numbers alone; a random float,",
            f"{random_float}, made a brief appearance, igniting curiosity.",
            f"Guided by mathematical sorcery, the cube root of {random_int_one} was revealed:",
            f"##nth_root({random_int_one}, 3) manifested as the key to unlocking this mystery.",
            f"In the symphony of numbers, the geometric mean of the list whispered its melody:",
            f"##geometric_mean({random_list}) bestowed its hidden melody upon the scene.",
            f"A lingering question emerged: Was {random_int_one} a power of two?",
            f"The answer emerged: ##is_power_of_two({random_int_one}).",
            f"Binary whispers danced, as {random_int_one} transformed into binary code:",
            f"##decimal_to_binary({random_int_one}) unveiled its binary essence.",
            f"Then, in a twist of enchantment, binary metamorphosed back to its primal form:",
            f"##binary_to_decimal(##decimal_to_binary({random_int_one})) revealed its innate truth.",
            f"The magic of symmetry unveiled {random_int_one} as a palindrome:",
            f"##is_palindrome({random_int_one}) affirmed its symmetrical nature.",
            f"The saga continued as the digits of {random_int_two} unveiled their collective secret:",
            f"##sum_of_digits({random_int_two}) divulged the sum of these individual components.",
            f"In the realm of triangles, with sides {random_int_one} and {random_int_two},",
            f"the enigmatic hypotenuse emerged: ##hypotenuse({random_int_one}, {random_int_two}).",
            f"And so, the chronicle of numbers, calculations, and enigmas gracefully concluded,",
            f"leaving a legacy of mathematical marvels and an eternal quest for discovery."
        ],
        [
            f"In the realm of mathematical marvels, a circle emerged with a radius of {random_float}. Its arcane area, discovered through ##circle_area({random_float}), held secrets as profound as the universe itself.",
            f"A gathering of {random_int_one} individuals, plucked from a pool of {random_int_two}, orchestrated a dance of permutations through ##permutation({random_int_two}, {random_int_one}). The arrangement was a masterpiece of mathematical choreography.",
            f"Amidst the mathematical symphony, {random_int_two} harmonious notes were selected from a collection of {random_int_three}, forming a symphonic combination encoded by ##combination({random_int_three}, {random_int_two}).",
            f"A numerical transformation akin to fate's inversion was unveiled. The enigmatic number {random_float}, when subjected to ##invert_number({random_float}), revealed its cryptic mirror image.",
            f"Venturing into the integer realm, {random_float} exposed its inner integer essence through ##float_to_int({random_float}). The transition echoed the dual nature of numbers, a delicate balance of distinct worlds.",
            f"The integer {random_int_three} embarked on a metamorphosis, shedding its integer form and embracing a floating existence via ##int_to_float({random_int_three}). This transformation signified a fluid dance between mathematical identities.",
            f"From the canvas of sequences arose a geometric series, with an overture of {random_float}, a recurring motif of {random_float}, and a crescendo of {random_int_one} iterations, harmonized through ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"The sigmoid curve, a harbinger of transition, enveloped {random_float}. Its unveiling, marked by a value of ##sigmoid({random_float}), symbolized the journey from obscurity to revelation.",
            f"Two vectors, depicted as {random_list} and {random_list}, embarked on a dance of resonance. Their hidden kinship, quantified by the cosine similarity, emerged as ##cosine_similarity(eval({random_list}), eval({random_list})), a testament to their alignment.",
            f"The cryptic Euler's totient function beckoned, unraveling the mysteries of {random_int_four}. Its pronouncement, ##euler_totient({random_int_four}), resonated with the secret patterns woven through prime numbers.",
            f"As the story drew to a close, the echoes of mathematical revelations lingered, whispering of the profound beauty that numbers and equations concealed."
        ],
        [
            f"Long ago, within the realm of mathematical wonders, there arose a vector adorned with the elements {random_list}.",
            f"Its length, determined by ##length({random_list}), revealed itself, as did its L1 norm, calculated as ##l1_norm({random_list}).",
            f"Venturing further, it delved into the realm of L2 norms, discovering its own to be ##l2_norm({random_list}).",
            f"Meanwhile, the kingdom witnessed the emergence of four integers: {random_int_one}, {random_int_two}, {random_int_three}, and {random_int_four}.",
            f"The sum of the first two integers materialized as ##sum([{random_int_one}, {random_int_two}]), while the combined sum of all four was revealed to be ##sum([{random_int_one}, {random_int_two}, {random_int_three}, {random_int_four}]).",
            f"Curiosity led to the calculation of an average, pondering over {random_int_one}, {random_int_two}, and {random_int_three}, resulting in ##average([{random_int_one}, {random_int_two}, {random_int_three}]).",
            f"Amidst the numerical symphony, a floating point number, {random_float}, gracefully appeared, introducing an element of randomness.",
            f"A question of truth arose, and the answer was found in the value of truth itself: {random_bool}.",
            f"The mystical π made its appearance, evoking a sense of wonder: ##get_pi().",
            f"Similarly, the enigmatic constant e made its presence felt: ##get_e().",
            f"Two vectors, each possessing the elements {random_list} and {random_list}, embarked on a collaborative quest to uncover their dot product.",
            f"After intricate calculations, their journey unveiled the dot product as ##calculate_dot_product({random_list}, {random_list}).",
            f"In a twist of logic, it was revealed that 'Racecar' remained unchanged even when reversed: ##check_same_string('racecar', ##reverse_string('racecar')).",
            f"In the enchanting domain of mathematical marvels, numbers reigned supreme, weaving a tapestry of intrigue and fascination."
        ],
        [
            f"In the mesmerizing world of Numeterra, two adventurous companions, {random_list[0]} and {random_list[1]}, embarked on an exhilarating mathematical expedition.",
            f"Fueled by their insatiable fascination with numbers, {random_list[0]} stumbled upon the hidden magic within the square of the sum of two numbers.",
            f"As their revelation unfolded, a formula emerged: ({random_int_one}) plus ({random_int_two}) whole square equals ##a_plus_b_whole_square({random_int_one},{random_int_two}).",
            f"The formula revealed its elegance when expanded: ({random_int_one} squared) plus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared). This intricate dance of numbers resulted in ##a_squared_plus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"On a parallel journey, {random_list[1]} unraveled another enigmatic puzzle. The square of the difference between two numbers, resonating with the power of four times their product, unveiled its secrets.",
            f"The cryptic equation unfurled: ({random_int_two} minus {random_int_three}) whole squared plus (4 times {random_int_two} times {random_int_three}). This mystery unraveled as ##a_minus_b_whole_squared_plus_4ab({random_int_two},{random_int_three}).",
            f"As their voyage continued, they encountered the essence of simplicity within complexity. The square of the difference between two numbers, distilled to its purest form:",
            f"({random_int_one} minus {random_int_four}) whole squared, guarded its secret within its simplicity. This revelation transformed into ##a_minus_b_whole_squared({random_int_one},{random_int_four}).",
            f"Delving deeper, they discovered the captivating interplay of squares and differences, intricately woven in an elegant waltz:",
            f"The difference between the squares of {random_int_one} and {random_int_two}, a symphony of numbers orchestrated through ({random_int_one} squared) minus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared). This mathematical ballet led them to ##a_squared_minus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"Yet, their journey remained incomplete without an encounter with the square of the sum of two numbers, shedding the weight of four times their dance:",
            f"({random_int_two} plus {random_int_three}) whole squared, a tale of numbers in harmony and divergence, unfurling as ##a_plus_b_whole_squared_minus_4ab({random_int_two},{random_int_three}).",
            f"In the expansive tapestry of Numeterra, they unearthed a gem of simplicity amid complexity, the heart of their expedition encapsulated:",
            f"The sum of the squares of {random_int_two} and {random_int_three}, a harmonious duet in ({random_int_two} squared) plus ({random_int_three} squared), revealing the essence of ##a_squared_plus_b_squared({random_int_two},{random_int_three}).",
            f"Their odyssey through Numeterra endured, a symphony of exploration driven by their unwavering passion for numbers and the graceful choreography of calculations.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator

    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_six_example_paragraph(),
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
        get_batch_six_example_paragraph(),
        1,
    )
    sample = Utility.create_sample_from_example(
        next_token_example, PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
