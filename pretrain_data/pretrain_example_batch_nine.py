import random

from cl_data.src.constants import PretrainTasks
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def get_batch_nine_example_paragraph():
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
            f"In the realm of Arithmos, a land where numbers held the secrets of magic, two intrepid seekers, Maya and Eli, set forth on a quest to unveil the mysteries of mathematical marvels.",
            f"Maya, a fearless mathematician, embarked on her journey by delving into the enigmatic realm of negative numbers. Through intricate calculations, she unveiled the hidden truth behind -2 times {random_int_one} times {random_int_two}, yielding the result: ##negative_2ab({random_int_one}, {random_int_two}).",
            f"Meanwhile, Eli, an inquisitive explorer, turned his attention to the world of positivity. Guided by curiosity, he harnessed the mathematical forces to master 2 times {random_int_three} times {random_int_four}, revealing: ##positive_2ab({random_int_three}, {random_int_four}).",
            f"Maya's path then led her through the maze of quadratic equations. She skillfully simplified the intricate expression {random_int_one}x + ({random_int_two}x + {random_int_three}) into a more elegant form: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
            f"Eli, on the other hand, was drawn to the captivating symphony of polynomials. He harmonized the elements of {random_int_four}x^2 + {random_int_two}x + {random_int_three}x, with x = {random_int_one}, revealing its melodious essence: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
            f"As their journey unfolded, Maya and Eli united their strengths to unlock the ancient wisdom of cubes. The fusion of cubical energies, embracing {random_int_two} and {random_int_three}, revealed its arcane secrets: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
            f"Undaunted by challenges, they advanced further, encountering a profound puzzle involving cube differences. They harnessed the cube of the sum of {random_int_one} and {random_int_four}, meticulously subtracting thrice their cosmic connection, revealing: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
            f"Their journey then led them to unravel expressive expansions. The mystical incantation of ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2, bore an intricate inscription: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
            f"Their expedition then ventured into the enigma of cube disparities. The riddle unraveled, revealing the profound difference between the sacred cube of {random_int_one} and the elusive cube of {random_int_four}: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
            f"At the zenith of their journey, Maya and Eli faced the ultimate cube challenge. Their insight harmonized with cosmic vibrations, unveiling the cube of the difference between {random_int_two} and {random_int_three}, touched by the trinity of unity, emerging as: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
            f"In the end, Maya and Eli discovered that in Arithmos, the language of numbers held the power to reveal the secrets of the universe, and their quest became an eternal testament to the beauty of mathematical exploration.",
            f"Their legacy echoed through generations, inspiring the curious minds of Arithmos to embark on their own quests, guided by the enchanting allure of numbers and the infinite worlds they unveiled.",
        ],
        [
            f"Venture into the realm of Equatia, where the young scholar, Oliver, sought to unlock the language of numbers.",
            f"Oliver's journey commenced with the elegant art of addition, merging {random_int_one} and {random_int_two} in perfect harmony through ##addition({random_int_one},{random_int_two}).",
            f"As the sun dipped below the horizon, Oliver found himself entwined in the intricate dance of subtraction. The enigmatic rhythm between {random_int_two} and {random_int_three} revealed itself through ##subtraction({random_int_two},{random_int_three}).",
            f"Guided by the constellations, Oliver's spirit resonated with the symphony of multiplication. He conducted the universe to unveil the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
            f"Like the first light of dawn, Oliver embarked on the path of division. With grace, he uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
            f"Oliver's insatiable curiosity led him to the cosmic dance of exponents. He elevated {random_int_three} to the power of {random_int_four}, revealing the universe's mysteries through ##exponentiation({random_int_three},{random_int_four}).",
            f"Beneath the enchanting moonlight, Oliver's heart was drawn to the mystic realm of square roots. He whispered the incantation, unveiling the secrets of {random_int_four}'s square root through ##square_root({random_int_four}).",
            f"As the first rays of sunlight graced the sky, Oliver faced the puzzle of floor division. With determination, he deciphered the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
            f"In the cosmic symphony of remainders, Oliver uncovered the hidden rhythm. The dance between {random_int_three} and {random_int_one} was unveiled through ##modulus({random_int_three},{random_int_one}).",
            f"Inscribed in the constellations were the secrets of logarithms. Oliver contemplated the harmony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
            f"Embracing the cosmos, Oliver resonated with the celestial sine wave. With a profound connection to the universe, he unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        ],
        [
            f"Journey into Arctopia, where numbers dance in harmony and equations tell tales of wonder. Amidst this vibrant realm, home to a diverse community reminiscent of the digits themselves ({random_list}), the enchantment of mathematics reigns.",
            f"Amidst the stars, a mathematician embarked on a quest with an enigma in hand: an angle, {random_float}. This angle, a key to unlocking the treasure troves of trigonometry, unveiled the cosmic rhythm of cosine.",
            f"From the celestial canvas emerged the very essence of the unknown: the cosine of {random_float} radians, whispered by the cosmos itself: ##cosine({random_float}). The mathematician's odyssey now led to the unraveling of its tangent.",
            f"The whisper of angles guided the mathematician to reveal the enigmatic tangent of ##arccosine({random_float}). This revelation held not just a value, but a profound insight etched within the tapestry of mathematics.",
            f"Across Arctopia, another soul was entranced by hyperbolic mysteries. Their fascination centered around the hyperbolic sine of {random_int_one}, a formula resonating with the echoes of time.",
            f"As twilight cast its hues of curiosity, young minds gathered to decode the riddles of logarithms. Among them, the base-10 logarithm of {random_int_two} unveiled patterns transcending the ordinary.",
            f"In this gathering, a prodigious child pondered the enigma of the cube root of ##hyperbolic_tangent({random_int_three}). A question that resonated with the essence of numbers and the limitless expanse of possibilities.",
            f"Amid contemplation, a sage, guardian of ancient wisdom, pondered the profound union of numbers and angles: ##logarithm_base_2({random_int_four}) raised to the celestial power of ##arcsine({random_float}).",
            f"As destiny's threads wove intricate patterns, the two mathematicians converged, merging their insights to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
            f"After a symphony of calculations, the answer was revealed: {random_int_two + random_int_four}. Arctopia celebrated, a grand gala honoring intellect and discovery. Thus, the legacy of Arctopia's mathematical marvels continued to illuminate paths ahead.",
        ],
        [
            f"Welcome to the mystical land of Mathoria, a realm where numbers hold the keys to secrets beyond imagination. In this land, a spirited adventurer named Max embarked on a journey of numbers and magic.",
            f"Armed with an angle of {random_int_one} degrees, Max set out to unlock the secrets of radians through the enchantment of degrees_to_radians: ##degrees_to_radians({random_int_one}).",
            f"Continuing the adventure, Max encountered an ancient gate guarded by the sentinels of greatest common divisor. By invoking the sacred numbers {random_int_two} and {random_int_three}, Max unsealed the gate and uncovered its hidden knowledge: ##gcd({random_int_two}, {random_int_three}).",
            f"Stepping further into Mathoria's depths, Max discovered the scrolls of least common multiples, revealing the intricate links between {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
            f"Amidst the enchanting flora of the Numerical Grove, Max stumbled upon an ancient tree, a symbol of time's flow. The tree's age whispered through the power of isqrt, revealing itself as ##isqrt({random_int_three}).",
            f"As the sun painted the skies in hues of gold and lavender, Max harnessed the arcane powers of congruence. By invoking the pow_mod enchantment, {random_int_two} was raised to the power of {random_int_one}, modulo {random_int_four}, revealing a hidden gem: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
            f"In the river of time that flowed through Mathoria, Max rode its currents using the incantations of ceil, floor, and round. The river's surface reflected the profound difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
            f"As Max's adventure unfolded, the realization dawned that each mathematical function held the potential to unlock a new dimension of understanding. Armed with this insight, Max returned to Mathoria, sharing the tales of their journey, and inspiring others to explore the limitless wonders of numbers and magic.",
        ],
        [
            f"In the realm where numbers held the keys to the universe, a relentless mathematician embarked on a profound quest.",
            f"Their insatiable curiosity led them to unravel the enigmas woven around {random_int_one}, {random_int_two}, and {random_int_three}.",
            f"Their journey began with the enigmatic puzzle of the greatest value between {random_float} and {random_int_one}.",
            f"After deep contemplation, they unveiled the answer: ##greatest_value({random_float}, {random_int_one}).",
            f"But the allure of numbers beckoned further. Their focus shifted to {random_list}, an array of mystic numbers.",
            f"The mathematician revealed the concealed tale within, illuminating the secret product: ##product({random_list}).",
            f"Driven by a thirst for knowledge, they delved into the realm of factorials, exposing the enchantment of {random_int_one}!: ##factorial({random_int_one}).",
            f"Another puzzle awaited—the essence of {random_int_two}. Was it a prime number? The revelation emerged as ##is_prime({random_int_two}).",
            f"Undeterred, they embarked on the timeless journey for prime factors, unearthing the epic tale of {random_int_three}: ##prime_factors({random_int_three}).",
            f"In their exploration, they stumbled upon {random_int_four}, a number holding a secret—it was a perfect square: ##is_perfect_square({random_int_four}).",
            f"Continuing their odyssey, they unveiled the hidden truth of {random_int_three}, a concealed perfect cube: ##is_perfect_cube({random_int_three}).",
            f"With a heart ignited by the power of numbers, the mathematician returned to {random_list}, deciphering their collective story through the prism of the mean: ##mean({random_list}).",
            f"Yet, one last puzzle remained—the elusive median, the rhythmic pulse of the numbers: ##median({random_list}).",
            f"And thus, the mathematician's odyssey through the realm of numbers pressed on, revealing the intricate tapestry woven by the language of mathematics.",
        ],
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
        ],
        [
            f"Journey into a realm where numbers wield their magic and equations whisper secrets,",
            f"revealing an enigmatic array of numbers: {random_list}.",
            f"From this array, the mightiest number emerged: ##max_value({random_list}).",
            f"Yet, the most unassuming number stepped into the light: ##min_value({random_list}).",
            f"Amidst this domain of numbers, a solitary integer took the stage:",
            f"{random_int_one}, an enigma wrapped in numbers.",
            f"Soon after, another integer entered the stage, known as",
            f"{random_int_two}, born from the union of {random_int_one} and another cryptic number.",
            f"As the narrative unfolded, another integer came into play:",
            f"{random_int_three}, forged from the fusion of {random_int_two} and a hidden value.",
            f"But this tale was more than just numbers; a random float,",
            f"{random_float}, made a fleeting appearance, sparking intrigue.",
            f"With the power of math, the cube root of {random_int_one} was revealed:",
            f"##nth_root({random_int_one}, 3) emerged as the key to the mystery.",
            f"In the symphony of numbers, the geometric mean of the list whispered its harmony:",
            f"##geometric_mean({random_list}) shared its hidden melody with the world.",
            f"A lingering question emerged: Was {random_int_one} a power of two?",
            f"The answer appeared: ##is_power_of_two({random_int_one}).",
            f"Binary whispers echoed as {random_int_one} transformed into binary code:",
            f"##decimal_to_binary({random_int_one}) decoded the binary enigma.",
            f"Then, in a twist of magic, binary reverted to its original form:",
            f"##binary_to_decimal(##decimal_to_binary({random_int_one})) unveiled the essence.",
            f"The magic of symmetry revealed that {random_int_one} was a palindrome:",
            f"##is_palindrome({random_int_one}) confirmed its symmetrical nature.",
            f"The saga continued with the digits of {random_int_two}, unraveling their combined story:",
            f"##sum_of_digits({random_int_two}) laid bare the power within their union.",
            f"In the realm of triangles, with sides {random_int_one} and {random_int_two},",
            f"the elusive hypotenuse emerged: ##hypotenuse({random_int_one}, {random_int_two}).",
            f"And so, the story of numbers, calculations, and enigmas reached its conclusion,",
            f"leaving behind a legacy of mathematical wonder and a never-ending pursuit of knowledge.",
        ],
        [
            f"Venture into a realm where numbers weave tales of wonder, as a circle emerges with its mysterious radius of {random_float}. Through the incantation of ##circle_area({random_float}), we unveil its enigmatic area, a puzzle piece in the grand numerical tapestry.",
            f"In the mathematical masquerade, {random_int_one} participants step forth from a realm of {random_int_two}, orchestrating their sequence through the dance of permutations via ##permutation({random_int_two}, {random_int_one}). Their arrangement forms an elegant equation that captivates the imagination.",
            f"In the symphony of numbers, {random_int_two} harmonious notes are plucked from a symposium of {random_int_three}. Their fusion, guided by the enchantment ##combination({random_int_three}, {random_int_two}), resonates like a melodic chord, harmonizing unity and diversity.",
            f"A transformation, akin to destiny's flip, is embarked upon. The number {random_float} submits to the enigma of ##invert_number({random_float}), revealing a mirrored dimension, as numbers themselves whisper secrets of symmetry.",
            f"Embarking into the integer realm, {random_float} transforms, revealing its integer core through the invocation of ##float_to_int({random_float}). This transition mirrors the intricate dance between continuous and discrete worlds.",
            f"The integer {random_int_three} embarks on a metamorphosis, relinquishing its integer mantle for a floating existence through the enchantment of ##int_to_float({random_int_three}). A transformation that mirrors the fluidity of mathematical concepts.",
            f"From the canvas of mathematical sequences, a geometric series arises, commencing with {random_float}, embracing a recurring motif of {random_float}, and culminating in a crescendo of {random_int_one} iterations, as revealed by ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"A sigmoid curve, a bridge between extremes, cradles the number {random_float}, culminating in its transformation through the spell ##sigmoid({random_float}). A revelation that mirrors the profound journey from chaos to equilibrium.",
            f"Two vectors, symbolized by {random_list} and {random_list}, engage in a dance of resonance. Their connection, measured by the cosine similarity, unfolds as ##cosine_similarity(eval({random_list}), eval({random_list})), an ode to their harmonious alignment.",
            f"Euler's totient function, an enigmatic oracle of numbers, beckons, unfurling the secrets of {random_int_four}. Its chant, ##euler_totient({random_int_four}), reveals hidden patterns as numbers whisper their tales of co-prime dance.",
            f"As our odyssey through the numerical realm nears its conclusion, the echoes of equations and calculations linger, leaving behind a sense of wonder and reverence for the boundless world of mathematics.",
        ],
        [
            f"Amidst the universe of mathematical wonders, a vector emerged, its elements echoing the harmony of nature: {random_list}.",
            f"Revealing its essence, it shared a length of ##length({random_list}). Its L1 norm, decoded through ##l1_norm({random_list}), coexisted with the L2 norm, ##l2_norm({random_list}), painting a vivid portrait.",
            f"As the saga unfolded, four integers graced the scene: {random_int_one}, {random_int_two}, {random_int_three}, and {random_int_four}.",
            f"The symphony of numbers resonated in the sum of the first two integers, unveiling ##sum([{random_int_one}, {random_int_two}]), while the grand ensemble of all four presented ##sum([{random_int_one}, {random_int_two}, {random_int_three}, {random_int_four}]).",
            f"Exploring further, the quest for an average united {random_int_one}, {random_int_two}, and {random_int_three}. The outcome unfolded as ##average([{random_int_one}, {random_int_two}, {random_int_three}]).",
            f"Amidst the numerical realm, a floating point number, {random_float}, emerged, its presence weaving unpredictability into the narrative.",
            f"Amidst contemplations of truth, the value of truth revealed itself as {random_bool}.",
            f"From the depths of possibility, the enigmatic π emerged, bearing its mathematical legacy: ##get_pi().",
            f"Likewise, the mysterious constant e cast its allure: ##get_e().",
            f"In a symphony of exploration, two vectors, embodying the elements {random_list} and {random_list}, embarked on a shared voyage to unveil their dot product.",
            f"After intricate calculations, their journey culminated in the revelation of the dot product as ##calculate_dot_product({random_list}, {random_list}).",
            f"A twist in the tale unfolded as it was discovered that 'Racecar' remained unaltered even through the mirror of reversal: ##check_same_string('racecar', ##reverse_string('racecar')).",
            f"Within the enchanting tapestry of mathematics, numbers held the key to curiosity and awe, inviting all to decipher their cryptic messages.",
        ],
        [
            f"In the mystical domain of Numerosia, two intrepid explorers, {random_list[0]} and {random_list[1]}, embarked on a grand mathematical quest.",
            f"Driven by their boundless curiosity, {random_list[0]} stumbled upon the enigmatic potential hidden within the square of the sum of two numbers.",
            f"As their revelation unfolded, a formula materialized: ({random_int_one}) plus ({random_int_two}) whole square equals ##a_plus_b_whole_square({random_int_one},{random_int_two}).",
            f"The formula revealed its elegance when expanded: ({random_int_one} squared) plus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared). This intricate symphony of numbers resulted in ##a_squared_plus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"On a parallel journey, {random_list[1]} unearthed another cryptic enigma. The square of the difference between two numbers, resonating with the power of four times their product, unveiled its mysteries.",
            f"The enigmatic equation unfurled: ({random_int_two} minus {random_int_three}) whole squared plus (4 times {random_int_two} times {random_int_three}). This riddle unraveled as ##a_minus_b_whole_squared_plus_4ab({random_int_two},{random_int_three}).",
            f"As their expedition carried on, they encountered the essence of simplicity within complexity. The square of the difference between two numbers, distilled to its purest form:",
            f"({random_int_one} minus {random_int_four}) whole squared, guarded its secret within its elegant simplicity. This revelation transformed into ##a_minus_b_whole_squared({random_int_one},{random_int_four}).",
            f"Venturing deeper, they uncovered the captivating interplay of squares and differences, intricately woven in an elegant dance:",
            f"The difference between the squares of {random_int_one} and {random_int_two}, a symphony of numbers orchestrated through ({random_int_one} squared) minus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared). This mathematical ballet led them to ##a_squared_minus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"Yet, their journey remained incomplete without an encounter with the square of the sum of two numbers, releasing the burden of four times their dance:",
            f"({random_int_two} plus {random_int_three}) whole squared, a tale of numbers entwined in harmony and divergence, unfurling as ##a_plus_b_whole_squared_minus_4ab({random_int_two},{random_int_three}).",
            f"In the vast tapestry of Numerosia, they uncovered a gem of simplicity amid complexity, the heart of their expedition encapsulated:",
            f"The sum of the squares of {random_int_two} and {random_int_three}, a harmonious blend in ({random_int_two} squared) plus ({random_int_three} squared), revealing the essence of ##a_squared_plus_b_squared({random_int_two},{random_int_three}).",
            f"Their odyssey through Numerosia continued, a symphony of exploration driven by their unwavering passion for numbers and the graceful choreography of calculations.",
        ],
    ]

    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator

    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_nine_example_paragraph(),
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
        get_batch_nine_example_paragraph(),
        1,
    )
    sample = Utility.create_sample_from_example(
        next_token_example, PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
