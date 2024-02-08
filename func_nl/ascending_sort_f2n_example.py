import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_ascending_sort_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        lst = RandomValueGenerator.generate_random_list(seed=(None if identifier is None else identifier+i))
        examples.append(
            {
                "inputStr": f"##ascending_sort({lst})",
                "outputStr": __random_explanation_ascending_sort(lst, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_ascending_sort(lst: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in lst)
    explanations = [
        f"The list {lst_str} sorted in ascending order",
        f"The sorted version of the list {lst_str}",
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
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_ascending_sort_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
