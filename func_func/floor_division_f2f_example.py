import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2f_floor_division_example(count: int):
    examples = []
    for _ in range(count):
        num1 = RandomValueGenerator.generate_random_integer()
        num2 = RandomValueGenerator.generate_random_integer()
        choice_one = __random_io_floor_division(num1, num2)
        choice_two = __random_io_floor_division(num1, num2, choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_floor_division(num1: int, num2: int, prev_choice=None) -> str:
    explanations = [
        f"##floor_division({num1}, {num2})",
        f"##floor(##division({num1}, {num2}))",
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
            create_f2f_floor_division_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )