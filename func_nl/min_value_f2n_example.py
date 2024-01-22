import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_min_value_example(count: int):
    examples = []
    for _ in range(count):
        lst = [random.randint(-100, 100) for _ in range(random.randint(2, 10))]
        examples.append(
            {
                "inputStr": f"##min_value({lst})",
                "outputStr": __random_explanation_min_value(lst),
            }
        )
    return examples


def __random_explanation_min_value(vector: list[int]) -> str:
    lst_str = " , ".join(str(num) for num in vector)
    explanations = [
        f"The minimum value in the list {lst_str}",
        f"min_value({vector})",
        f"The result of finding the minimum value in {lst_str}",
        f"Calculation: min_value({vector})",
        f"The lowest value among the elements in {lst_str}",
        f"The outcome of determining the minimum value in {lst_str}",
        f"The minimum value found in the list {lst_str}",
        f"The smallest value among the numbers in {lst_str}",
        f"The computed result of finding the minimum value in {lst_str}",
        f"The value of the smallest element in {lst_str}",
        f"The least value among the integers in {lst_str}",
        f"The minimum result obtained from the numbers in {lst_str}",
        f"The outcome of evaluating min_value({vector}) is",
        f"The value calculated by finding the minimum value in {lst_str}",
        f"The result of evaluating min_value({vector}) is",
        f"The outcome of finding the smallest value in the list {lst_str} is",
        f"The result of finding the minimum value among {lst_str} is",
        f"The calculated outcome of evaluating min_value({vector}) is",
        f"The least result obtained from the elements in {lst_str} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_min_value_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
