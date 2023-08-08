import random

from src.random_value_generator import RandomValueGenerator
from src.constants import TaskTypes
from src.utility import Utility


def create_f2f_average_example(count: int):
    examples = []
    for _ in range(count):
        list1 = RandomValueGenerator.generate_random_list()
        choice_one = __random_io(list1)
        choice_two = __random_io(list1, choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io(list1: list, prev_choice=None) -> str:
    explanations = [
        f"##average({list1})",
        f"##mean({list1})",
        f"##division(##sum({list1}),##length({list1}))",
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
            create_f2f_average_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
