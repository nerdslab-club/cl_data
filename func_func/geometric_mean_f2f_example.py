import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2f_geometric_mean_example(count: int):
    examples = []
    for _ in range(count):
        list_length = RandomValueGenerator.generate_random_integer(2, 10)
        list1 = RandomValueGenerator.generate_random_list(list_length)
        choice_one = __random_io_operation(list1)
        choice_two = __random_io_operation(list1, choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_operation(list1: list, prev_choice=None) -> str:
    explanations = [
        f"##geometric_mean({list1})",
        f"##exponentiation(##product({list1}), ##invert_number(##length({list1})))",
        f"##exponentiation(##product({list1}), ##division(1, ##length({list1})))",
    ]

    if prev_choice is not None:
        explanations.remove(prev_choice)

    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2f_geometric_mean_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
