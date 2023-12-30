import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_median_example(count: int, max_list_length: int = 5):
    examples = []
    for _ in range(count):
        length = RandomValueGenerator.generate_random_integer(2, max_list_length + 1)
        numbers = RandomValueGenerator.generate_random_list(length, -10, 100)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##median({numbers})",
        })
    return examples


def __random_explanation(numbers: list) -> str:
    explanations = [
        f"Calculate the median of the numbers {numbers}",
        f"MEDIAN({numbers})",
        f"Find the median value for the list {numbers}",
        f"The result of MEDIAN({numbers})",
        f"Determine the median for the numbers {numbers}",
        f"Calculating the median for the numbers {numbers}",
        f"The median value of the numbers {numbers}",
        f"MEDIAN calculation: {numbers}",
        f"The median of the list {numbers}, what is it?",
        f"The median of the numbers {numbers}, what does it give?",
        f"Let's find the median of the numbers {numbers}",
        f"Find the MEDIAN for the list {numbers}",
        f"The median of the list {numbers}, result is",
        f"Calculating the median of the numbers {numbers}",
        f"The result of finding the median of the numbers {numbers}",
        f"The median of the list {numbers}, what is its value?",
        f"Let's determine the median of the numbers {numbers}",
        f"The median value of the numbers in the list: {numbers}",
        f"{numbers}, what is their median?",
        f"Finding the median of the numbers {numbers}",
        f"The median of the list {numbers}, what is its value?",
        f"Find the median of the numbers {numbers} and provide the result",
        f"MEDIAN({numbers}), what does it yield?",
        f"The median of the numbers {numbers}, ignoring order",
        f"The result of finding the median of the elements in the list {numbers}",
        f"The median value of the numbers {numbers}, what is it?",
        f"Calculate the median of the list {numbers}, find the answer",
        f"The median of the numbers {numbers}, what does it give?",
        f"Let's find the result of finding the median of the numbers {numbers}",
        f"{numbers}, their median, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_median_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
