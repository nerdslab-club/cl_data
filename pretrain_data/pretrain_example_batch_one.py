import random

from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_pretrain_batch_one_example(count: int):
    examples = []
    for _ in range(count):
        example = __get_batch_one_example_pair()
        examples.append({
            "rawInputStr": example
        })
    return examples



def __get_batch_one_example_pair():
    random_int_one = RandomValueGenerator.generate_random_integer()
    random_int_two = random_int_one + RandomValueGenerator.generate_random_integer()
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer()
    random_int_four = RandomValueGenerator.generate_random_integer()
    random_float = RandomValueGenerator.generate_random_float()
    random_bool = RandomValueGenerator.generate_random_boolean()
    random_list = Utility.remove_spaces(str(RandomValueGenerator.generate_random_list()))

    examples = [[
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
        f"And so, the legend of Alex, the mathematical adventurer, spread far and wide, inspiring others to embrace the magic of numbers."
    ]]

    return random.choice(examples)
