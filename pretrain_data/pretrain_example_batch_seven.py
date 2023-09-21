import random

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def get_batch_seven_example_paragraph():
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
            f"In the realm of Numarctica, where numbers held mystical powers, two valiant scholars, Ava and Leo, embarked on a quest to decipher the ancient scrolls of mathematical magic.",
            f"Ava, a curious enchantress, decided to first explore the enigmatic realm of negative numbers. Her incantation revealed the hidden truth behind -2 times {random_int_one} times {random_int_two}, conjuring the result: ##negative_2ab({random_int_one}, {random_int_two}).",
            f"Meanwhile, Leo, a sage of positivity, sought illumination from positive forces. Delving into the cosmic arithmetic, he harnessed 2 times {random_int_three} times {random_int_four}, revealing: ##positive_2ab({random_int_three}, {random_int_four}).",
            f"Ava's path then led her to unravel the arcane secrets of quadratic formations. She gazed upon the equation {random_int_one}x + ({random_int_two}x + {random_int_three}), weaving her powers to simplify it to: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
            f"Yet, it was in the constellation of polynomials that Leo sought inspiration. Guided by the celestial muse, he manifested the essence of {random_int_one}x^2 + {random_int_two}x + {random_int_three}x, with x = {random_int_one}, uncovering: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
            f"As their journey continued, Ava and Leo united their energies to fathom the mystical realm of cubes. The combined essence of cubes, embracing {random_int_two} and {random_int_three}, revealed its true nature: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
            f"Undeterred by challenges, they ventured deeper into mathematical mysteries. Their pursuit led them to a profound cube enigma, where the cube of the sum of {random_int_one} and {random_int_four}, minus thrice their ethereal union, transformed into: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
            f"As Ava and Leo traversed through the labyrinthine expressions, they stumbled upon the eldritch expansion of ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2, revealing an intricate sigil: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
            f"Yet, their saga held a transcendental twist - a tale of cube disparities. The riddle unraveled, exposing the gap between the sacred cube of {random_int_one} and the mystic cube of {random_int_four}: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
            f"At the pinnacle of their journey, Ava and Leo encountered the zenith of cube conundrums. Their insight resonated with the cosmos, deciphering the cube of the difference between {random_int_two} and {random_int_three}, enriched by threefold cosmic fusion, ultimately emerging as: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
            f"With newfound wisdom and a sense of unity, Ava and Leo realized that the sacred art of mathematics was a universal language that transcended time and space, connecting all realms in Numarctica.",
            f"Their legacy lived on, reminding future generations that the quest for knowledge was a voyage of endless discovery, forever intertwined with the captivating mysteries of numbers."
        ],
        [
            f"Amidst the pages of an ancient tome, the story of a young mathemagician named Maya unfolded.",
            f"Maya's journey through the realm of numbers began with the art of addition. She delicately added {random_int_one} and {random_int_two}, conjuring the answer through ##addition({random_int_one},{random_int_two}).",
            f"In her quest for mathematical enlightenment, Maya encountered the enigma of subtraction. The dance between {random_int_two} and {random_int_three} was revealed through ##subtraction({random_int_two},{random_int_three}).",
            f"Guided by the celestial patterns, Maya's mind ignited with the allure of multiplication. She orchestrated the universe's symphony to reveal the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
            f"As dawn kissed the horizon, Maya ventured into the realm of division. With grace, she uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
            f"Maya's insatiable curiosity led her to the cosmic dance of exponents. She raised {random_int_three} to the power of {random_int_four}, unraveling the universe's mysteries through ##exponentiation({random_int_three},{random_int_four}).",
            f"Beneath the shimmering moonlight, Maya's gaze was drawn to the mystic realm of square roots. She whispered the enchanting incantation, unveiling the secrets of {random_int_four}'s square root through ##square_root({random_int_four}).",
            f"As the first rays of sunlight emerged, Maya faced the puzzle of floor division. With determination, she decoded the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
            f"In the cosmic tapestry of remainders, Maya uncovered the hidden rhythm. The dance between {random_int_three} and {random_int_one} was unveiled through ##modulus({random_int_three},{random_int_one}).",
            f"Inscribed in the fabric of the universe were the secrets of logarithms. Maya contemplated the symphony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
            f"Nestled in the embrace of cosmic harmony, Maya embraced the celestial sine wave. With a profound connection to the cosmos, she unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        ],
        [
            f"Step into Arctopia, a realm where numbers whisper secrets and equations weave tales. Amidst this vibrant land, inhabited by individuals as diverse as the digits themselves ({random_list}), the magic of mathematics thrives.",
            f"On a day painted with curiosity, a mathematician set forth on a quest with an angle, a mystical key: {random_float}. This key unlocked the gateway to trigonometry, where the enchanting choreography of cosine awaited.",
            f"From the celestial stage emerged the essence of the unknown: the cosine of {random_float} radians, whispered by the universe itself: ##cosine({random_float}). The mathematician's journey now led to the discovery of its tangent.",
            f"The symphony of angles guided the mathematician to reveal the enigmatic tangent of ##arccosine({random_float}). This revelation held not only a numerical value but a profound insight within its mathematical embrace.",
            f"Elsewhere, another soul in Arctopia was captivated by hyperbolic enigmas. Their fascination revolved around the hyperbolic sine of {random_int_one}, a formula that seemed to echo across time.",
            f"As twilight painted the sky with shades of wonder, young minds converged to decipher the riddles of logarithms. Among them, the base-10 logarithm of {random_int_two} unveiled patterns transcending the ordinary.",
            f"Within this assembly, a prodigious child contemplated the enigma of the cube root of ##hyperbolic_tangent({random_int_three}). A question resonating with the essence of numbers and the vast realm of possibilities.",
            f"Amid contemplation, a sage, a custodian of ancient wisdom, pondered the profound synergy of numbers and angles: ##logarithm_base_2({random_int_four}) elevated to the ethereal power of ##arcsine({random_float}).",
            f"As destiny wove its threads, the two mathematicians united, their insights converging to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
            f"After a symphony of calculations, the answer materialized: {random_int_two + random_int_four}. Arctopia rejoiced, a grand celebration of intellect and discovery. And thus, the legacy of Arctopia's mathematical marvels illuminated the path forward."
        ],
        [
            f"Within the realm of Numaria, where numbers held the key to all mysteries, a young mathematician named Eli set forth on a journey of discovery.",
            f"With {random_int_one} degrees in hand, Eli embarked on a quest to transform them into the esoteric language of radians. Through the power of degrees_to_radians, the transformation was ##degrees_to_radians({random_int_one}).",
            f"Venturing deeper into the land, Eli stumbled upon an ancient doorway guarded by the sentinels of greatest common divisor. The sacred numbers {random_int_two} and {random_int_three} revealed the path: ##gcd({random_int_two}, {random_int_three}).",
            f"Continuing the expedition, Eli deciphered the scrolls of least common multiples, uncovering the connection between {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
            f"Guided by the stars, Eli encountered a mystical tree deep within the Enchanted Forest of Numbers. The tree's age was unveiled through the power of isqrt, and the age was ##isqrt({random_int_three}).",
            f"As the sun dipped below the horizon, bathing Numaria in a warm glow, Eli harnessed the magic of congruence. By invoking the pow_mod enchantment, {random_int_two} was raised to the power of {random_int_one}, modulo {random_int_four}, revealing the secret: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
            f"In a realm where time flowed like a river, Eli rode its currents with the spells of ceil, floor, and round. The river's surface reflected the profound difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
            f"As Eli's odyssey neared its end, the realization dawned that each mathematical function was a key to unlock a new chamber of understanding. Armed with this wisdom, Eli returned to Numaria to share their journey, inspiring others to embark on their own mathematical quests.",
        ],
        [
            f"Legend whispers of a land where numbers held ancient truths, and in that land, a curious mathematician roamed.",
            f"In their pursuit of wisdom, they unveiled the enigmas surrounding {random_int_one}, {random_int_two}, and {random_int_three}.",
            f"Their journey unfolded with the mystery of the greatest value between {random_float} and {random_int_one}.",
            f"After deep contemplation, they revealed the answer: ##greatest_value({random_float}, {random_int_one}).",
            f"But the allure of numbers persisted. Their gaze turned to {random_list}, a collection of mystical numbers.",
            f"The mathematician unearthed the cryptic tale within, exposing the elusive product: ##product({random_list}).",
            f"Driven by curiosity, they ventured into the realm of factorials, unravelling the enchantment of {random_int_one}!: ##factorial({random_int_one}).",
            f"Yet, another enigma beckoned—the nature of {random_int_two}. Was it a prime number? The revelation emerged as ##is_prime({random_int_two}).",
            f"Undeterred, they embarked on the age-old quest of prime factors, unearthing the saga of {random_int_three}: ##prime_factors({random_int_three}).",
            f"In their journey, they stumbled upon {random_int_four}, a number with a secret—it was a perfect square: ##is_perfect_square({random_int_four}).",
            f"Their odyssey continued, revealing the hidden truth of {random_int_three}, a concealed perfect cube: ##is_perfect_cube({random_int_three}).",
            f"With a heart aflame with numbers, the mathematician returned to {random_list}, decoding their collective story through the prism of the mean: ##mean({random_list}).",
            f"Yet, a final enigma lingered—the elusive median, the heartbeat of the numbers: ##median({random_list}).",
            f"And so, the mathematician's epic journey through the realm of numbers endured, unravelling the intricate tapestry woven by the language of mathematics."
        ],
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
        ],
        [
            f"Step into a world where numbers weave stories and equations unveil secrets,",
            f"revealing an enigmatic list of numbers: {random_list}.",
            f"From this array, the mightiest number arose: ##max_value({random_list}).",
            f"Yet, the most unpretentious number also claimed its place: ##min_value({random_list}).",
            f"Within this numerical realm, a solitary integer emerged:",
            f"{random_int_one}, a figure imbued with mystique and allure.",
            f"In the unfolding drama, a new integer took the spotlight, known as",
            f"{random_int_two}, the result of {random_int_one} combining with another enigmatic integer.",
            f"The narrative continued to unfold, ushering forth another integer:",
            f"{random_int_three}, born from the union of {random_int_two} and a hidden number.",
            f"But numbers alone did not hold sway; a random float,",
            f"{random_float}, made a fleeting cameo, sparking curiosity.",
            f"With mathematical incantations, the cube root of {random_int_one} was unveiled:",
            f"##nth_root({random_int_one}, 3) emerged as the enigma's solution.",
            f"Amidst the symphony of numbers, the geometric mean of the list whispered its melody:",
            f"##geometric_mean({random_list}) bestowed its hidden harmony.",
            f"Yet, a question lingered: Was {random_int_one} a power of two?",
            f"The answer emerged: ##is_power_of_two({random_int_one}).",
            f"Binary whispers danced, as {random_int_one} transformed into binary code:",
            f"##decimal_to_binary({random_int_one}) unraveled the binary enigma.",
            f"Then, in a twist of enchantment, binary reverted to its original form:",
            f"##binary_to_decimal(##decimal_to_binary({random_int_one})) unveiled the truth.",
            f"The magic of symmetry unveiled that {random_int_one} was a palindrome:",
            f"##is_palindrome({random_int_one}) confirmed its symmetrical essence.",
            f"The saga progressed with the digits of {random_int_two}, revealing their collective tale:",
            f"##sum_of_digits({random_int_two}) unveiled the power within those digits.",
            f"In the realm of triangles, with sides {random_int_one} and {random_int_two},",
            f"the elusive hypotenuse emerged: ##hypotenuse({random_int_one}, {random_int_two}).",
            f"And thus, the chronicle of numbers, calculations, and enigmas reached its finale,",
            f"leaving behind a legacy of mathematical wonder and a perpetual quest for discovery."
        ],
        [
            f"Once upon a numerical odyssey, a circle emerged, its radius {random_float} invoking curiosity. Its hidden area, a calculation away with ##circle_area({random_float}), held the key to unlocking its enigmatic nature.",
            f"In a mathematical masquerade, {random_int_one} participants were chosen from a pool of {random_int_two}, their order meticulously arranged through ##permutation({random_int_two}, {random_int_one}). This sequence of selection formed a mesmerizing mathematical dance.",
            f"A symphony of numbers unfolded, as {random_int_two} harmonious notes were selected from {random_int_three}, their union orchestrated by ##combination({random_int_three}, {random_int_two}). This harmonic blend resonated with the essence of mathematical unity.",
            f"Amidst the numerical realm, a daring transformation occurred. The number {random_float}, when subjected to ##invert_number({random_float}), revealed its shadowy counterpart, akin to a reflection in the mathematical looking glass.",
            f"Venturing into the world of integers, {random_float} unveiled its integer alter ego through ##float_to_int({random_float}). This metamorphosis embodied the delicate balance between the continuous and the discrete.",
            f"The integer {random_int_three} underwent a metamorphosis, shedding its integer identity to embrace a new form as a float through ##int_to_float({random_int_three}). This transformation symbolized the fluidity of mathematical expression.",
            f"From the canvas of mathematical sequences arose a geometric series. With an initial note of {random_float}, a recurring motif of {random_float}, and a symphonic progression of {random_int_one} terms, the melody was captured by ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"The sigmoid curve, a mathematical shapeshifter, encountered the number {random_float}, transforming it to a value of ##sigmoid({random_float}). This metamorphosis mirrored the transformative power of mathematical operations.",
            f"Two vectors, embodied as {random_list} and {random_list}, embarked on a dance of similarity. Their connection, measured by the cosine similarity, emerged as ##cosine_similarity(eval({random_list}), eval({random_list})), a testament to their mathematical affinity.",
            f"The enigmatic Euler's totient function beckoned, unveiling secrets concealed within {random_int_four}. Its revelation, ##euler_totient({random_int_four}), illuminated the intricate dance of numbers in their prime.",
            f"As the mathematical narrative neared its conclusion, the resonance of numbers and equations continued to echo, leaving behind a sense of wonder and appreciation for the mathematical world."
        ],
        [
            f"Once in the realm of mathematical marvels, a vector emerged, its elements shimmering with numbers: {random_list}.",
            f"Exploring its identity, it uncovered a length of ##length({random_list}). Its L1 norm, ##l1_norm({random_list}), and L2 norm, ##l2_norm({random_list}), added to its mystique.",
            f"Meanwhile, four integers came into existence: {random_int_one}, {random_int_two}, {random_int_three}, and {random_int_four}.",
            f"The sum of the first two integers was ##sum([{random_int_one}, {random_int_two}]), while the collective sum of all four reached ##sum([{random_int_one}, {random_int_two}, {random_int_three}, {random_int_four}]).",
            f"Venturing deeper, an average was sought amidst the integers {random_int_one}, {random_int_two}, and {random_int_three}. The result was ##average([{random_int_one}, {random_int_two}, {random_int_three}]).",
            f"Intrigue grew as a floating point number, {random_float}, appeared, adding a touch of uncertainty.",
            f"Contemplating truth, it was unveiled that the value of truth stood as {random_bool}.",
            f"The mystical π materialized, carrying the weight of its mathematical significance: ##get_pi().",
            f"Similarly, the elusive constant e made its presence known: ##get_e().",
            f"Two vectors, bearing the elements {random_list} and {random_list}, set out on a quest to unveil their dot product.",
            f"After intricate calculations, their journey unveiled the dot product as ##calculate_dot_product({random_list}, {random_list}).",
            f"A twist of logic brought forth the discovery that 'Racecar' remained unaltered when reversed: ##check_same_string('racecar', ##reverse_string('racecar')).",
            f"In the enchanting tapestry of mathematics, numbers reigned supreme, casting a spell of fascination and discovery."
        ],
        [
            f"In the wondrous land of Arithmetica, two intrepid companions, {random_list[0]} and {random_list[1]}, embarked on a thrilling mathematical journey.",
            f"Fueled by their unquenchable thirst for numerical marvels, {random_list[0]} stumbled upon the hidden enchantment within the square of the sum of two numbers.",
            f"As their revelation unfolded, a formula emerged: ({random_int_one}) plus ({random_int_two}) whole square equals ##a_plus_b_whole_square({random_int_one},{random_int_two}).",
            f"The formula unveiled its elegance when expanded: ({random_int_one} squared) plus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared). This intricate dance of numbers resulted in ##a_squared_plus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"On a parallel expedition, {random_list[1]} unraveled another enigmatic puzzle. The square of the difference between two numbers, resonating with the power of four times their product, unveiled its secrets.",
            f"The enigmatic equation unfurled: ({random_int_two} minus {random_int_three}) whole squared plus (4 times {random_int_two} times {random_int_three}). This mystery unfurled as ##a_minus_b_whole_squared_plus_4ab({random_int_two},{random_int_three}).",
            f"As their journey continued, they encountered the essence of simplicity within complexity. The square of the difference between two numbers, distilled to its purest form:",
            f"({random_int_one} minus {random_int_four}) whole squared, guarded its secret within its simplicity. This revelation transformed into ##a_minus_b_whole_squared({random_int_one},{random_int_four}).",
            f"Delving deeper, they discovered the captivating interplay of squares and differences, intricately woven in an elegant waltz:",
            f"The difference between the squares of {random_int_one} and {random_int_two}, a symphony of numbers orchestrated through ({random_int_one} squared) minus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared). This mathematical ballet led them to ##a_squared_minus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"Yet, their journey remained incomplete without an encounter with the square of the sum of two numbers, shedding the weight of four times their dance:",
            f"({random_int_two} plus {random_int_three}) whole squared, a tale of numbers in harmony and divergence, unfurling as ##a_plus_b_whole_squared_minus_4ab({random_int_two},{random_int_three}).",
            f"In the sprawling tapestry of Arithmetica, they unearthed a gem of simplicity amid complexity, the heart of their expedition encapsulated:",
            f"The sum of the squares of {random_int_two} and {random_int_three}, a harmonious duet in ({random_int_two} squared) plus ({random_int_three} squared), revealing the essence of ##a_squared_plus_b_squared({random_int_two},{random_int_three}).",
            f"Their odyssey through Arithmetica endured, a symphony of exploration driven by their unyielding passion for numbers and the graceful choreography of calculations.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator

    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_seven_example_paragraph(),
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
        get_batch_seven_example_paragraph(),
        1,
    )
    sample = Utility.create_sample_from_example(
        next_token_example, PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
