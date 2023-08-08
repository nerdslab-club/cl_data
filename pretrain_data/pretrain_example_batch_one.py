import random

import spacy

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_masked_token_batch_one_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_one_example_paragraph()
        for paragraph in paragraphs:
            masked_data = Utility.create_masked_input_output_example(paragraph, nlp)
            examples.extend(masked_data)
    return examples


def create_next_token_batch_one_example(count: int, nlp: spacy.Language):
    examples = []
    for _ in range(count):
        paragraphs = __get_batch_one_example_paragraph()
        for paragraph in paragraphs:
            next_token_data = Utility.create_next_word_input_output_example(
                paragraph, nlp
            )
            examples.extend(next_token_data)
    return examples


def __get_batch_one_example_paragraph():
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
            f"In the town of Mathematicville, where numbers ruled the day, lived a young mathematician named Alex.",
            f"Alex's favorite pastime was solving mathematical puzzles. One sunny morning, they woke up to a challenge.",
            f"They were asked to add {random_int_one} and {random_int_two}. Eager to begin, Alex quickly solved it using ##addition({random_int_one},{random_int_two}).",
            f"Next, they encountered a tricky subtraction problem: {random_int_three} minus {random_int_one}. The answer was found using ##subtraction({random_int_three},{random_int_one}).",
            f"Venturing deeper into the world of numbers, they were faced with a multiplication puzzle. How much is {random_float} multiplied by {random_int_four}? The answer was revealed through ##multiplication({random_float},{random_int_four}).",
            f"A river blocked their path. They needed to cross it by solving the division problem: {random_int_three} divided by {random_int_two}. The solution came from ##division({random_int_three},{random_int_two}).",
            f"Curiosity led them to a towering puzzle involving exponentiation: {random_int_four} raised to the power of {random_int_one}. The answer was found through ##exponentiation({random_int_four},{random_int_one}).",
            f"A mysterious artifact held a challenge: find the square root of {random_int_three}. Alex's skills shone as they used ##square_root({random_int_three}).",
            f"In a hidden chamber, they encountered a question about floor division: How many times does {random_int_one} divide into {random_int_three}? The solution was given by ##floor_division({random_int_three},{random_int_one}).",
            f"Further on, a mystical portal demanded the modulus of {random_int_two} and {random_int_one}. Alex solved it using ##modulus({random_int_two},{random_int_one}).",
            f"The journey continued to a room filled with ancient scrolls. One scroll held a logarithmic challenge: What is the logarithm base {random_float} of {random_int_two}? The answer was revealed by ##logarithm({random_int_two},{random_float}).",
            f"High above, a celestial challenge awaited. They needed to find the sine of {random_float} degrees. The solution came from ##sine({random_float}).",
            f"With each challenge surmounted, Alex's mastery of math grew. The townspeople marveled at their prowess and knowledge.",
            f"In the end, Alex realized that the true treasure wasn't just the answers they found, but the journey of discovery itself.",
            f"And so, the legend of Alex, the mathematical adventurer, spread far and wide, inspiring others to embrace the magic of numbers.",
        ],
        [
            f"The world of mathematics is a realm of endless possibilities. Among its many operations, let's explore...",
            f"Addition: Imagine having {random_int_one} apples and gaining {random_int_two} more. You would then have ##addition({random_int_one},{random_int_two}) apples.",
            f"Subtraction: If you had {random_int_three} dollars and spent {random_int_two}, you'd have ##subtraction({random_int_three},{random_int_two}) dollars left.",
            f"Multiplication: If a field has a length of {random_float} meters and a width of {random_float}, its area would be ##multiplication({random_float},{random_float}).",
            f"Division: If you share {random_float} candies among {random_float} friends, each would get ##division({random_float},{random_float}) candies.",
            f"Exponentiation: Consider the power of a rocket with thrust {random_int_one} and time {random_int_two}. The total force would be ##exponentiation({random_int_one},{random_int_two}).",
            f"Square Root: The length of the hypotenuse in a right triangle with sides {random_int_three} and {random_int_four} would be ##square_root({random_int_three}).",
            f"Floor Division: When dividing {random_int_two} by {random_int_three}, you get ##floor_division({random_int_two},{random_int_three}) with no remainder.",
            f"Modulus: Dividing {random_int_three} by {random_int_one} leaves a remainder of ##modulus({random_int_three},{random_int_one}).",
            f"Logarithm: The base-{random_int_one} logarithm of {random_int_two} is ##logarithm({random_int_two},{random_int_one}).",
            f"Sine: In a right triangle, the ratio of the length of the side opposite the angle to the hypotenuse is the sine. For an angle of {random_float} degrees, the sine is ##sine({random_float}).",
            f"These mathematical operations are like tools in a craftsman's hands, shaping the world of numbers and giving rise to the wonders of science and technology.",
        ],
        [
            f"In the realm of mathematics, the tapestry of numbers weaves intricate patterns that...",
            f"Cosine: Imagine an angle of {random_float} degrees. The cosine of this angle is ##cosine({random_float}).",
            f"Tangent: The tangent of an angle can be found using the formula ##tangent({random_float}).",
            f"Arcsine: If the sine of an angle is {random_float}, then the angle itself is ##arcsine({random_float}).",
            f"Arccosine: Similarly, if the cosine of an angle is {random_float}, the angle is ##arccosine({random_float}).",
            f"Arctangent: And if the tangent of an angle is {random_float}, the angle is ##arctangent({random_float}).",
            f"Hyperbolic Sine: The hyperbolic sine of {random_float} is ##hyperbolic_sine({random_float}).",
            f"Hyperbolic Cosine: The hyperbolic cosine of {random_float} is ##hyperbolic_cosine({random_float}).",
            f"Hyperbolic Tangent: The hyperbolic tangent of {random_float} is ##hyperbolic_tangent({random_float}).",
            f"Logarithm (Base 10): The logarithm base 10 of {random_float} is ##logarithm_base_10({random_float}).",
            f"Logarithm (Base 2): The logarithm base 2 of {random_float} is ##logarithm_base_2({random_float}).",
            f"These mathematical functions unravel hidden insights, letting us comprehend the world from a different perspective.",
        ],
        [
            f"In the town of Mathematicville, where numbers ruled the day, lived a young mathematician named Alex.",
            f"Alex's favorite pastime was solving mathematical puzzles. One sunny morning, they woke up to a challenge.",
            f"They were asked to add {random_int_one} and {random_int_two}. Eager to begin, Alex quickly solved it using ##addition({random_int_one},{random_int_two}).",
            f"Next, they encountered a tricky subtraction problem: {random_int_three} minus {random_int_one}. The answer was found using ##subtraction({random_int_three},{random_int_one}).",
            f"Venturing deeper into the world of numbers, they were faced with a multiplication puzzle. How much is {random_float} multiplied by {random_int_four}? The answer was revealed through ##multiplication({random_float},{random_int_four}).",
            f"A river blocked their path. They needed to cross it by solving the division problem: {random_int_three} divided by {random_int_two}. The solution came from ##division({random_int_three},{random_int_two}).",
            f"Curiosity led them to a towering puzzle involving exponentiation: {random_int_four} raised to the power of {random_int_one}. The answer was found through ##exponentiation({random_int_four},{random_int_one}).",
            f"A mysterious artifact held a challenge: find the square root of {random_int_three}. Alex's skills shone as they used ##square_root({random_int_three}).",
            f"In a hidden chamber, they encountered a question about floor division: How many times does {random_int_one} divide into {random_int_three}? The solution was given by ##floor_division({random_int_three},{random_int_one}).",
            f"Further on, a mystical portal demanded the modulus of {random_int_two} and {random_int_one}. Alex solved it using ##modulus({random_int_two},{random_int_one}).",
            f"The journey continued to a room filled with ancient scrolls. One scroll held a logarithmic challenge: What is the logarithm base {random_float} of {random_int_two}? The answer was revealed by ##logarithm({random_int_two},{random_float}).",
            f"High above, a celestial challenge awaited. They needed to find the sine of {random_float} degrees. The solution came from ##sine({random_float}).",
            f"With each challenge surmounted, Alex's mastery of math grew. The townspeople marveled at their prowess and knowledge.",
            f"Next, Alex encountered a perplexing challenge that required converting degrees to radians: {random_float} degrees. They used ##degrees_to_radians({random_float}).",
            f"Then came a puzzle that required converting radians back to degrees: {random_float} radians. Alex used ##radians_to_degrees({random_float}).",
            f"A curious artifact presented a problem in greatest common divisor: find the GCD of {random_int_two} and {random_int_one}. Alex's calculations revealed the answer through ##gcd({random_int_two},{random_int_one}).",
            f"In another hidden chamber, a challenge in least common multiple awaited. The task was to find the LCM of {random_int_two} and {random_int_one}. Alex used ##lcm({random_int_two},{random_int_one}).",
            f"They stumbled upon an ancient oracle which required finding the integer square root of {random_int_one}. The answer came through ##isqrt({random_int_one}).",
            f"A magical enigma tasked them with calculating {random_int_one} raised to the power of {random_int_two}, modulo {random_int_four}. They used ##pow_mod({random_int_one},{random_int_two},{random_int_four}).",
            f"Upon reaching the summit of their journey, they found a treasure room with enchanted floors. To uncover the ceiling of {random_float}, Alex employed ##ceil({random_float}).",
            f"Within the treasure room, the floor seemed to hold secrets too. The challenge was to find the floor of {random_float}. Alex used ##floor({random_float}).",
            f"Among the treasures, there was a mystery of rounding. Alex was asked to round {random_float} to the nearest integer. They used ##round({random_float}).",
            f"As their journey drew to an end, a profound realization emerged. The true treasure was not just the answers they'd discovered, but the voyage of exploration itself.",
            f"And so, the tale of Alex, the mathematical explorer, spread far and wide, inspiring others to embrace the enchanting world of numbers.",
        ],
        [
            f"In the town of Mathematicville, where numbers ruled the day, lived a young mathematician named Alex.",
            f"Alex's favorite pastime was solving mathematical puzzles. One sunny morning, they woke up to a challenge.",
            f"They were asked to find the greatest value between {random_float} and {random_int_one}. Eager to begin, Alex quickly solved it using ##greatest_value({random_float},{random_int_one}).",
            f"Next, they encountered a tricky task: finding the smallest value between {random_int_three} and {random_int_two}. The answer was found using ##smallest_value({random_int_three},{random_int_two}).",
            f"Venturing deeper into the world of numbers, they faced a challenge to find the product of the list {random_list}. The answer was revealed through ##product({random_list}).",
            f"A river blocked their path. They needed to cross it by solving the factorial of {random_int_four}. The solution came from ##factorial({random_int_four}).",
            f"Curiosity led them to a towering puzzle about primality: Is {random_int_one} a prime number? Alex's skills shone as they used ##is_prime({random_int_one}).",
            f"In a hidden chamber, they encountered a question about prime factors: What are the prime factors of {random_int_two}? The solution was given by ##prime_factors({random_int_two}).",
            f"Further on, a mystical portal demanded the truth about perfect squares: Is {random_int_three} a perfect square? Alex solved it using ##is_perfect_square({random_int_three}).",
            f"In another hidden realm, the mystery of perfect cubes awaited. The task was to determine if {random_int_one} is a perfect cube. Alex used ##is_perfect_cube({random_int_one}).",
            f"The journey continued to a room filled with numbers. One scroll held a challenge: Calculate the mean of the list {random_list}. The answer was revealed by ##mean({random_list}).",
            f"High above, a celestial challenge awaited. They needed to find the median of the list {random_list}. The solution came from ##median({random_list}).",
            f"With each challenge surmounted, Alex's mastery of math grew. The townspeople marveled at their prowess and knowledge.",
            f"As their journey drew to an end, a profound realization emerged. The true treasure was not just the answers they'd discovered, but the voyage of exploration itself.",
            f"And so, the tale of Alex, the mathematical explorer, spread far and wide, inspiring others to embrace the enchanting world of numbers.",
        ],
        [
            f"In the bustling city of Numina, where the hum of numbers echoed through every street, lived a young accountant named Mia.",
            f"Mia was known far and wide for her meticulous attention to detail and love for all things numerical. Her favorite spot was the city's grand library, where she could lose herself in mathematical wonders.",
            f"One day, Mia received a letter inviting her to a prestigious mathematics conference held in the distant town of Equatia. Excitement coursing through her veins, she embarked on a journey.",
            f"Upon arrival, the conference's theme emerged: 'Unveiling the Mysteries of Numbers.' The participants were presented with a challenge: Find the result of the Rectified Linear Unit (ReLU) activation function for the value {random_float}. Eager to prove herself, Mia used ##relu({random_float}) to solve it.",
            f"As the conference continued, friendships formed among the attendees. Collaborations flourished, leading to the next challenge. Mia was tasked with sorting a list of integers in ascending order: {random_list}. She employed ##ascending_sort({random_list}) to organize the numbers.",
            f"A night of stargazing inspired the next challenge. The participants were to sort another list, but this time in descending order: {random_list}. Mia skillfully used ##descending_sort({random_list}) to arrange the values.",
            f"Amidst workshops and discussions, a riddle emerged: 'What is the square of {random_int_one}?' Mia answered confidently with ##square_int({random_int_one}).",
            f"The conference's grand finale involved intricate calculations. Mia was given a task: 'Calculate the square of {random_float}.' She used ##square({random_float}) to unveil the answer.",
            f"A challenge about absolute value awaited. 'What is the absolute value of {random_float}?' Mia solved it using ##absolute({random_float}).",
            f"In a magical session, the power of ten was explored. The question posed was: 'What is ten raised to the power of {random_float}?' Mia confidently answered using ##power_of_ten({random_float}).",
            f"As the conference drew to a close, the topic shifted to cubes. Mia's task was to calculate the cube of {random_float}. She used ##cube({random_float}) to reveal the result.",
            f"A discussion on roots led to a question: 'What is the cube root of {random_float}?' Mia applied ##cube_root({random_float}) to find the answer.",
            f"The conference was filled with debates and discussions. A question about parity arose: 'Is {random_int_two} an even number?' Mia employed ##is_even({random_int_two}) to settle the matter.",
            f"Another puzzle emerged: 'Is {random_int_one} an odd number?' Mia skillfully used ##is_odd({random_int_one}) to determine the outcome.",
            f"As the conference concluded, Mia realized that numbers were not just tools; they were a language of discovery and connection. She returned to Numina, inspired to share her newfound knowledge.",
            f"And so, Mia's journey through Equatia's mathematical realm became a tale of exploration, friendship, and the beauty of numbers. Her passion ignited curiosity in others, ensuring that the mysteries of mathematics continued to thrive.",
        ],
        [
            f"Welcome to the land of Numenoria, a realm where the language of numbers weaves the very fabric of reality.",
            f"In the heart of this mystical land lived Lila, a young mathematician whose curiosity knew no bounds.",
            f"Lila's days were spent unraveling the secrets of numbers, but one day, a peculiar letter arrived.",
            f"The letter invited Lila to the 'Numenoria Challenge'—a journey through the mathematical wonders of her land.",
            f"As Lila embarked on her adventure, she encountered the first challenge: Find the maximum value in the list {random_list}.",
            f"Quickly, she used ##max_value({random_list}) to uncover the largest number in the sequence.",
            f"The next challenge appeared as a riddle: 'What is the smallest value in the list {random_list}?'",
            f"Lila confidently solved it using ##min_value({random_list}).",
            f"As she journeyed deeper, the land presented a question: 'Calculate the cube root of {random_float}, rounded to 2 decimal places.'",
            f"With precision, Lila employed ##nth_root({random_float}, 3) to uncover the answer.",
            f"A mysterious gate guarded by a geometric puzzle stood in her path. 'Calculate the geometric mean of the numbers {random_list}.'",
            f"Equipped with knowledge, Lila utilized ##geometric_mean({random_list}) to unveil the secret.",
            f"A towering tree, surrounded by fireflies, whispered a question: 'Is {random_int_one} a power of two?'",
            f"Lila used ##is_power_of_two({random_int_one}) to provide the answer.",
            f"As she journeyed through Numenoria, she came across a cavern of ancient scripts. 'Decode the binary sequence {random_binary_str} to decimal.'",
            f"Delving into the mysteries of binary, Lila applied ##binary_to_decimal('{random_binary_str}') to decipher the code.",
            f"An enigmatic mirror challenged her next: 'Is {random_int_two} a palindrome?'",
            f"With a keen eye, Lila determined the truth using ##is_palindrome('{random_int_two}').",
            f"Amidst the challenges, Lila discovered a sparkling pool with a question: 'Calculate the sum of digits of {random_int_three}.'",
            f"She applied ##sum_of_digits({random_int_three}) to reveal the answer.",
            f"Finally, her path led to a labyrinth, guarded by a puzzle: 'Find the hypotenuse of a right triangle with sides {random_int_one} and {random_int_two}.'",
            f"Lila employed Pythagoras' wisdom, using ##hypotenuse({random_int_one}, {random_int_two}) to unlock the way.",
            f"Through trials and triumphs, Lila's journey was a testament to the power of numbers.",
            f"She returned to her homeland, a heroine of Numenoria, sharing tales of her adventure and inspiring others to explore the wonders of mathematics.",
            f"And so, the legend of Lila, the mathematical explorer, spread like wildfire, igniting curiosity and reverence for the beauty of numbers in every corner of Numenoria.",
        ],
        [
            "In the realm of Numerica, where equations danced in the air and numbers glowed with magic, lived an aspiring mathematician named Ava.",
            "Ava's fascination with numbers led her on a journey that would forever change her destiny.",
            "One day, an old parchment appeared at her doorstep, bearing a mysterious riddle:",
            "'Find the area of a circle with radius {random_float}, rounding to two decimal places.'",
            "Determined to solve the puzzle, Ava used ##circle_area({random_float}) to unveil the secret.",
            "The solution granted her access to the next challenge—a quest for permutations:",
            "'Calculate the number of ways to arrange {random_int_one} objects out of {random_int_two}.'",
            "Ava skillfully employed ##permutation({random_int_two}, {random_int_one}) to navigate through the permutations.",
            "As her journey unfolded, she encountered a locked door. The key lay in combinations:",
            "'How many combinations are possible when choosing {random_int_one} items from {random_int_three}?'",
            "With grace, Ava solved it using ##combination({random_int_three}, {random_int_one}).",
            "A cryptic encounter led to the enigma of inversion:",
            "'What is the reciprocal of {random_float}, rounded to four decimal places?'",
            "Ava's expertise shone as she used ##invert_number({random_float}) to decipher the puzzle.",
            "The path revealed a bridge to transformation:",
            "'Convert {random_float} to an integer using truncation.'",
            "Ava confidently used ##float_to_int({random_float}) to continue her journey.",
            "In a radiant glade, an ethereal riddle emerged:",
            "Return {random_int_four} as a floating-point value.",
            "Knowledge as her guide, Ava employed ##int_to_float({random_int_four}) to unlock the wisdom.",
            "As she ventured further, an ancient tree whispered secrets of geometric series:",
            "'Calculate the sum of a geometric series with first term {random_float}, common ratio {random_float}, and {random_int_one} terms.'",
            "Ava applied the formula, using ##geometric_series_sum({random_float}, {random_float}, {random_int_one}) to reveal the sum.",
            "The climax of her odyssey approached, presenting a question of sigmoidal nature:",
            "'Determine the sigmoid value of {random_float}.'",
            "Ava's calculations resonated with precision as she employed ##sigmoid({random_float}) to unveil the answer.",
            "In the final moments of her journey, Ava was faced with a challenge of vectors:",
            "'Compute the cosine similarity between vectors {random_list} and {random_list}.'",
            "Drawing on her skills, Ava applied ##cosine_similarity({random_list}, {random_list}) to find the solution.",
            "A triumphant epiphany awaited her at the end—an exploration of Euler's totient function:",
            "'Find the Euler's totient value of {random_int_one}.'",
            "With reverence for the ancient knowledge, Ava used ##euler_totient({random_int_one}) to unlock the final treasure.",
            "As she returned to Numerica, Ava carried not just the answers, but a deep connection to the mathematical wonders that shape the universe.",
            "Her journey became a tale told through generations, inspiring all to embark on their own mathematical odysseys.",
        ],
        [
            "In the kingdom of Numerosia, where equations adorned the walls and numbers held the key to understanding, lived a passionate mathematician named Mia.",
            "Mia's life was dedicated to unraveling mathematical puzzles, and her reputation extended far beyond the kingdom's borders.",
            "One fateful day, a mysterious messenger delivered an ornate scroll to her doorstep.",
            "The scroll revealed an invitation to a prestigious mathematics symposium, promising challenges that would test the limits of her expertise.",
            "Upon arrival at the symposium, Mia encountered her first challenge:",
            "'Calculate the area of a circle with radius {random_float}, rounding to two decimal places.'",
            "Determined to succeed, Mia employed ##circle_area({random_float}) to unlock the circle's secret.",
            "As the symposium continued, friendships formed and camaraderie filled the air. Mia faced her next test:",
            "'Calculate the number of permutations for {random_int_one} objects out of {random_int_two}.'",
            "Mia's prowess in permutations shone as she used ##permutation({random_int_two}, {random_int_one}) to solve the puzzle.",
            "In the heart of the symposium, a door to knowledge stood—a question of combinations:",
            "'How many combinations are possible when choosing {random_int_one} items from {random_int_three}?'",
            "With precision, Mia used ##combination({random_int_three}, {random_int_one}) to unveil the secret.",
            "A cryptic passage led to the enigma of inversion:",
            "'What is the reciprocal of {random_float}, rounded to four decimal places?'",
            "Mia's expertise shone as she used ##invert_number({random_float}) to solve the riddle.",
            "Her journey unveiled a path to transformation:",
            "'Convert {random_float} to an integer using truncation.'",
            "With confidence, Mia employed ##float_to_int({random_float}) to continue her symposium adventure.",
            "In a hidden alcove, an ethereal riddle emerged:",
            "'Return {random_int_four} as a floating-point value.'",
            "Mia's understanding of transformation was evident as she used ##int_to_float({random_int_four}) to unveil the answer.",
            "Amidst the symposium's brilliance, an ancient tree whispered secrets of geometric series:",
            "'Calculate the sum of a geometric series with first term {random_float}, common ratio {random_float}, and {random_int_one} terms.'",
            "Mia's skillful application of the formula, using ##geometric_series_sum({random_float}, {random_float}, {random_int_one}), revealed the sum.",
            "The climax of her symposium journey approached, presenting a question of sigmoidal nature:",
            "'Determine the sigmoid value of {random_float}.'",
            "Mia's calculations resonated with precision as she used ##sigmoid({random_float}) to unveil the answer.",
            "In the final moments of her journey, Mia faced a challenge of vectors:",
            "'Compute the cosine similarity between vectors {random_list} and {random_list}.'",
            "Drawing on her expertise, Mia employed ##cosine_similarity({random_list}, {random_list}) to find the solution.",
            "The symposium's culmination arrived with a tribute to ancient knowledge—an exploration of Euler's totient function:",
            "'Find the Euler's totient value of {random_int_one}.'",
            "Mia embraced the wisdom of the past, using ##euler_totient({random_int_one}) to unveil the final revelation.",
            "As the symposium concluded, Mia returned to Numerosia as a celebrated mathematician, carrying the symposium's lessons with her.",
            "Her journey became a story of inspiration, resonating with all who sought to explore the boundless wonders of numbers.",
        ],
        [
            "In the enchanting land of Mathoria, where numbers whispered secrets and equations glowed like constellations, lived a young mathematician named Leo.",
            "Leo's days were spent uncovering the mysteries of mathematics, until a mysterious scroll appeared on his doorstep one morning.",
            "The scroll beckoned him to a grand mathematics festival, promising challenges that would test his skills.",
            "Upon arriving at the festival, Leo encountered his first puzzle:",
            "'Calculate the area of a circle with radius {random_float}, rounded to two decimal places.'",
            "Eager to impress, Leo used ##circle_area({random_float}) to reveal the circle's secret.",
            "The festival's atmosphere buzzed with excitement and camaraderie as Leo faced his next task:",
            "'Determine the number of permutations for {random_int_one} objects out of {random_int_two}.'",
            "Leo's swift calculations, powered by ##permutation({random_int_two}, {random_int_one}), earned him admiration.",
            "A gateway to wisdom appeared in the form of combinations:",
            "'Find the number of combinations when selecting {random_int_one} items from {random_int_three}.'",
            "Leo showcased his expertise by employing ##combination({random_int_three}, {random_int_one}), impressing fellow participants.",
            "A hidden puzzle emerged—a riddle about inversion:",
            "'What is the reciprocal of {random_float}, rounded to four decimal places?'",
            "With determination, Leo used ##invert_number({random_float}) to solve the enigma.",
            "Guided by the festival's mystical aura, Leo faced a transformational task:",
            "'Convert {random_float} to an integer using truncation.'",
            "Leo confidently used ##float_to_int({random_float}) to unlock the next challenge.",
            "An ethereal realm whispered of conversion:",
            "'Return {random_int_four} as a floating-point value.'",
            "Leo embraced the knowledge, utilizing ##int_to_float({random_int_four}) to traverse the mystical paths.",
            "Amidst the festival's grandeur, a radiant glade unveiled geometric series:",
            "'Calculate the sum of a geometric series with first term {random_float}, common ratio {random_float}, and {random_int_one} terms.'",
            "Leo's mathematical prowess shone as he used ##geometric_series_sum({random_float}, {random_float}, {random_int_one}) to reveal the sum.",
            "The peak of the festival approached, introducing the sigmoid function:",
            "'Determine the sigmoid value of {random_float}.'",
            "Leo's calculations resonated with precision as he applied ##sigmoid({random_float}) to unveil the answer.",
            "In the final moments of the festival, Leo faced a challenge of vectors:",
            "'Compute the cosine similarity between vectors {random_list} and {random_list}.'",
            "Drawing on his skills, Leo employed ##cosine_similarity({random_list}, {random_list}) to find the solution.",
            "The festival reached its crescendo with an exploration of Euler's totient function:",
            "'Find the Euler's totient value of {random_int_one}.'",
            "Leo embraced the ancient wisdom, using ##euler_totient({random_int_one}) to unveil the final revelation.",
            "As the festival concluded, Leo returned to Mathoria with newfound knowledge and a heart full of gratitude for the magic of mathematics.",
            "His journey became a beacon of inspiration, inviting all to immerse themselves in the enchanting world of numbers.",
        ],
        [
            f"Once upon a time, in a land where numbers ruled, there lived a mathematician named Alex. Alex loved exploring the properties of numbers and vectors.",
            f"One day, Alex decided to calculate the l1_norm of a random vector: {random_list}. After some calculations, the result was ##l1_norm({random_list}).",
            f"Next, Alex wanted to find the l2_norm of the same vector. The result was ##l2_norm({random_list}).",
            f"Feeling inspired, Alex decided to find the average of a set of random numbers: {random_int_one}, {random_int_two}, and {random_int_three}. The average was ##average([{random_int_one}, {random_int_two}, {random_int_three}]).",
            f"Curious about the sum of those numbers, Alex computed the sum as ##sum([{random_int_one}, {random_int_two}, {random_int_three}]).",
            f"Alex wondered about the length of another random vector: {random_list}. After calculations, the length turned out to be ##length({random_list}).",
            f"Switching gears, Alex checked if two random strings were the same: 'math' and 'science'. It was ##check_same_string('math', 'science').",
            f"To add a twist, Alex decided to reverse a random string: 'calculator'. The result was ##reverse_string('calculator').",
            f"Eager to find some constants, Alex calculated an approximation of π: ##get_pi(). Additionally, the value of Euler's number e was ##get_e().",
            f"Now, for a vector challenge, Alex calculated the dot product of two vectors: {random_list} and {random_list}. The result was ##calculate_dot_product({random_list}, {random_list}).",
            f"Alex's mathematical adventure continued with an exploration of exponentiation. The result of raising {random_int_one} to the power of {random_int_four} was ##exponentiation({random_int_one}, {random_int_four}).",
            f"The journey didn't end there. Alex decided to calculate the cube root of {random_int_three}. After some calculations, the result was ##cube_root({random_int_three}).",
            f"Finally, in a moment of randomness, Alex checked if a random float {random_float} was greater than or equal to 0.5. The result was ##greater_than_or_equal({random_float}, 0.5).",
            f"As the day came to an end, Alex marveled at the beauty of mathematics and the power of calculations.",
        ],
        [
            f"Once upon a time, in the realm of algebraic mysteries, lived a mathematician named Claire. Claire was known far and wide for her prowess in solving intricate equations and unraveling mathematical enigmas.",
            f"One sunny morning, Claire set out to explore the wonders of binomial expansions. She started by calculating the value of (a + b)^2, where a = {random_int_one} and b = {random_int_two}. The result was ##a_plus_b_whole_square({random_int_one}, {random_int_two}).",
            f"Buoyed by her success, Claire ventured further into the realm of binomials. She delved into (a^2 + 2ab + b^2), with a = {random_int_three} and b = {random_int_four}. The result was ##a_squared_plus_2ab_plus_b_squared({random_int_three}, {random_int_four}).",
            f"As the day progressed, Claire's curiosity led her to explore another fascinating expression: (a - b)^2 + 4ab. With a = {random_int_two} and b = {random_int_one}, the value turned out to be ##a_minus_b_whole_squared_plus_4ab({random_int_two}, {random_int_one}).",
            f"In her relentless pursuit of mathematical truths, Claire embarked on a quest to understand the value of (a - b)^2, where a = {random_int_four} and b = {random_int_three}. The result was ##a_minus_b_whole_squared({random_int_four}, {random_int_three}).",
            f"Undeterred by complexity, Claire sought to fathom the intricacies of (a^2 - 2ab + b^2), for a = {random_int_one} and b = {random_int_three}. The outcome was ##a_squared_minus_2ab_plus_b_squared({random_int_one}, {random_int_three}).",
            f"Amidst her mathematical odyssey, Claire pondered the mysteries of (a + b)^2 - 4ab. With a = {random_int_three} and b = {random_int_four}, she discovered the result to be ##a_plus_b_whole_squared_minus_4ab({random_int_three}, {random_int_four}).",
            f"As the sun began to set, Claire marveled at the beauty of mathematical patterns. In her contemplation, she realized that (a^2 + b^2) represented a unique sum, where a = {random_int_two} and b = {random_int_one}. The value was ##a_squared_plus_b_squared({random_int_two}, {random_int_one}).",
            f"With her heart full of mathematical wonder, Claire returned home, carrying the knowledge of binomial expansions and their intricate forms.",
            f"And so, the tale of Claire's mathematical journey became a legend, inspiring generations of mathematicians to explore the boundless realm of algebraic expressions.",
        ],
        [
            f"Deep within the realm of equations and algebraic expressions, lived a mathematician named Ethan. Ethan was known for his boundless curiosity and passion for solving complex mathematical puzzles.",
            f"One day, as Ethan walked through the forest of numbers, he stumbled upon an equation involving the term -2ab. With a = {random_int_two} and b = {random_int_one}, he calculated ##negative_2ab({random_int_two}, {random_int_one}).",
            f"Energized by his discovery, Ethan continued his journey by exploring the realm of positive 2ab. For a = {random_int_three} and b = {random_int_two}, he found ##positive_2ab({random_int_three}, {random_int_two}).",
            f"As the sun set, Ethan's path led him to an expression involving x and coefficients. He solved the equation (x + a) * (x + b), with x = {random_int_four}, a = {random_int_two}, and b = {random_int_three}. The result was ##x_plus_a_times_x_plus_b({random_int_four}, {random_int_two}, {random_int_three}).",
            f"In the heart of the mathematical forest, Ethan encountered a complex expression: x^2 + (a + b) * (x + ab), with x = {random_int_one}, a = {random_int_three}, and b = {random_int_four}. He unveiled the value of ##x_squared_plus_a_plus_b_times_x_plus_ab({random_int_one}, {random_int_three}, {random_int_four}).",
            f"As Ethan journeyed further, he stumbled upon a mysterious artifact that held the secret to a_cubed + b_cubed. With a = {random_int_four} and b = {random_int_two}, he unlocked the value of ##a_cubed_plus_b_cubed({random_int_four}, {random_int_two}).",
            f"Along with newfound determination, Ethan took on the challenge of (a + b)^3 - 3ab * (a + b), where a = {random_int_three} and b = {random_int_one}. He solved the equation, revealing the answer as ##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({random_int_three}, {random_int_one}).",
            f"Guided by the mathematical energy of the forest, Ethan uncovered the hidden meaning of (a + b) * (a^2 - ab + b^2), where a = {random_int_four} and b = {random_int_three}. The solution was ##a_plus_b_times_a_squared_minus_ab_plus_b_squared({random_int_four}, {random_int_three}).",
            f"The forest of equations whispered secrets of a_cubed - b_cubed to Ethan's eager ears. With a = {random_int_two} and b = {random_int_one}, he revealed the enigma of ##a_cubed_minus_b_cubed({random_int_two}, {random_int_one}).",
            f"In the heart of the night, Ethan unlocked the final mystery: (a - b)^3 + 3ab * (a - b), with a = {random_int_three} and b = {random_int_two}. The equation yielded its secrets, and Ethan's calculations revealed ##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({random_int_three}, {random_int_two}).",
            f"Ethan emerged from the forest, having delved deep into the realm of equations and expressions. He had uncovered the magic within numbers and celebrated the beauty of mathematical exploration.",
            f"And so, the legend of Ethan's mathematical journey spread far and wide, inspiring generations of mathematicians to seek the hidden wonders of algebraic mysteries.",
        ],
    ]

    return random.choice(examples)


if __name__ == "__main__":
    masked_example = create_masked_token_batch_one_example(1, Utility.get_spacy_nlp())
    print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example, PretrainTasks.MASKED_TOKEN_PREDICTION
    )
    print(sample)
#
#     next_token_example = create_next_token_batch_one_example(1, Utility.get_spacy_nlp())
#     print(len(next_token_example), next_token_example)
