import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_descending_sort_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        lst_len = random.randint(3, 6)  # Generate a list of 3 to 6 numbers
        lst = [random.randint(-100, 100) for _ in range(lst_len)]
        examples.append(
            {
                "inputStr": f"##descending_sort({lst})",
                "outputStr": __random_explanation_descending_sort(lst, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_descending_sort(lst: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in lst)
    explanations = [
        f"The list {lst_str} sorted in descending order",
        f"descending_sort({lst_str})",
        f"The sorted version of the list {lst_str} in descending order",
        f"Calculation: descending_sort({lst_str})",
        f"The list {lst_str} arranged in decreasing order",
        f"The outcome of sorting the elements in the list {lst_str} in descending order",
        f"The result of arranging the numbers in {lst_str} in descending order",
        f"The list {lst_str} organized in descending sequence",
        f"The sorted list of numbers {lst_str} in descending order",
        f"The list {lst_str} sorted from greatest to least",
        f"The result of sorting the elements of the list {lst_str} in descending order",
        f"The computed result of sorting {lst_str} in descending order",
        f"The result of evaluating descending_sort({lst_str})",
        f"The ordered sequence of numbers in the list {lst_str} in descending order",
        f"The outcome of arranging the elements {lst_str} in descending order",
        f"The list {lst_str} in decreasing order is",
        f"The list {lst_str} sorted in non-increasing order",
        f"The sorted form of the list {lst_str} in descending order",
        f"The value of descending_sort({lst_str}) is",
        f"The outcome of sorting the list {lst_str} in descending order is",
        f"The ordered arrangement of the numbers in the list {lst_str} in descending order",
        f"The sorted list of {lst_str} in descending order is",
        f"The computed sorted list of {lst_str} in descending order is",
        f"The ordered sequence obtained from sorting the list {lst_str} in descending order is",
        f"The descending sorted list of {lst_str} is",
        f"The ordered form of the list {lst_str} in descending order is",
        f"The result of sorting the list {lst_str} in descending order is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_descending_sort_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
