import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2f_floor_example(count: int):
    examples = []
    for _ in range(count):
        num1 = RandomValueGenerator.generate_random_float()
        choice_one = __random_io_operation(num1)
        choice_two = __random_io_operation(num1, choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_operation(num1: float, prev_choice=None) -> str:
    explanations = [
        f"##floor({num1})",
        f"##subtraction(##ceil({num1}), 1)",
    ]

    if prev_choice is not None:
        explanations.remove(prev_choice)

    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2f_floor_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
