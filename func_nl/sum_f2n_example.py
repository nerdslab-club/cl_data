import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_sum_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        numbers = RandomValueGenerator.generate_random_list()
        examples.append(
            {
                "inputStr": f"##sum({numbers})",
                "outputStr": __random_explanation_sum(numbers, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_sum(vector: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in vector)
    explanations = [
        f"The sum of the lst_str {lst_str}",
        f"The result of calculating the sum of the lst_str {lst_str}",
        f"Calculation: sum({lst_str})",
        f"The total value of the lst_str {lst_str}",
        f"The outcome of finding the sum of the lst_str {lst_str}",
        f"The summation value of the lst_str {lst_str}",
        f"The result of determining the sum of the lst_str {lst_str}",
        f"The computed result of calculating the sum of the lst_str {lst_str}",
        f"The sum of the given lst_str {lst_str}",
        f"The outcome of evaluating sum({lst_str})",
        f"The value obtained by calculating the sum of the lst_str {lst_str}",
        f"The result of evaluating sum({lst_str})",
        f"The summation of the given lst_str {lst_str}",
        f"The computed sum value of the lst_str {lst_str}",
        f"The total value of the given lst_str {lst_str}",
        f"The calculated result of determining the sum of the lst_str {lst_str}",
        f"The sum of the lst_str {lst_str} is",
        f"The result derived from calculating the sum of the lst_str {lst_str}",
        f"The computed summation value of the lst_str {lst_str}",
        f"The calculated outcome of evaluating sum({lst_str})",
        f"The computed total value of the lst_str {lst_str}",
        f"The calculated sum value of the lst_str {lst_str}",
        f"The calculated summation value of the lst_str {lst_str}",
        f"The outcome of finding the summation value of the lst_str {lst_str}",
        f"The calculated total value of the lst_str {lst_str}",
        f"The calculated value of the sum of the lst_str {lst_str}",
        f"The outcome of evaluating sum({lst_str})",
        f"The outcome of calculating the sum value of the lst_str {lst_str}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_sum_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
