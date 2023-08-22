import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2f_square_minus_example(count: int):
    examples = []
    for _ in range(count):
        num1 = RandomValueGenerator.generate_random_integer()
        num2 = RandomValueGenerator.generate_random_integer()
        choice_one = __random_io_operation(num1, num2)
        choice_two = __random_io_operation(num1, num2, choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_operation(num1: int, num2: int, prev_choice=None) -> str:
    explanations = [
        f"##a_minus_b_whole_squared({num1}, {num2})",
        f"##a_squared_minus_2ab_plus_b_squared({num1}, {num2})",
        f"##a_plus_b_whole_squared_minus_4ab({num1}, {num2})",
    ]

    if prev_choice is not None:
        explanations.remove(prev_choice)

    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2f_square_minus_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
