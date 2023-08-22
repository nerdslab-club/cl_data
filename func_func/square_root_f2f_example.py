import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2f_square_root_example(count: int):
    examples = []
    for _ in range(count):
        num1 = RandomValueGenerator.generate_random_float()
        choice_one = __random_io_square_root(num1)
        choice_two = __random_io_square_root(num1, choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_square_root(num1: float, prev_choice=None) -> str:
    explanations = [
        f"##square_root({num1})",
        f"##exponentiation({num1}, 0.5)",
        f"##exponentiation({num1}, ##invert_number(2))",
        f"##invert_number(##exponentiation({num1}, -0.5))",
        f"##nth_root({num1}, 2)",
    ]
    if prev_choice is not None:
        explanations.remove(prev_choice)
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2f_square_root_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
