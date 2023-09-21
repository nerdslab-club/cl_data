import random

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def get_batch_eight_example_paragraph():
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
            f"In the vibrant realm of Numerosia, where mathematical wonders held the key to unlocking extraordinary powers, two daring adventurers, Lily and Max, embarked on an epic quest to harness the mystique of numbers.",
            f"Lily, a scholar with an insatiable curiosity, chose to begin her journey by unraveling the enigma of negative numbers. Her calculation prowess uncovered the hidden truth behind -2 times {random_int_one} times {random_int_two}, yielding the result: ##negative_2ab({random_int_one}, {random_int_two}).",
            f"Meanwhile, Max, a fearless explorer of positivity, embarked on a parallel odyssey. He dived into the realm of positivity, wielding the mathematical forces to conquer 2 times {random_int_three} times {random_int_four}, unveiling: ##positive_2ab({random_int_three}, {random_int_four}).",
            f"Lily's path meandered through the intriguing landscape of quadratic equations. She ventured to simplify the enigmatic expression {random_int_one}x + ({random_int_two}x + {random_int_three}) into: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
            f"Meanwhile, Max was drawn to the symphony of polynomials. He orchestrated the expression {random_int_four}x^2 + {random_int_two}x + {random_int_three}x, with x = {random_int_one}, to reveal its harmonious essence: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
            f"As their journey unfolded, Lily and Max united their strengths to unravel the enchanting lore of cubes. The fusion of cubes, embodying the essence of {random_int_two} and {random_int_three}, unfolded its ancient secrets: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
            f"Undeterred by challenges, they pressed forward, encountering a profound cube conundrum. They harnessed the cube of the sum of {random_int_one} and {random_int_four}, meticulously subtracting thrice their cosmic union, revealing: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
            f"A harmonious synergy of intellect brought them to the realm of expressive expansions. The ethereal incantation of ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2, bore a mystic inscription: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
            f"Their journey then unfolded into the intricate tapestry of cube disparities. The enigma unfurled, laying bare the difference between the sacred cube of {random_int_one} and the elusive cube of {random_int_four}: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
            f"As twilight embraced Numerosia, Lily and Max stood before the pinnacle of their quest – a transcendental cube challenge. Their insight harmonized with cosmic melodies, revealing the cube of the difference between {random_int_two} and {random_int_three}, blessed by the trinity of unity, emerging as: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
            f"In the end, Lily and Max beheld the enchantment of mathematical exploration, realizing that in the realm of Numerosia, the magic of numbers held the promise of boundless discovery and awe-inspiring wisdom.",
            f"Their legacy echoed through time, inspiring generations to venture into the realm of numbers, where every equation was a portal to uncover the secrets of the universe itself."
        ],
        [
            f"Once in the land of Numerica, a young scholar named Sophia embarked on a journey through the mathematical tapestry.",
            f"Sophia's odyssey commenced with the art of addition, blending {random_int_one} and {random_int_two} into an exquisite union through ##addition({random_int_one},{random_int_two}).",
            f"As the sun dipped behind the horizon, Sophia found herself entwined in the dance of subtraction. The intricate choreography between {random_int_two} and {random_int_three} unfolded through ##subtraction({random_int_two},{random_int_three}).",
            f"Guided by the stars, Sophia's spirit resonated with the symphony of multiplication. She orchestrated the cosmos to unveil the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
            f"Like a dawn of revelation, Sophia embarked on the path of division. With grace, she uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
            f"Sophia's inquisitive mind led her to the cosmic dance of exponents. She raised {random_int_three} to the power of {random_int_four}, unraveling the universe's mysteries through ##exponentiation({random_int_three},{random_int_four}).",
            f"Beneath the shimmering moonlight, Sophia's heart stirred with curiosity for the mystic realm of square roots. She whispered the incantation, unveiling the secrets of {random_int_four}'s square root through ##square_root({random_int_four}).",
            f"As the first rays of sunlight painted the sky, Sophia faced the puzzle of floor division. With determination, she deciphered the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
            f"In the cosmic symphony of remainders, Sophia uncovered the hidden rhythm. The dance between {random_int_three} and {random_int_one} was unveiled through ##modulus({random_int_three},{random_int_one}).",
            f"Inscribed in the stars were the secrets of logarithms. Sophia contemplated the harmony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
            f"Embracing the cosmos, Sophia resonated with the celestial sine wave. With a profound connection to the universe, she unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        ],
        [
            f"Step into Arctopia, a realm where numbers orchestrate symphonies of discovery. Amidst this vibrant land, inhabited by diverse individuals like the digits themselves ({random_list}), the magic of mathematics flourishes.",
            f"An auspicious day beckoned a mathematician to embark on a quest, armed with an enigma: an angle, {random_float}. This angle became the key unlocking the gateway to the realm of trigonometry, where the beguiling dance of cosine awaited.",
            f"From the celestial canvas emerged the very essence of the unknown: the cosine of {random_float} radians, whispered by the cosmos itself: ##cosine({random_float}). The path of the mathematician now led to the revelation of its tangent.",
            f"The whisper of angles guided the mathematician to unravel the enigmatic tangent of ##arccosine({random_float}). This revelation held not merely a numerical value, but a profound insight etched within its mathematical essence.",
            f"Elsewhere in Arctopia, another soul was entranced by hyperbolic mysteries. Their fascination centered around the hyperbolic sine of {random_int_one}, a formula echoing through the corridors of time.",
            f"As twilight brushed the sky with hues of wonder, young minds converged to decode the riddles of logarithms. Among them, the base-10 logarithm of {random_int_two} revealed patterns transcending the mundane.",
            f"In the midst of this assembly, a prodigious child contemplated the enigma of the cube root of ##hyperbolic_tangent({random_int_three}). A question resonating with the essence of numbers and the boundless realm of possibilities.",
            f"Amid contemplation, a sage, guardian of ancient wisdom, pondered the profound union of numbers and angles: ##logarithm_base_2({random_int_four}) raised to the celestial power of ##arcsine({random_float}).",
            f"As destiny wove its intricate threads, the two mathematicians converged, blending their insights to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
            f"After an intricate choreography of calculations, the answer materialized: {random_int_two + random_int_four}. Arctopia rejoiced, a grand celebration of intellect and discovery. And thus, the legacy of Arctopia's mathematical marvels continued to inspire."
        ],
        [
            f"In the mesmerizing realm of Numerion, where numbers held the power to weave destinies, a spirited young mathematician named Mia embarked on a transformative journey.",
            f"Bearing an angle of {random_int_one} degrees, Mia embarked on an odyssey to translate it into the mystical tongue of radians. With the sacred incantation degrees_to_radians, the transformation was revealed: ##degrees_to_radians({random_int_one}).",
            f"Her path led her to an ancient door protected by the guardians of greatest common divisor. By invoking the spirits of {random_int_two} and {random_int_three}, Mia unlocked the door, unveiling its secrets: ##gcd({random_int_two}, {random_int_three}).",
            f"Continuing her voyage, Mia uncovered the ancient scrolls of least common multiples, discovering the hidden connections between {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
            f"In the heart of the enchanted Forest of Numbers, Mia encountered an ancient tree that stood as a testament to time. Through the magic of isqrt, she discerned the tree's age, finding it to be ##isqrt({random_int_three}).",
            f"As twilight painted Numerion with hues of amber and indigo, Mia harnessed the arcane powers of congruence. By invoking the pow_mod enchantment, she raised {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, revealing the hidden truth: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
            f"In a realm where time flowed like a river, Mia navigated its currents using the spells of ceil, floor, and round. The river's surface reflected the profound difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
            f"As Mia's journey unfolded, she realized that each mathematical function was a key to unlocking a new chamber of insight. Armed with this wisdom, Mia returned to Numerion, sharing her tale to inspire others to embark on their own quests of numerical discovery.",
        ],
        [
            f"Amidst a world where numbers held secrets like stars in the night sky, a quest was undertaken by a curious mathematician.",
            f"In their pursuit of understanding, they embarked on a journey to unravel the mysteries surrounding {random_int_one}, {random_int_two}, and {random_int_three}.",
            f"Their voyage commenced with the enigma of the greatest value between {random_float} and {random_int_one}.",
            f"After profound contemplation, they unveiled the answer: ##greatest_value({random_float}, {random_int_one}).",
            f"Yet, the allure of numbers beckoned further. Their focus turned to {random_list}, an ensemble of cryptic numbers.",
            f"The mathematician uncovered the hidden narrative within, illuminating the elusive product: ##product({random_list}).",
            f"Fueled by curiosity, they delved into the realm of factorials, revealing the enchantment of {random_int_one}!: ##factorial({random_int_one}).",
            f"However, another enigma awaited—the essence of {random_int_two}. Was it a prime number? The revelation materialized as ##is_prime({random_int_two}).",
            f"Undaunted, they embarked on the age-old quest for prime factors, unearthing the story of {random_int_three}: ##prime_factors({random_int_three}).",
            f"In their journey, they stumbled upon {random_int_four}, a number holding a secret—it was a perfect square: ##is_perfect_square({random_int_four}).",
            f"Continuing their odyssey, they unveiled the hidden truth of {random_int_three}, a concealed perfect cube: ##is_perfect_cube({random_int_three}).",
            f"With a heart ignited by numbers, the mathematician returned to {random_list}, deciphering their collective story through the prism of the mean: ##mean({random_list}).",
            f"Yet, one final enigma lingered—the elusive median, the rhythmic heartbeat of the numbers: ##median({random_list}).",
            f"And thus, the mathematician's epic journey through the realm of numbers continued, unveiling the intricate tapestry woven by the language of mathematics."
        ],
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
        ],
        [
            f"Step into a realm where numbers hold secrets and equations reveal tales,",
            f"unveiling a cryptic array of numbers: {random_list}.",
            f"From this array, the mightiest number emerged: ##max_value({random_list}).",
            f"Yet, the most unassuming number stepped forward: ##min_value({random_list}).",
            f"Amidst this domain of numbers, a lone integer took the stage:",
            f"{random_int_one}, an enigmatic figure with untold significance.",
            f"Soon after, another integer made its appearance, identified as",
            f"{random_int_two}, the outcome of {random_int_one} merging with another concealed integer.",
            f"As the plot unfolded, another integer emerged:",
            f"{random_int_three}, the result of {random_int_two} fusing with yet another mysterious value.",
            f"But this tale delved beyond mere numbers; a random float,",
            f"{random_float}, made a brief but impactful appearance, invoking curiosity.",
            f"Through mathematical magic, the cube root of {random_int_one} was unveiled:",
            f"##nth_root({random_int_one}, 3) materialized as the key to the puzzle.",
            f"In the symphony of numbers, the geometric mean of the list whispered its melody:",
            f"##geometric_mean({random_list}) bestowed its concealed harmony upon the narrative.",
            f"A lingering question emerged: Was {random_int_one} a power of two?",
            f"The answer surfaced: ##is_power_of_two({random_int_one}).",
            f"Binary whispers danced as {random_int_one} transformed into binary code:",
            f"##decimal_to_binary({random_int_one}) unraveled the binary enigma.",
            f"Then, in a twist of enchantment, binary transformed back to its primal form:",
            f"##binary_to_decimal(##decimal_to_binary({random_int_one})) unveiled the underlying truth.",
            f"The magic of symmetry unveiled {random_int_one} as a palindrome:",
            f"##is_palindrome({random_int_one}) affirmed its symmetrical nature.",
            f"The tale continued with the digits of {random_int_two}, revealing their collective secret:",
            f"##sum_of_digits({random_int_two}) divulged the sum of these constituent digits.",
            f"In the realm of triangles, with sides {random_int_one} and {random_int_two},",
            f"the enigmatic hypotenuse emerged: ##hypotenuse({random_int_one}, {random_int_two}).",
            f"And so, the chronicle of numbers, calculations, and enigmas drew to its final chapter,",
            f"leaving behind a legacy of mathematical marvels and an eternal journey of exploration."
        ],
        [
            f"Embark on a journey through the realms of numbers, where a circle unfurls with a mysterious radius of {random_float}. Unlocking its enigma, we delve into its area through the incantation of ##circle_area({random_float}), revealing its arcane magnitude.",
            f"In the grand mathematical masquerade, {random_int_one} individuals step forth from a realm of {random_int_two}, their sequence orchestrated by the dance of permutations via ##permutation({random_int_two}, {random_int_one}). An arrangement that beckons awe and fascination.",
            f"As the symphony of mathematics continues, {random_int_two} harmonious notes are chosen from a symposium of {random_int_three}. Their harmonization, guided by the spell ##combination({random_int_three}, {random_int_two}), produces a melody of unity and diversity.",
            f"A transformation, akin to a mystical riddle, is undertaken. The number {random_float} is subjected to the cryptic incantation of ##invert_number({random_float}), revealing its hidden reflection, a glimpse into the duality of numbers.",
            f"Venturing into the realm of integers, {random_float} undergoes a metamorphosis, revealing its integer essence through the spell ##float_to_int({random_float}). A transition that resonates with the symbiosis of continuous and discrete.",
            f"The integer {random_int_three}, once confined to the world of integers, takes on a new ethereal form as a float through the enchantment of ##int_to_float({random_int_three}). A transformation that mirrors the fluidity of mathematical expressions.",
            f"From the tapestry of mathematical sequences emerges a geometric series, commencing with {random_float}, guided by the recurring theme of {random_float}, and culminating in a crescendo of {random_int_one} iterations. The chronicle unfolds through ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"A sigmoid curve, a harbinger of transformation, embraces the number {random_float}, unveiling its value through the incantation of ##sigmoid({random_float}). A revelation that echoes the journey from obscurity to revelation.",
            f"Two vectors, a dance of congruence between {random_list} and {random_list}, unfold their affinity. The measure of their harmony, the cosine similarity, emerges as ##cosine_similarity(eval({random_list}), eval({random_list})), an ode to their mathematical alignment.",
            f"The enigmatic Euler's totient function beckons, an oracle of numbers. Through its invocation, the essence of {random_int_four} is unveiled, its hidden patterns whispered through the conjuring of ##euler_totient({random_int_four}).",
            f"As our journey through the tapestry of mathematics nears its conclusion, the echoes of equations and calculations resonate, leaving us with an enduring sense of awe and reverence for the world of numbers."
        ],
        [
            f"Once within the realm of mathematical enigmas, a vector emerged, its elements as diverse as the cosmos: {random_list}.",
            f"Whispering secrets of its existence, it revealed a length of ##length({random_list}). Its L1 norm, a mystery untangled by ##l1_norm({random_list}), coexisted with its L2 norm, ##l2_norm({random_list}).",
            f"Meanwhile, four integers appeared on the horizon: {random_int_one}, {random_int_two}, {random_int_three}, and {random_int_four}.",
            f"The sum of the first two integers danced as ##sum([{random_int_one}, {random_int_two}]), while the collective sum of all four was a revelation at ##sum([{random_int_one}, {random_int_two}, {random_int_three}, {random_int_four}]).",
            f"Delving deeper, the pursuit of an average brought together {random_int_one}, {random_int_two}, and {random_int_three}. The outcome was ##average([{random_int_one}, {random_int_two}, {random_int_three}]).",
            f"As the story unfolded, a floating point number, {random_float}, entered the stage, ushering in a touch of serendipity.",
            f"Contemplating truth, it was unveiled that the value of truth was indeed {random_bool}.",
            f"From the veil of possibilities, the mystical π emerged, offering a glimpse into its numerical significance: ##get_pi().",
            f"Similarly, the enigmatic constant e revealed its presence: ##get_e().",
            f"Two vectors, each embodying the elements {random_list} and {random_list}, embarked on a shared quest to unveil their dot product.",
            f"After intricate calculations, their journey revealed the dot product as ##calculate_dot_product({random_list}, {random_list}).",
            f"A twist of logic uncovered that 'Racecar' remained unaltered when subjected to reversal: ##check_same_string('racecar', ##reverse_string('racecar')).",
            f"Within the mesmerizing tapestry of mathematics, numbers ruled with elegance and charm, inviting all to decipher their mysteries."
        ],
        [
            f"In the captivating realm of Mathoria, two inquisitive minds, {random_list[0]} and {random_list[1]}, embarked on a mathematical voyage like no other.",
            f"Fueled by their insatiable curiosity, {random_list[0]} stumbled upon the hidden mysteries within the square of the sum of two numbers.",
            f"As their revelation unfolded, a formula emerged: ({random_int_one}) plus ({random_int_two}) whole square equals ##a_plus_b_whole_square({random_int_one},{random_int_two}).",
            f"The formula revealed its elegance when expanded: ({random_int_one} squared) plus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared). This intricate dance of numbers resulted in ##a_squared_plus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"On a parallel journey, {random_list[1]} unraveled another enigmatic puzzle. The square of the difference between two numbers, resonating with the power of four times their product, unveiled its secrets.",
            f"The enigmatic equation unfurled: ({random_int_two} minus {random_int_three}) whole squared plus (4 times {random_int_two} times {random_int_three}). This mystery unfurled as ##a_minus_b_whole_squared_plus_4ab({random_int_two},{random_int_three}).",
            f"As their expedition continued, they encountered the essence of simplicity within complexity. The square of the difference between two numbers, distilled to its purest form:",
            f"({random_int_one} minus {random_int_four}) whole squared, guarded its secret within its simplicity. This revelation transformed into ##a_minus_b_whole_squared({random_int_one},{random_int_four}).",
            f"Delving deeper, they discovered the captivating interplay of squares and differences, intricately woven in an elegant waltz:",
            f"The difference between the squares of {random_int_one} and {random_int_two}, a symphony of numbers orchestrated through ({random_int_one} squared) minus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared). This mathematical ballet led them to ##a_squared_minus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"Yet, their journey remained incomplete without an encounter with the square of the sum of two numbers, shedding the weight of four times their dance:",
            f"({random_int_two} plus {random_int_three}) whole squared, a tale of numbers in harmony and divergence, unfurling as ##a_plus_b_whole_squared_minus_4ab({random_int_two},{random_int_three}).",
            f"In the expansive tapestry of Mathoria, they unearthed a gem of simplicity amid complexity, the heart of their expedition encapsulated:",
            f"The sum of the squares of {random_int_two} and {random_int_three}, a harmonious duet in ({random_int_two} squared) plus ({random_int_three} squared), revealing the essence of ##a_squared_plus_b_squared({random_int_two},{random_int_three}).",
            "Their odyssey through Mathoria continued, a symphony of exploration driven by their unwavering passion for numbers and the graceful choreography of calculations.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator

    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_eight_example_paragraph(),
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
        get_batch_eight_example_paragraph(),
        1,
    )
    sample = Utility.create_sample_from_example(
        next_token_example, PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
