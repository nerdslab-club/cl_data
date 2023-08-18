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
    max_value_result = "what ?"
    lst = ", ".join(str(num) for num in lst_one)
    explanations = [
        f"The maximum value in the list {lst}",
        f"max_value({lst})",
        f"The result of finding the maximum value in {lst}",
        f"Calculation: max_value({lst})",
        f"The highest value among the elements in {lst}",
        f"The outcome of determining the maximum value in {lst}",
        f"The maximum value found in the list {lst}",
        f"The largest value among the numbers in {lst}",
        f"The computed result of finding the maximum value in {lst}",
        f"The value of the largest element in {lst}",
        f"The greatest value among the integers in {lst}",
        f"The maximum result obtained from the numbers in {lst}",
        f"The outcome of evaluating max_value({lst}) is",
        f"The value calculated by finding the maximum value in {lst}",
        f"The result of evaluating max_value({lst}) is",
        f"The maximum value in the list is {max_value_result}",
        f"The computed maximum value in the list is {max_value_result}",
        f"The largest number found in the list is {max_value_result}",
        f"The outcome of finding the largest value in the list {lst} is {max_value_result}",
        f"The highest value in the list is {max_value_result}",
        f"The result of finding the maximum value among {lst} is {max_value_result}",
        f"The maximum element in the list is {max_value_result}",
        f"The calculated outcome of evaluating max_value({lst}) is {max_value_result}",
        f"The greatest result obtained from the elements in {lst} is {max_value_result}",
        f"The largest value among the elements is {max_value_result}",
        f"The value of the maximum element in the list is {max_value_result}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_max_value_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
