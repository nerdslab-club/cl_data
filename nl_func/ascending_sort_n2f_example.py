import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_ascending_sort_example(count: int, max_list_length: int = 5):
    examples = []
    for _ in range(count):
        length = RandomValueGenerator.generate_random_integer(2, max_list_length + 1)
        numbers = RandomValueGenerator.generate_random_list(length, -10, 100)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##ascending_sort({numbers})",
        })
    return examples


def __random_explanation(numbers: list) -> str:
    explanations = [
        f"Sort the list {numbers} in ascending order",
        f"ASCENDING_SORT({numbers})",
        f"Arrange the elements in {numbers} in ascending order",
        f"The result of sorting {numbers} in ascending order",
        f"Perform ascending sort on the list {numbers}",
        f"Sorting {numbers} in ascending order",
        f"The sorted version of {numbers} in ascending order",
        f"ASCENDING_SORT calculation: {numbers}",
        f"The result after arranging {numbers} in ascending order, what is it?",
        f"The sorted order of {numbers} in ascending fashion, what does it give?",
        f"Let's sort {numbers} in ascending order",
        f"Sort the list {numbers} in ascending order, result is",
        f"Calculating the ascending sort for {numbers}",
        f"The sorted result after sorting {numbers} in ascending order",
        f"The arrangement of {numbers} in ascending order, what is its value?",
        f"Let's determine the sorted order of {numbers} in ascending fashion",
        f"The sorted version of {numbers} in ascending order",
        f"Sort {numbers} in ascending order, what is the result?",
        f"The arrangement of {numbers} in ascending order, what does it give?",
        f"Sort {numbers} in ascending order and provide the result",
        f"ASCENDING_SORT({numbers}), what does it yield?",
        f"The sorted order of {numbers} in ascending fashion, ignoring order",
        f"The result after sorting {numbers} in ascending order",
        f"The arrangement of {numbers} in ascending order, what is it?",
        f"Calculate the ascending sort for {numbers}, find the answer",
        f"The sorted order of {numbers} in ascending fashion, what does it give?",
        f"Let's find the result after sorting {numbers} in ascending order",
        f"Sort {numbers} in ascending order, what is the output?",
        f"The sorted result after sorting {numbers} in ascending order, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_ascending_sort_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
