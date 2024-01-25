import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2f_binary_to_decimal_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_binary_string()
        choice_one = __random_io_operation(num1, (None if identifier is None else identifier+i))
        choice_two = __random_io_operation(num1, (None if identifier is None else identifier+i), choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_operation(num1: str, identifier: int | None, prev_choice=None) -> str:
    explanations = [
        f"##binary_to_decimal('{num1}')",
        f"##binary_to_decimal(##decimal_to_binary(##binary_to_decimal('{num1}')))",
    ]

    if prev_choice is not None:
        explanations.remove(prev_choice)

    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2f_binary_to_decimal_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
