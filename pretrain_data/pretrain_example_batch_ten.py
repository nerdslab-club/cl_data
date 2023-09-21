import random

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def get_batch_ten_example_paragraph():
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
            f"Amid the mystical realm of Mathoria, where numbers held the key to extraordinary feats, two intrepid scholars, Sophia and Oliver, embarked on an awe-inspiring journey to uncover the profound magic of mathematics.",
            f"Sophia, a brilliant mathematician, chose to begin her exploration by deciphering the enigmatic world of negative numbers. Her calculations unveiled the truth behind -2 times {random_int_one} times {random_int_two}, yielding the result: ##negative_2ab({random_int_one}, {random_int_two}).",
            f"Meanwhile, Oliver, a curious seeker of positivity, ventured into the realm of positive forces. Guided by his mathematical instincts, he harnessed the energy of 2 times {random_int_three} times {random_int_four}, revealing: ##positive_2ab({random_int_three}, {random_int_four}).",
            f"Sophia's path then led her through the labyrinth of quadratic expressions. With careful precision, she unraveled the complexity of {random_int_one}x + ({random_int_two}x + {random_int_three}), simplifying it to: ##x_plus_a_times_x_plus_b({random_int_one}, {random_int_two}, {random_int_three}).",
            f"Oliver, driven by curiosity, sought the symphony of polynomials. He harmoniously orchestrated {random_int_four}x^2 + {random_int_two}x + {random_int_three}x, with x = {random_int_one}, revealing its musical essence: ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_two}, {random_int_three}).",
            f"As their journey unfolded, Sophia and Oliver united their strengths to unlock the profound mysteries of cubes. The fusion of their efforts, embracing {random_int_two} and {random_int_three}, revealed its concealed truths: ##a_cubed_plus_b_cubed({random_int_two}, {random_int_three}).",
            f"Undaunted by challenges, they delved deeper, encountering a captivating cube difference puzzle. They harnessed the cube of the sum of {random_int_one} and {random_int_four}, meticulously subtracting thrice their cosmic connection, revealing: ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_one}, {random_int_four}).",
            f"Their journey then led them to the world of expressive expansions. The ethereal incantation of ({random_int_two}x + {random_int_three})^2 - ({random_int_one}x - {random_int_four})^2 bore a spellbinding inscription: ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_two}, {random_int_three}).",
            f"Their expedition then unraveled the enigma of cube disparities. The riddle unfurled, revealing the intricate difference between the sacred cube of {random_int_one} and the elusive cube of {random_int_four}: ##a_cubed_minus_b_cubed({random_int_one}, {random_int_four}).",
            f"At the zenith of their journey, Sophia and Oliver faced the ultimate cube challenge. Their insight resonated with cosmic harmonies, unveiling the cube of the difference between {random_int_two} and {random_int_three}, touched by the unity of three, emerging as: ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_two}, {random_int_three}).",
            f"In the end, Sophia and Oliver discovered that Mathoria's tapestry of numbers held the key to unlocking the secrets of the universe. Their journey became an enduring testament to the eternal allure of mathematical exploration.",
            f"Their legacy reverberated through the ages, inspiring future generations of Mathoria to embark on their own quests, driven by the endless wonder of numbers and the boundless realms they unveiled."
        ],
        [
            f"Embark on a mathematical voyage to Numaria, a realm where numbers weave the fabric of reality, and meet Jasper, a young mathematician.",
            f"Jasper's quest unfurled with the art of addition, merging {random_int_one} and {random_int_two} in a harmonious embrace through ##addition({random_int_one},{random_int_two}).",
            f"As twilight painted the sky, Jasper found himself entwined in the intricate dance of subtraction. The enigma between {random_int_two} and {random_int_three} revealed itself through ##subtraction({random_int_two},{random_int_three}).",
            f"Guided by the cosmic symphony, Jasper's spirit resonated with the allure of multiplication. He conjured the universe to unveil the product of {random_float:.2f} and {random_int_four} through ##multiplication({random_float},{random_int_four}).",
            f"Like the dawn's first light, Jasper embarked on the path of division. With a flourish, he uncovered the division of {random_float:.2f} by {random_int_one} through ##division({random_float},{random_int_one}).",
            f"Jasper's insatiable curiosity propelled him to the cosmic dance of exponents. He raised {random_int_three} to the power of {random_int_four}, illuminating the universe's mysteries through ##exponentiation({random_int_three},{random_int_four}).",
            f"Beneath the silvery moonlight, Jasper's heart was drawn to the mystic realm of square roots. He whispered the incantation, unveiling the secrets of {random_int_four}'s square root through ##square_root({random_int_four}).",
            f"As the sun's rays graced the horizon, Jasper faced the enigma of floor division. With resolve, he deciphered the division of {random_int_two} by {random_int_one} through ##floor_division({random_int_two},{random_int_one}).",
            f"In the cosmic tapestry of remainders, Jasper unraveled the hidden rhythm. The dance between {random_int_three} and {random_int_one} was unveiled through ##modulus({random_int_three},{random_int_one}).",
            f"Inscribed in the celestial heavens were the secrets of logarithms. Jasper contemplated the harmony of numbers, calculating the logarithm of {random_float:.2f} with base {random_int_two} through ##logarithm({random_float},{random_int_two}).",
            f"Embracing the cosmic ebb and flow, Jasper resonated with the celestial sine wave. With a profound connection to the universe, he unveiled the sine of an angle {random_float:.2f} degrees through ##sine({random_float}).",
        ],
        [
            f"Step into Arctopia, where numbers compose the very melodies of existence. Amidst this vibrant realm, inhabited by individuals as diverse as the digits themselves ({random_list}), the allure of mathematics thrives.",
            f"On an auspicious day, a mathematician embarked on a quest armed with an enigma: an angle, {random_float}. This angle, a key to unlocking the boundless chambers of trigonometry, revealed the cosmic choreography of cosine.",
            f"From the cosmic canvas emerged the essence of the unknown: the cosine of {random_float} radians, whispered by the universe itself: ##cosine({random_float}). The mathematician's journey now led to the revelation of its tangent.",
            f"The whisper of angles guided the mathematician to unravel the enigmatic tangent of ##arccosine({random_float}). This revelation held not only a numerical value, but also a profound insight etched within its mathematical essence.",
            f"Elsewhere in Arctopia, another soul was captivated by hyperbolic enigmas. Their fascination centered on the hyperbolic sine of {random_int_one}, a formula that seemed to reverberate through the corridors of time.",
            f"As twilight painted the sky with hues of curiosity, young minds gathered to decode the riddles of logarithms. Among them, the base-10 logarithm of {random_int_two} unveiled patterns that transcended the ordinary.",
            f"In the midst of this assembly, a prodigious child pondered the enigma of the cube root of ##hyperbolic_tangent({random_int_three}). A question that resonated with the essence of numbers and the limitless realm of possibilities.",
            f"Amid contemplation, a sage, guardian of ancient wisdom, contemplated the profound union of numbers and angles: ##logarithm_base_2({random_int_four}) raised to the celestial power of ##arcsine({random_float}).",
            f"As destiny wove its intricate threads, the two mathematicians converged, weaving their insights to unlock a cryptic equation: ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
            f"After a symphony of calculations, the answer was unveiled: {random_int_two + random_int_four}. Arctopia rejoiced, a grand celebration of intellect and discovery. And thus, the legacy of Arctopia's mathematical marvels continued to inspire."
        ],
        [
            f"Step into the enchanting world of Arithmos, a realm where numbers weave the tapestry of existence. Amidst its magic, a young seeker named Nora embarked on a journey of discovery and equations.",
            f"Bearing an angle of {random_int_one} degrees, Nora embarked on her quest to translate it into the cryptic language of radians. With the incantation degrees_to_radians, the transformation was unveiled: ##degrees_to_radians({random_int_one}).",
            f"As Nora ventured deeper, she stumbled upon an ancient gateway guarded by the sentinels of greatest common divisor. By invoking the spirits of {random_int_two} and {random_int_three}, she unlocked the gateway, revealing its hidden truths: ##gcd({random_int_two}, {random_int_three}).",
            f"Continuing her expedition, Nora unveiled the ancient scrolls of least common multiples, discovering the hidden unity between {random_int_four} and {random_int_two}: ##lcm({random_int_four}, {random_int_two}).",
            f"In the heart of Arithmos' sacred Numerical Grove, Nora encountered an ancient tree, a living testament to the passage of time. Through the art of isqrt, the tree's age was revealed to be ##isqrt({random_int_three}).",
            f"As twilight painted Arithmos with hues of amethyst and gold, Nora harnessed the essence of congruence. By invoking the pow_mod enchantment, she elevated {random_int_two} to the power of {random_int_one}, modulo {random_int_four}, unveiling a hidden gem: ##pow_mod({random_int_two}, {random_int_one}, {random_int_four}).",
            f"In a realm where time flowed like a river, Nora navigated its currents with the wisdom of ceil, floor, and round. The river's surface reflected the profound difference between {random_float} and {random_int_four}: ##absolute_difference({random_float}, {random_int_four}).",
            f"As Nora's journey unfolded, she realized that each mathematical function was a key to unlock a new dimension of understanding. Armed with this insight, she returned to Arithmos, sharing the tales of her adventure, inspiring others to embark on their own quests to unravel the mystique of numbers.",
        ],
        [
            f"In a realm where the language of numbers held sway, a relentless mathematician embarked on a voyage of discovery.",
            f"With unyielding curiosity, they set out to unravel the enigmas surrounding {random_int_one}, {random_int_two}, and {random_int_three}.",
            f"Their expedition commenced with the riddle of the greatest value between {random_float} and {random_int_one}.",
            f"After moments of contemplation, they revealed the answer: ##greatest_value({random_float}, {random_int_one}).",
            f"Yet, the allure of numbers beckoned them further. Their gaze turned to {random_list}, an array of cryptic numbers.",
            f"The mathematician brought to light the hidden story within, illuminating the elusive product: ##product({random_list}).",
            f"Fueled by an insatiable thirst for understanding, they ventured into the realm of factorials, revealing the enchantment of {random_int_one}!: ##factorial({random_int_one}).",
            f"Still, another mystery lay ahead—the essence of {random_int_two}. Was it a prime number? The truth emerged as ##is_prime({random_int_two}).",
            f"Undeterred, they embarked on the timeless pursuit of prime factors, unearthing the epic saga of {random_int_three}: ##prime_factors({random_int_three}).",
            f"In their journey, they stumbled upon {random_int_four}, a number that hid a secret—it was a perfect square: ##is_perfect_square({random_int_four}).",
            f"Continuing their odyssey, they unveiled the concealed truth of {random_int_three}, a hidden perfect cube: ##is_perfect_cube({random_int_three}).",
            f"With a heart ignited by the power of numbers, the mathematician returned to {random_list}, deciphering their collective story through the prism of the mean: ##mean({random_list}).",
            f"Yet, a final enigma remained—the elusive median, the rhythmic pulse of the numbers: ##median({random_list}).",
            f"And so, the mathematician's expedition through the realm of numbers persevered, revealing the intricate tapestry woven by the language of mathematics."
        ],
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
        ],
        [
            f"Venture into a realm where numbers orchestrate tales and equations reveal secrets,",
            f"unveiling an enigmatic array of numbers: {random_list}.",
            f"From this array, the mightiest number emerged: ##max_value({random_list}).",
            f"Yet, the most unassuming number took its place: ##min_value({random_list}).",
            f"Amidst this world of numbers, a lone integer stepped into the limelight:",
            f"{random_int_one}, an enigmatic figure, wrapped in intrigue.",
            f"Soon after, another integer graced the stage, introduced as",
            f"{random_int_two}, the product of {random_int_one} combining with another concealed integer.",
            f"As the narrative continued to unfold, another integer emerged:",
            f"{random_int_three}, formed from the fusion of {random_int_two} and a hidden number.",
            f"But this tale delved deeper than numbers alone; a random float,",
            f"{random_float}, made a brief but captivating appearance, igniting curiosity.",
            f"With the magic of mathematics, the cube root of {random_int_one} was unveiled:",
            f"##nth_root({random_int_one}, 3) materialized as the solution to the riddle.",
            f"In the symphony of numbers, the geometric mean of the list whispered its harmony:",
            f"##geometric_mean({random_list}) bestowed its concealed melody upon the narrative.",
            f"A question lingered: Was {random_int_one} a power of two?",
            f"The answer emerged: ##is_power_of_two({random_int_one}).",
            f"Binary whispers danced as {random_int_one} transformed into binary code:",
            f"##decimal_to_binary({random_int_one}) deciphered the binary enigma.",
            f"Then, in a twist of enchantment, binary reverted to its original form:",
            f"##binary_to_decimal(##decimal_to_binary({random_int_one})) uncovered the truth.",
            f"The magic of symmetry unveiled {random_int_one} as a palindrome:",
            f"##is_palindrome({random_int_one}) affirmed its symmetrical nature.",
            f"The story continued with the digits of {random_int_two}, revealing their collective tale:",
            f"##sum_of_digits({random_int_two}) unveiled the power locked within their union.",
            f"In the realm of triangles, with sides {random_int_one} and {random_int_two},",
            f"the elusive hypotenuse emerged: ##hypotenuse({random_int_one}, {random_int_two}).",
            f"And thus, the chronicle of numbers, calculations, and enigmas neared its finale,",
            f"leaving behind a legacy of mathematical wonder and an eternal quest for understanding."
        ],
        [
            f"Step into a realm where numbers orchestrate a symphony of mystery, as a circle emerges with its enigmatic radius of {random_float}. Guided by the incantation of ##circle_area({random_float}), we unveil its hidden area, a puzzle piece in the grand mosaic of mathematics.",
            f"In the grand mathematical masquerade, {random_int_one} participants are chosen from a realm of {random_int_two}, weaving their sequence through the dance of permutations with the spell ##permutation({random_int_two}, {random_int_one}). Their arrangement forms an elegant equation that captivates the imagination.",
            f"In the symphony of numbers, {random_int_two} harmonious notes are plucked from a collection of {random_int_three}. Their fusion, guided by the enchantment of ##combination({random_int_three}, {random_int_two}), resonates like a melodic chord, harmonizing unity and diversity.",
            f"A transformation, akin to destiny's enigma, unfurls. The number {random_float} succumbs to the enigmatic transformation of ##invert_number({random_float}), revealing a mirrored dimension, as numbers themselves unveil secrets of symmetry.",
            f"Embarking into the realm of integers, {random_float} transforms, revealing its integer essence through the invocation of ##float_to_int({random_float}). This transition mirrors the intricate dance between the continuous and the discrete.",
            f"The integer {random_int_three} embarks on a metamorphosis, relinquishing its integer mantle for a floating existence through the enchantment of ##int_to_float({random_int_three}). This transformation echoes the fluidity of mathematical concepts.",
            f"From the canvas of mathematical sequences arises a geometric series, with a prologue of {random_float}, embracing a recurring motif of {random_float}, and reaching a crescendo of {random_int_one} iterations, as revealed by ##geometric_series_sum({random_float}, {random_float}, {random_int_one}).",
            f"A sigmoid curve, a bridge between extremes, cradles the number {random_float}, culminating in its transformation through the invocation of ##sigmoid({random_float}). A revelation that mirrors the profound journey from chaos to equilibrium.",
            f"Two vectors, symbolized by {random_list} and {random_list}, engage in a dance of resonance. Their connection, measured by the cosine similarity, unfolds as ##cosine_similarity(eval({random_list}), eval({random_list})), an ode to their harmonious alignment.",
            f"Euler's totient function, an enigmatic oracle of numbers, beckons, unfurling the secrets of {random_int_four}. Its invocation, ##euler_totient({random_int_four}), reveals hidden patterns as numbers whisper their tales of co-prime dance.",
            f"As our odyssey through the numerical realm nears its finale, the echoes of equations and calculations linger, leaving behind a sense of wonder and reverence for the infinite world of mathematics."
        ],
        [
            f"In the realm where numbers reign supreme, a vector emerged, its elements a symphony of possibilities: {random_list}.",
            f"Peering into its essence, it unveiled a length of ##length({random_list}). Its L1 norm, deciphered through ##l1_norm({random_list}), danced with its L2 norm, ##l2_norm({random_list}), crafting a tale of contrasts.",
            f"Meanwhile, four integers took center stage: {random_int_one}, {random_int_two}, {random_int_three}, and {random_int_four}.",
            f"Their harmonious rhythm echoed in the sum of the first two integers, revealing ##sum([{random_int_one}, {random_int_two}]), while the grand ensemble resonated as ##sum([{random_int_one}, {random_int_two}, {random_int_three}, {random_int_four}]).",
            f"Delving into depths unknown, the pursuit of an average brought together {random_int_one}, {random_int_two}, and {random_int_three}. The outcome unfolded as ##average([{random_int_one}, {random_int_two}, {random_int_three}]).",
            f"Amidst the tapestry of numbers, a floating point number, {random_float}, made its appearance, painting the story with shades of unpredictability.",
            f"Amid contemplations of truth, the value of truth emerged as {random_bool}.",
            f"From the realms of the infinite, the enigmatic π emerged, bearing the wisdom of circles: ##get_pi().",
            f"Similarly, the mystical constant e extended its invitation: ##get_e().",
            f"In a dance of discovery, two vectors, embodying the elements {random_list} and {random_list}, embarked on a shared odyssey to uncover their dot product.",
            f"Through intricate calculations, their journey unveiled the dot product as ##calculate_dot_product({random_list}, {random_list}).",
            f"A twist in the narrative led to the revelation that 'Racecar' remained unchanged, even when mirrored: ##check_same_string('racecar', ##reverse_string('racecar')).",
            f"Within the magical tapestry of mathematics, numbers wove tales of intrigue and mystery, inviting all to unlock their secrets."
        ],
        [
            f"In the enigmatic realm of Mathovia, two intrepid companions, {random_list[0]} and {random_list[1]}, embarked on a captivating mathematical expedition.",
            f"Driven by their unyielding curiosity, {random_list[0]} stumbled upon the hidden marvels within the square of the sum of two numbers.",
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
            f"In the expansive tapestry of Mathovia, they unearthed a gem of simplicity amid complexity, the heart of their expedition encapsulated:",
            f"The sum of the squares of {random_int_two} and {random_int_three}, a harmonious blend in ({random_int_two} squared) plus ({random_int_three} squared), revealing the essence of ##a_squared_plus_b_squared({random_int_two},{random_int_three}).",
            f"Their odyssey through Mathovia continued, a symphony of exploration driven by their unyielding passion for numbers and the graceful choreography of calculations.",
        ]
    ]

    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator

    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_ten_example_paragraph(),
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
        get_batch_ten_example_paragraph(),
        1,
    )
    sample = Utility.create_sample_from_example(
        next_token_example, PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
