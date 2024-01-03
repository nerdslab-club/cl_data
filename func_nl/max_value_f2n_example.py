import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_max_value_example(count: int):
    examples = []
    for _ in range(count):
        lst = [random.randint(-100, 100) for _ in range(random.randint(2, 10))]
        examples.append(
            {
                "inputStr": f"##max_value({lst})",
                "outputStr": __random_explanation_max_value(lst),
            }
        )
    return examples


def __random_explanation_max_value(lst_one: list[int]) -> str:

    lst_str = ", ".join(str(num) for num in lst_one)
    explanations = [
        f"The maximum value in the list {lst_str}",
        f"max_value({lst_str})",
        f"The result of finding the maximum value in {lst_str}",
        f"Calculation: max_value({lst_str})",
        f"The highest value among the elements in {lst_str}",
        f"The outcome of determining the maximum value in {lst_str}",
        f"The maximum value found in the list {lst_str}",
        f"The largest value among the numbers in {lst_str}",
        f"The computed result of finding the maximum value in {lst_str}",
        f"The value of the largest element in {lst_str}",
        f"The greatest value among the integers in {lst_str}",
        f"The maximum result obtained from the numbers in {lst_str}",
        f"The outcome of evaluating max_value({lst_str}) is",
        f"The value calculated by finding the maximum value in {lst_str}",
        f"The result of evaluating max_value({lst_str}) is",
        f"The outcome of finding the largest value in the list {lst_str} is",
        f"The calculated outcome of evaluating max_value({lst_str}) is",
        f"The greatest result obtained from the elements in {lst_str} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_max_value_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
