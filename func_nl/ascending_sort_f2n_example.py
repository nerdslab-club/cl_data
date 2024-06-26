import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_ascending_sort_example(count: int):
    examples = []
    for _ in range(count):
        lst_len = random.randint(3, 6)  # Generate a list of 3 to 6 numbers
        lst = [random.randint(-100, 100) for _ in range(lst_len)]
        examples.append(
            {
                "inputStr": f"##ascending_sort({lst})",
                "outputStr": __random_explanation_ascending_sort(lst),
            }
        )
    return examples


def __random_explanation_ascending_sort(lst: list) -> str:
    lst_str = ", ".join(str(num) for num in lst)
    explanations = [
        f"The list {lst_str} sorted in ascending order",
        f"ascending_sort({lst_str})",
        f"The sorted version of the list {lst_str}",
        f"Calculation: ascending_sort({lst_str})",
        f"The list {lst_str} arranged in increasing order",
        f"The outcome of sorting the elements in the list {lst_str}",
        f"The result of arranging the numbers in {lst_str} in ascending order",
        f"The list {lst_str} organized in ascending sequence",
        f"The sorted list of numbers {lst_str}",
        f"The list {lst_str} sorted from least to greatest",
        f"The result of sorting the elements of the list {lst_str}",
        f"The computed result of sorting {lst_str} in ascending order",
        f"The result of evaluating ascending_sort({lst_str})",
        f"The ordered sequence of numbers in the list {lst_str}",
        f"The outcome of arranging the elements {lst_str} in ascending order",
        f"The list {lst_str} in increasing order is",
        f"The list {lst_str} sorted in non-decreasing order",
        f"The sorted form of the list {lst_str}",
        f"The value of ascending_sort({lst_str}) is",
        f"The outcome of sorting the list {lst_str} is",
        f"The ordered arrangement of the numbers in the list {lst_str}",
        f"The sorted list of {lst_str} is",
        f"The computed sorted list of {lst_str} is",
        f"The ordered sequence obtained from sorting the list {lst_str} is",
        f"The ascending sorted list of {lst_str} is",
        f"The ordered form of the list {lst_str} is",
        f"The result of sorting the list {lst_str} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_ascending_sort_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
