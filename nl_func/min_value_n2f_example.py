import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_min_value_example(count: int):
    examples = []
    for _ in range(count):
        numbers = RandomValueGenerator.generate_random_list(5, 0, 100)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##min_value({numbers})",
        })
    return examples


def __random_explanation(numbers: list[int]) -> str:
    explanations = [
        f"Find the minimum value in the list {numbers}",
        f"MIN_VALUE({numbers})",
        f"Determine the smallest value in the list {numbers}",
        f"Find the minimum element in the list {numbers}",
        f"Locate the lowest value in the list {numbers}",
        f"Searching for the minimum value in the list {numbers}",
        f"MIN_VALUE calculation: {numbers}",
        f"The result after finding the minimum value in the list {numbers}, what is it?",
        f"The minimum value in the list {numbers}, what does it give?",
        f"Let's find the minimum value in the list {numbers}",
        f"The minimum value in the list {numbers}, result is",
        f"Searching for the smallest value in the list {numbers}",
        f"The minimum element after finding the minimum value in the list {numbers}",
        f"The smallest value in the list {numbers}, what is its value?",
        f"Let's determine the minimum value in the list {numbers}",
        f"The minimum value in the list {numbers}",
        f"The minimum value in the list {numbers}, what is the result?",
        f"The minimum value in the list {numbers}, what does it give?",
        f"The minimum value in the list {numbers} and provide the result",
        f"MIN_VALUE({numbers}), what does it yield?",
        f"The minimum value in the list {numbers}, ignoring order",
        f"The result after finding the minimum value in the list {numbers}",
        f"The minimum value in the list {numbers}, what is it?",
        f"Calculate the minimum value in the list {numbers}, find the answer",
        f"The minimum value in the list {numbers}, what does it give?",
        f"Let's find the result after finding the minimum value in the list {numbers}",
        f"The minimum value in the list {numbers}, what is the output?",
        f"The result after finding the minimum value in the list {numbers}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_min_value_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
