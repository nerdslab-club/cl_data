import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_descending_sort_example(count: int, identifier: int | None, max_list_length: int = 5):
    examples = []
    for i in range(count):
        numbers = RandomValueGenerator.generate_random_list(seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(numbers, (None if identifier is None else identifier+i)),
            "outputStr": f"##descending_sort({numbers})",
        })
    return examples


def __random_explanation(vector: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in vector)
    explanations = [
        f"Sort the list {lst_str} in descending order",
        f"Arrange the elements in {lst_str} in descending order",
        f"The result of sorting {lst_str} in descending order",
        f"Perform descending sort on the list {lst_str}",
        f"Sorting {lst_str} in descending order",
        f"The sorted version of {lst_str} in descending order",
        f"Let's sort {lst_str} in descending order",
        f"Sort the list {lst_str} in descending order, result is",
        f"Calculating the descending sort for {lst_str}",
        f"The sorted result after sorting {lst_str} in descending order",
        f"Let's determine the sorted order of {lst_str} in descending fashion",
        f"The sorted version of {lst_str} in descending order",
        f"Sort {lst_str} in descending order and provide the result",
        f"The sorted order of {lst_str} in descending fashion, ignoring order",
        f"The result after sorting {lst_str} in descending order",
        f"Calculate the descending sort for {lst_str}, find the answer",
        f"Let's find the result after sorting {lst_str} in descending order",
        f"Sort {lst_str} in descending order, what is the output",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_descending_sort_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
