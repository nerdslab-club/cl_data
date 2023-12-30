import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_descending_sort_example(count: int, max_list_length: int = 5):
    examples = []
    for _ in range(count):
        length = RandomValueGenerator.generate_random_integer(2, max_list_length + 1)
        numbers = RandomValueGenerator.generate_random_list(length, -10, 10)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##descending_sort({numbers})",
        })
    return examples


def __random_explanation(numbers: list) -> str:
    explanations = [
        f"Sort the list {numbers} in descending order",
        f"DESCENDING_SORT({numbers})",
        f"Arrange the elements in {numbers} in descending order",
        f"The result of sorting {numbers} in descending order",
        f"Perform descending sort on the list {numbers}",
        f"Sorting {numbers} in descending order",
        f"The sorted version of {numbers} in descending order",
        f"DESCENDING_SORT calculation: {numbers}",
        f"The result after arranging {numbers} in descending order, what is it?",
        f"The sorted order of {numbers} in descending fashion, what does it give?",
        f"Let's sort {numbers} in descending order",
        f"Sort the list {numbers} in descending order, result is",
        f"Calculating the descending sort for {numbers}",
        f"The sorted result after sorting {numbers} in descending order",
        f"The arrangement of {numbers} in descending order, what is its value?",
        f"Let's determine the sorted order of {numbers} in descending fashion",
        f"The sorted version of {numbers} in descending order",
        f"Sort {numbers} in descending order, what is the result?",
        f"The arrangement of {numbers} in descending order, what does it give?",
        f"Sort {numbers} in descending order and provide the result",
        f"DESCENDING_SORT({numbers}), what does it yield?",
        f"The sorted order of {numbers} in descending fashion, ignoring order",
        f"The result after sorting {numbers} in descending order",
        f"The arrangement of {numbers} in descending order, what is it?",
        f"Calculate the descending sort for {numbers}, find the answer",
        f"The sorted order of {numbers} in descending fashion, what does it give?",
        f"Let's find the result after sorting {numbers} in descending order",
        f"Sort {numbers} in descending order, what is the output?",
        f"The sorted result after sorting {numbers} in descending order, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_descending_sort_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
