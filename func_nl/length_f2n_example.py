import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_length_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        vector = RandomValueGenerator.generate_random_list(seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": f"##length({vector})",
                "outputStr": __random_explanation_length(vector, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_length(vector: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in vector)
    explanations = [
        f"The length of the list {lst_str}",
        f"The result of calculating the length of the list {lst_str}",
        f"The number of elements in the list {lst_str}",
        f"The outcome of finding the length of the list {lst_str}",
        f"The count of elements in the list {lst_str}",
        f"The result of determining the length of the list {lst_str}",
        f"The computed result of calculating the length of the list {lst_str}",
        f"The length of the given list {lst_str}",
        f"The value obtained by calculating the length of the list {lst_str}",
        f"The count of elements in the given list {lst_str}",
        f"The computed length value of the list {lst_str}",
        f"The number of items in the given list {lst_str}",
        f"The calculated result of determining the length of the list {lst_str}",
        f"The length (number of elements) of the list {lst_str} is",
        f"The result derived from calculating the length of the list {lst_str}",
        f"The computed count of elements in the list {lst_str}",
        f"The calculated outcome of evaluating length({vector})",
        f"The computed number of elements in the list {lst_str}",
        f"The calculated length value of the list {lst_str}",
        f"The calculated count of elements in the list {lst_str}",
        f"The outcome of finding the count of elements in the list {lst_str}",
        f"The calculated number of items in the list {lst_str}",
        f"The calculated value of the length of the list {lst_str}",
        f"The outcome of evaluating length({vector})",
        f"The outcome of calculating the length value of the list {lst_str}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_length_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
