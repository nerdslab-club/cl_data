import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2f_hypotenuse_example(count: int):
    examples = []
    for _ in range(count):
        num1 = RandomValueGenerator.generate_random_integer(1, 100)
        num2 = RandomValueGenerator.generate_random_integer(1, 100)
        choice_one = __random_io_operation(num1, num2)
        choice_two = __random_io_operation(num1, num2, choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_operation(num1: float, num2: float, prev_choice=None) -> str:
    explanations = [
        f"##hypotenuse({num1}, {num2})",
        f"##square_root(##addition(##square({num1}), ##square({num2})))",
        f"##exponentiation(##addition(##exponentiation({num1}, 2), ##exponentiation({num2}, 2)), 0.5)",
    ]

    if prev_choice is not None:
        explanations.remove(prev_choice)

    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2f_hypotenuse_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
