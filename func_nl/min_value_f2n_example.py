import random

from src.constants import TaskTypes
from src.utility import Utility


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


def __random_explanation_min_value(lst_one: list[int]) -> str:
    min_value_result = "what ?"
    lst = ", ".join(str(num) for num in lst_one)
    explanations = [
        f"The minimum value in the list {lst}",
        f"min_value({lst})",
        f"The result of finding the minimum value in {lst}",
        f"Calculation: min_value({lst})",
        f"The lowest value among the elements in {lst}",
        f"The outcome of determining the minimum value in {lst}",
        f"The minimum value found in the list {lst}",
        f"The smallest value among the numbers in {lst}",
        f"The computed result of finding the minimum value in {lst}",
        f"The value of the smallest element in {lst}",
        f"The least value among the integers in {lst}",
        f"The minimum result obtained from the numbers in {lst}",
        f"The outcome of evaluating min_value({lst}) is",
        f"The value calculated by finding the minimum value in {lst}",
        f"The result of evaluating min_value({lst}) is",
        f"The minimum value in the list is {min_value_result}",
        f"The computed minimum value in the list is {min_value_result}",
        f"The smallest number found in the list is {min_value_result}",
        f"The outcome of finding the smallest value in the list {lst} is {min_value_result}",
        f"The lowest value in the list is {min_value_result}",
        f"The result of finding the minimum value among {lst} is {min_value_result}",
        f"The minimum element in the list is {min_value_result}",
        f"The calculated outcome of evaluating min_value({lst}) is {min_value_result}",
        f"The least result obtained from the elements in {lst} is {min_value_result}",
        f"The smallest value among the elements is {min_value_result}",
        f"The value of the minimum element in the list is {min_value_result}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_min_value_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
