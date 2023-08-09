import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2f_exponentiation_example(count: int):
    examples = []
    for _ in range(count):
        num1 = RandomValueGenerator.generate_random_integer(1, 1000)
        choice_one = __random_io_exponentiation(num1)
        choice_two = __random_io_exponentiation(num1, choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_exponentiation(num1: int, prev_choice=None) -> str:
    explanations = [
        f"##exponentiation({num1}, 3)",
        f"##cube({num1})",
    ]
    if prev_choice is None:
        return random.choice(explanations)
    new_choice = random.choice(explanations)
    while new_choice == prev_choice:
        new_choice = random.choice(explanations)
    return new_choice


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2f_exponentiation_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
