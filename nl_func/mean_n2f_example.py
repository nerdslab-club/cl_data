import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_mean_example(count: int, max_list_length: int = 5):
    examples = []
    for _ in range(count):
        length = RandomValueGenerator.generate_random_integer(2, max_list_length + 1)
        numbers = RandomValueGenerator.generate_random_list(length, -10, 100)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##mean({numbers})",
        })
    return examples


def __random_explanation(numbers: list) -> str:
    explanations = [
        f"Calculate the mean of the numbers {numbers}",
        f"MEAN({numbers})",
        f"Find the average of the numbers {numbers}",
        f"The result of MEAN({numbers})",
        f"Determine the mean value for the list {numbers}",
        f"Calculating the mean for the numbers {numbers}",
        f"The average value of the numbers {numbers}",
        f"MEAN calculation: {numbers}",
        f"The mean of the list {numbers}, what is it?",
        f"The mean of the numbers {numbers}, what does it give?",
        f"Let's find the mean of the numbers {numbers}",
        f"Find the MEAN for the list {numbers}",
        f"The mean of the list {numbers}, result is",
        f"Calculating the average of the numbers {numbers}",
        f"The result of averaging the numbers {numbers}",
        f"The mean of the list {numbers}, what is its value?",
        f"Let's determine the mean of the numbers {numbers}",
        f"The average value of the numbers in the list: {numbers}",
        f"{numbers}, what is their mean?",
        f"Finding the mean of the numbers {numbers}",
        f"The mean of the list {numbers}, what is its value?",
        f"Find the average of the numbers {numbers} and provide the result",
        f"MEAN({numbers}), what does it yield?",
        f"The mean of the numbers {numbers}, ignoring order",
        f"The result of averaging the elements in the list {numbers}",
        f"The average value of the numbers {numbers}, what is it?",
        f"Calculate the mean of the list {numbers}, find the answer",
        f"The mean of the numbers {numbers}, what does it give?",
        f"Let's find the result of averaging the numbers {numbers}",
        f"{numbers}, their mean, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_mean_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
