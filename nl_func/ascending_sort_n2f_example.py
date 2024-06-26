import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_ascending_sort_example(count: int, max_list_length: int = 5):
    examples = []
    for _ in range(count):
        vector = RandomValueGenerator.generate_random_list(
            RandomValueGenerator.generate_random_integer(2, 10), -10, 100
        )
        examples.append({
            "inputStr": __random_explanation(vector),
            "outputStr": f"##ascending_sort({vector})",
        })
    return examples


def __random_explanation(vector: list) -> str:
    lst_str = ", ".join(str(num) for num in vector)
    explanations = [
        f"Sort the list {lst_str} in ascending order",
        f"ASCENDING_SORT({vector})",
        f"Arrange the elements in {lst_str} in ascending order",
        f"The result of sorting {lst_str} in ascending order",
        f"Perform ascending sort on the list {lst_str}",
        f"Sorting {lst_str} in ascending order",
        f"The sorted version of {lst_str} in ascending order",
        f"ASCENDING_SORT calculation: {lst_str}",
        f"The result after arranging {lst_str} in ascending order, what is it?",
        f"The sorted order of {lst_str} in ascending fashion, what does it give?",
        f"Let's sort {lst_str} in ascending order",
        f"Sort the list {lst_str} in ascending order, result is",
        f"Calculating the ascending sort for {lst_str}",
        f"The sorted result after sorting {lst_str} in ascending order",
        f"The arrangement of {lst_str} in ascending order, what is its value?",
        f"Let's determine the sorted order of {lst_str} in ascending fashion",
        f"The sorted version of {lst_str} in ascending order",
        f"Sort {lst_str} in ascending order, what is the result?",
        f"The arrangement of {lst_str} in ascending order, what does it give?",
        f"Sort {lst_str} in ascending order and provide the result",
        f"ASCENDING_SORT({vector}), what does it yield?",
        f"The sorted order of {lst_str} in ascending fashion, ignoring order",
        f"The result after sorting {lst_str} in ascending order",
        f"The arrangement of {lst_str} in ascending order, what is it?",
        f"Calculate the ascending sort for {lst_str}, find the answer",
        f"The sorted order of {lst_str} in ascending fashion, what does it give?",
        f"Let's find the result after sorting {lst_str} in ascending order",
        f"Sort {lst_str} in ascending order, what is the output?",
        f"The sorted result after sorting {lst_str} in ascending order, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_ascending_sort_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
