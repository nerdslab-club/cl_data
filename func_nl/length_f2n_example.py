import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2n_length_example(count: int):
    examples = []
    for _ in range(count):
        item = RandomValueGenerator.generate_random_integer(2, 10)
        numbers = [RandomValueGenerator.generate_random_integer(-100, 1000) for _ in range(item)]
        examples.append(
            {
                "inputStr": f"##length({numbers})",
                "outputStr": __random_explanation_length(numbers),
            }
        )
    return examples


def __random_explanation_length(lst: list) -> str:
    numbers = ", ".join(str(num) for num in lst)
    explanations = [
        f"The length (number of elements) of the list {numbers}",
        f"length({numbers})",
        f"The result of calculating the length of the list {numbers}",
        f"Calculation: length({numbers})",
        f"The number of elements in the list {numbers}",
        f"The outcome of finding the length of the list {numbers}",
        f"The count of elements in the list {numbers}",
        f"The result of determining the length of the list {numbers}",
        f"The computed result of calculating the length of the list {numbers}",
        f"The length of the given list {numbers}",
        f"The outcome of evaluating length({numbers})",
        f"The value obtained by calculating the length of the list {numbers}",
        f"The result of evaluating length({numbers})",
        f"The count of elements in the given list {numbers}",
        f"The computed length value of the list {numbers}",
        f"The number of items in the given list {numbers}",
        f"The calculated result of determining the length of the list {numbers}",
        f"The length (number of elements) of the list {numbers} is",
        f"The result derived from calculating the length of the list {numbers}",
        f"The computed count of elements in the list {numbers}",
        f"The calculated outcome of evaluating length({numbers})",
        f"The computed number of elements in the list {numbers}",
        f"The calculated length value of the list {numbers}",
        f"The calculated count of elements in the list {numbers}",
        f"The outcome of finding the count of elements in the list {numbers}",
        f"The calculated number of items in the list {numbers}",
        f"The calculated value of the length of the list {numbers}",
        f"The outcome of evaluating length({numbers})",
        f"The outcome of calculating the length value of the list {numbers}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_length_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
