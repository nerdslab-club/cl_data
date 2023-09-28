import random

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def get_batch_four_example_paragraph():
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
            f"In the mystical land of numbers, there lived a curious mathematician named Alice.",
            f"She was known for her prowess in calculations and solving complex problems.",
            f"One day, she stumbled upon a magical equation: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
            f"Excited to unlock its secrets, Alice expanded the equation: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
            f"The result amazed her, as it was equal to ##a_cubed_plus_b_cubed({random_int_one}, {random_int_two})!",
            f"Eager to explore further, Alice encountered the mystical formula: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_two}).",
            f"Meanwhile, the mischievous Cheshire Cat watched as Alice delved deeper into calculations.",
            f"Alice decided to challenge herself with the equation: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_four}).",
            f"This reminded her of the identity ##a_cubed_minus_b_cubed({random_int_two}, {random_int_four}) = ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_four}).",
            f"The Cheshire Cat grinned and said, 'Ah, you've discovered the secrets of mathematics, Alice!'",
            f"Amazed by her journey, Alice realized that numbers held infinite mysteries waiting to be unraveled.",
            f"With a heart full of curiosity, she continued her exploration of the enchanting world of math.",
            f"And so, Alice's adventures in calculations and equations continued, as she embraced the beauty of numbers.",
        ],
        [
            f"Long ago, in a world where numbers danced like stars, lived a young mathematician named Leo.",
            f"Leo's journey began with the symphony of addition. He orchestrated the union of {random_int_one} and {random_int_two}, revealing the harmonious result through ##addition({random_int_one},{random_int_two}).",
            f"As the sun dipped beyond the horizon, Leo stumbled upon the puzzle of subtraction. The dance between {random_int_two} and {random_int_three} was expressed through ##subtraction({random_int_two},{random_int_three}).",
            f"In pursuit of cosmic revelations, Leo turned to the enigmatic dance of multiplication. The universe unveiled the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
            f"Amidst celestial wonders, Leo's thoughts wandered to the essence of division. The universe whispered its secrets as he uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
            f"As Leo gazed at the stars above, he contemplated the power of exponents. He ascended the cosmos by raising {random_int_three} to the power of {random_int_four} through ##exponentiation({random_int_three},{random_int_four}).",
            f"Under the shimmering moonlight, Leo was drawn to the mystery of the square root. The universe shared its secrets as he revealed the square root of {random_int_four} through ##square_root({random_int_four}).",
            f"As dawn painted the sky, Leo encountered the riddle of floor division. He unraveled the enigma, revealing the result of {random_int_two} divided by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
            f"In the labyrinth of cosmic patterns, Leo uncovered the hidden rhythm of remainders. The dance between {random_int_three} and {random_int_one} was unveiled through ##modulus({random_int_three},{random_int_one}).",
            f"The ancient scrolls spoke of the language of logarithms. Leo pondered the symphony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
            f"In the tranquil embrace of the universe, Leo embraced the cosmic sine wave. He harnessed the rhythm of the cosmos, unveiling the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
            f"each calculation, Leo's bond with the cosmos deepened, as he unveiled the universe's secrets through the art of mathematics.",
        ],
        [
            f"Once upon a time, in the realm of Arctopia, a charming town flourished. Its inhabitants, enchanted by the allure of numbers, reveled in their unpredictable dance, as reflected in their diverse population: {random_list}.",
            f"But the heart of Arctopia beat with the curiosity of one individual. Armed with an enigmatic angle, {random_float}, a mathematician embarked on a journey to fathom the mysteries of trigonometry.",
            f"Unveiling the secrets of the cosmos, the mathematician encountered the cosmic dance of the cosine of {random_float} radians: ##cosine({random_float}). Intrigued, they sought the path to its tangent.",
            f"The mathematician's quest led to a profound revelation—revealing the tangent of ##arccosine({random_float}). A truth hidden within the mathematical tapestry of Arctopia was brought to light.",
            f"Meanwhile, on the other side of the town, a different scholar explored the hyperbolic enigmas. The hyperbolic sine of {random_int_one} became the subject of their fascination.",
            f"As twilight painted the sky with hues of amber, young minds converged to decipher the secrets of logarithms. In their pursuit, the base-10 logarithm of {random_int_two} was unraveled, unraveling new horizons.",
            f"Among the curious minds, a prodigious child contemplated the enigma of the cube root of ##hyperbolic_tangent({random_int_three}). A question that resonated with the essence of numbers and possibility.",
            f"In parallel, a venerable sage meditated upon the mysterious power of numbers: What lies within the embrace of ##logarithm_base_2({random_int_four}) when elevated by the whispering winds of ##arcsine({random_float})?",
            f"As destiny would have it, the two scholars converged, uniting their wisdom. Together, they embarked on a voyage to decipher the cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
            f"Upon a crescendo of calculations, the answer materialized: {random_int_two + random_int_four}. The town rejoiced, celebrating the victory of intellect with a grand gala. And thus, the echoes of Arctopia's mathematical marvels resonated for generations to come.",
        ],
        [
            f"In a realm known as Numertopia, where numbers held the secrets of the universe, a curious mathematician named Alex embarked on an exhilarating quest.",
            f"Guided by a sense of wonder, Alex set out to convert {random_int_one} degrees into radians, using the mysterious formula degrees_to_radians: ##degrees_to_radians({random_int_one}).",
            f"On their journey, they discovered a hidden chamber that could only be unlocked with the magical key of greatest common divisor. The numbers {random_int_two} and {random_int_three} were the key, revealing the hidden truth: ##gcd({random_int_two}, {random_int_three}).",
            f"Delving deeper, Alex stumbled upon the ancient codex of least common multiples, and with it, they unveiled the secret codes of {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
            f"In a forest of mathematical wonders, Alex encountered an ancient tree with integer roots. Using the power of isqrt, they unraveled the tree's age, finding it to be ##isqrt({random_int_three}).",
            f"Venturing into the domain of congruence, Alex harnessed the pow_mod incantation. By raising {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, they uncovered a hidden gem: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
            f"As time flowed like a river, Alex navigated its currents using the tools of ceil, floor, and round. The river's surface revealed the mystic reflection of the absolute difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
            f"In the heart of Numertopia, Alex realized that each function was a portal to a new dimension of understanding. These mathematical tools were the keys to unlock the secrets of the universe.",
            f"Carrying the knowledge and wonder of their journey, Alex returned to their fellow mathematicians, sharing the tale that would forever inspire new generations to explore the infinite landscapes of numbers and discovery.",
        ],
        [
            f"Once upon a time, in a land where numbers held great power, lived a curious mathematician.",
            f"This brilliant mind pondered the mysteries of numbers like {random_int_one}, {random_int_two}, and {random_int_three}.",
            f"They wondered about the greatest value between {random_float} and {random_int_one}. After deep contemplation,",
            f"they concluded that the answer was ##greatest_value({random_float}, {random_int_one}).",
            f"But their thirst for knowledge didn't stop there. They turned their attention to {random_list}, a collection of enchanted numbers.",
            f"The mathematician uncovered that the product of these numbers was ##product({random_list}).",
            f"Intrigued by factorials, they delved into the mystery of {random_int_one}! and found it to be ##factorial({random_int_one}).",
            f"They embarked on a journey to unravel the truth about {random_int_two}. Was it truly a prime number?",
            f"The answer was revealed as ##is_prime({random_int_two}).",
            f"However, their quest was not over. They sought the ancient wisdom of prime factors for {random_int_three}, which led to ##prime_factors({random_int_three}).",
            f"Amidst their exploration, they stumbled upon {random_int_four} and realized it was a hidden perfect square: ##is_perfect_square({random_int_four}).",
            f"Their discoveries continued as they unlocked the secret of {random_int_three}, a concealed perfect cube: ##is_perfect_cube({random_int_three}).",
            f"With a heart full of numbers, the mathematician revisited {random_list} and revealed the hidden truths of their mean: ##mean({random_list}).",
            f"Lastly, they sought balance within the numbers, discovering the enigmatic median: ##median({random_list}).",
            f"And so, the mathematician's journey through the realm of numbers continued, uncovering the magic within their mathematical tapestry.",
        ],
        [
            f"In a world where numbers held ancient secrets...",
            f"A fearless voyager stumbled upon an array of enigmatic numbers: {random_list}.",
            f"Whispering the language of order, the traveler summoned: ##ascending_sort({random_list}).",
            f"Among these, an intriguing integer stood tall: {random_int_one}.",
            f"Contemplating its nature, a query emerged: Even or not? The answer echoed: ##is_even({random_int_one}).",
            f"Then, the traveler harnessed its essence, unearthing its square: ##square_int({random_int_one}).",
            f"But beyond the ordinary, a spectral floating number, {random_float}, beckoned.",
            f"Diving into the unknown, they conjured its squared form: ##square({random_float}).",
            f"With newfound courage, they channeled the might of ten: ##power_of_ten({random_float}).",
            f"From shadows, a different integer emerged: {random_int_two}.",
            f"Challenging its essence, the traveler wondered: Odd or even? Illumination came as: ##is_odd({random_int_two}).",
            f"And its absolute truth revealed: ##absolute({random_int_two}).",
            f"Yet destiny weaved another chapter, a ciphered integer: {random_int_three}.",
            f"Deciphering its riddle, the traveler uncovered its cube: ##cube({random_int_three}).",
            f"Unlocking its heart, the cube's core was laid bare: ##cube_root(##cube({random_int_three})).",
            f"Yet the odyssey held yet more marvels! A binary enigma emerged: {random_bool}.",
            f"Reflecting on the realm, they invoked the ReLU incantation for {random_float}: ##relu({random_float}).",
            f"Deeper still, an unforeseen integer materialized: {random_int_four}.",
            f"Drawn by the unknown, they orchestrated a descent: ##descending_sort([{random_int_four}, {random_int_two}, {random_int_one}]).",
            f"Thus, the chronicle unfolded, woven with calculations and epiphanies...",
            f"Amid twists and revelations, the traveler's journey surged, guided by the ancient magic of mathematics.",
        ],
        [
            f"In a land where numbers danced and equations whispered,",
            f"a list of enigmatic numbers materialized: {random_list}.",
            f"From this array, the grandest value emerged: ##max_value({random_list}).",
            f"Yet, the most humble number also surfaced: ##min_value({random_list}).",
            f"Amidst this numerical realm, a solitary integer stepped into the spotlight:",
            f"{random_int_one}, an integer shrouded in mystery and intrigue.",
            f"Soon after, a new integer entered the stage, its identity revealed as",
            f"{random_int_two}, a result of {random_int_one} harmonizing with another enigma.",
            f"The tale continued to unfold, ushering in another integer:",
            f"{random_int_three}, born from the fusion of {random_int_two} and an elusive figure.",
            f"But numbers alone did not rule this realm; a random float,",
            f"{random_float}, made a fleeting appearance, casting a spell of curiosity.",
            f"With mathematical incantations, the cube root of {random_int_one} unveiled itself:",
            f"##nth_root({random_int_one}, 3) emerged as the mystical answer.",
            f"Amidst the symphony of numbers, the geometric mean of the list was whispered:",
            f"##geometric_mean({random_list}) bestowed its hidden wisdom.",
            f"Yet, a question lingered: Was {random_int_one} a power of two?",
            f"The answer was unveiled: ##is_power_of_two({random_int_one}).",
            f"Binary whispers echoed, as {random_int_one} transformed into binary code:",
            f"##decimal_to_binary({random_int_one}) unfurled the binary enigma.",
            f"Then, in a twist of magic, binary reverted to its original form:",
            f"##binary_to_decimal(##decimal_to_binary({random_int_one})) bared the truth.",
            f"The magic of symmetry revealed that {random_int_one} was a palindrome:",
            f"##is_palindrome({random_int_one}) confirmed the symmetrical essence.",
            f"The saga pressed on, as the digits of {random_int_two} shared their secret sum:",
            f"##sum_of_digits({random_int_two}) unveiled the collective digit's tale.",
            f"In the realm of triangles, with sides {random_int_one} and {random_int_two},",
            f"the elusive hypotenuse emerged: ##hypotenuse({random_int_one}, {random_int_two}).",
            f"And thus, the chronicle of numbers, calculations, and enigma draws to a close,",
            f"leaving behind a legacy of mathematical marvels and eternal curiosity.",
        ],
        [
            f"In the heart of a mystical land, there existed a circle with an enigmatic radius of {random_float}. Its arcane area, computed using the formula ##circle_area({random_float}), held ancient secrets.",
            f"A gathering of {random_int_one} chosen individuals emerged, selected from a pool of {random_int_two}. The order of their assembly, calculated through ##permutation({random_int_two}, {random_int_one}), enchanted all who witnessed.",
            f"Amidst the intrigue, {random_int_two} magical elements were handpicked from a collection of {random_int_three}. The fusion of these, harmonized by ##combination({random_int_three}, {random_int_two}), invoked wonder and awe.",
            f"A daring numerical inversion took place, akin to inverting the course of fate. The transformation of {random_float} through ##invert_number({random_float}) revealed hidden truths concealed within the numbers.",
            f"Venturing into the realm of integers, {random_float} unveiled its inner integer self using ##float_to_int({random_float}). This transition mirrored the dual nature of numbers, each a world of its own.",
            f"By invoking the essence of change, the integer {random_int_three} was transmuted into a floating-point existence, becoming a different expression through ##int_to_float({random_int_three}).",
            f"From the harmony of sequences emerged a geometric series. With an inception at {random_float}, a common motif of {random_float}, and a crescendo of {random_int_one} iterations, it whispered its truth via ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"Enter the sigmoid, a curve of revelation. Its magic unfolded as it embraced {random_float}, bringing it to a value of ##sigmoid({random_float}), illuminating transitions from the extremities of existence.",
            f"Two vectors, symbolized by {random_list} and {random_list}, embarked on a dance of congruence. The measure of their resonance, the cosine similarity, became ##cosine_similarity(eval({random_list}), eval({random_list})), echoing their alignment.",
            f"Euler's totient function, a portal to the secrets of numbers, beckoned. As it deciphered the enigma of {random_int_four}, revealing its essence through ##euler_totient({random_int_four}), it highlighted the patterns that bind.",
            f"The tapestry of this mathematical journey unfolded, revealing the symphony of numbers and the labyrinthine beauty of equations.",
        ],
        [
            f"Once upon a time, in the realm of mathematics, a vector emerged with elements {random_list}.",
            f"Its length was ##length({random_list}), and its L1 norm was ##l1_norm({random_list}).",
            f"Embarking on an adventure, the vector calculated its L2 norm to be ##l2_norm({random_list}).",
            f"Meanwhile, four integers appeared: {random_int_one}, {random_int_two}, {random_int_three}, and {random_int_four}.",
            f"The sum of the first two integers became ##sum([{random_int_one}, {random_int_two}]), while the total sum of all four reached ##sum([{random_int_one}, {random_int_two}, {random_int_three}, {random_int_four}]).",
            f"Numbers danced as an average was calculated using {random_int_one}, {random_int_two}, and {random_int_three}. The result was ##average([{random_int_one}, {random_int_two}, {random_int_three}]).",
            f"A floating point number, {random_float}, made its appearance, adding a touch of randomness to the story.",
            f"A question of truth arose and was answered when the value of truth turned out to be {random_bool}.",
            f"Amidst the wonders, the mystical value π emerged: ##get_pi().",
            f"Similarly, the enigmatic constant e made its presence known: ##get_e().",
            f"Two vectors, with elements {random_list} and {random_list}, set out on a journey to find their dot product.",
            f"After an elaborate calculation, their dot product was unveiled as ##calculate_dot_product({random_list}, {random_list}).",
            f"A twist of fate revealed that 'Racecar' remained unchanged when reversed: ##check_same_string('racecar', ##reverse_string('racecar')).",
            f"In the enchanting realm of mathematical wonders, numbers reigned supreme, casting their spell upon all.",
        ],
        [
            f"In the magical world of Mathopia, two inquisitive friends, {random_list} and {random_list}, set out on an extraordinary mathematical quest.",
            f"Fueled by their insatiable curiosity for numerical wonders, {random_list} stumbled upon the mystical power of the square of the sum of two numbers.",
            f"In their revelation, a formula emerged: ({random_int_one}) plus ({random_int_two}) whole square equals ##a_plus_b_whole_square({random_int_one},{random_int_two}).",
            f"The formula revealed its elegance when expanded: ({random_int_one} squared) plus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared). This intricate dance of numbers resulted in ##a_squared_plus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"On a parallel journey, {random_list} uncovered another intriguing puzzle. The square of the difference between two numbers, enhanced by the resonance of four times their product, revealed its secret.",
            f"The enigmatic equation unfolded: ({random_int_two} minus {random_int_three}) whole squared plus (4 times {random_int_two} times {random_int_three}). This enigma unraveled as ##a_minus_b_whole_squared_plus_4ab({random_int_two},{random_int_three}).",
            f"As their voyage continued, they encountered the essence of simplicity within complexity. The square of the difference between two numbers, distilled to its purest form:",
            f"({random_int_one} minus {random_int_four}) whole squared, concealed its secret within its simplicity. This revelation manifested as ##a_minus_b_whole_squared({random_int_one},{random_int_four}).",
            f"Venturing deeper, they discovered the captivating interplay of squares and differences, intricately woven in an elegant waltz:",
            f"The difference between the squares of {random_int_one} and {random_int_two}, a symphony of numbers orchestrated through ({random_int_one} squared) minus (2 times {random_int_one} times {random_int_two}) plus ({random_int_two} squared). This mathematical ballet led them to ##a_squared_minus_2ab_plus_b_squared({random_int_one},{random_int_two}).",
            f"Yet, their journey remained incomplete without an encounter with the square of the sum of two numbers, shedding the weight of four times their dance:",
            f"({random_int_two} plus {random_int_three}) whole squared, a tale of numbers in harmony and divergence, unfurling as ##a_plus_b_whole_squared_minus_4ab({random_int_two},{random_int_three}).",
            f"In the vast tapestry of Mathopia, they unearthed a gem of simplicity amid complexity, the heart of their expedition encapsulated:",
            f"The sum of the squares of {random_int_two} and {random_int_three}, a harmonious duet in ({random_int_two} squared) plus ({random_int_three} squared), revealing the truth of ##a_squared_plus_b_squared({random_int_two},{random_int_three}).",
            f"Their odyssey through Mathopia persisted, a symphony of exploration driven by their unwavering zeal for numbers and the elegant choreography of calculations.",
        ],
    ]

    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator

    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_four_example_paragraph(),
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
        get_batch_four_example_paragraph(),
        1,
    )
    sample = Utility.create_sample_from_example(
        next_token_example, PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
