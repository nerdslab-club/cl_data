import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2f_hypotenuse_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i))
        num2 = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i+1))
        choice_one = __random_io_operation(num1, num2, (None if identifier is None else identifier+i))
        choice_two = __random_io_operation(num1, num2, (None if identifier is None else identifier+i), choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_operation(num1: float, num2: float, identifier: int | None, prev_choice=None) -> str:
    explanations = [
        f"##hypotenuse({num1}, {num2})",
        f"##square_root(##addition(##square({num1}), ##square({num2})))",
        f"##exponentiation(##addition(##exponentiation({num1}, 2), ##exponentiation({num2}, 2)), 0.5)",
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
            create_f2f_hypotenuse_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
