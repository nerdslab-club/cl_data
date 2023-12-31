import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_average_example(count: int):
    examples = []
    for _ in range(count):
        numbers = RandomValueGenerator.generate_random_list(3, -10, 10)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##average({numbers})",
        })
    return examples


def __random_explanation(numbers: list) -> str:
    explanations = [
        f"Calculate the average of the numbers {numbers}",
        f"AVERAGE({numbers})",
        f"Determine the result of the average for the numbers {numbers}",
        f"Find the average of the numbers {numbers}",
        f"The result of calculating the average of the numbers {numbers}",
        f"Performing the average calculation for the numbers {numbers}",
        f"The average of the numbers {numbers}",
        f"AVERAGE calculation: {numbers}",
        f"The result after calculating the average of the numbers {numbers}, what is it?",
        f"The average of the numbers {numbers}, what does it give?",
        f"Let's calculate the average of the numbers {numbers}",
        f"The average of the numbers {numbers}, result is",
        f"Calculating the average of the numbers {numbers}",
        f"The average result after calculating average for the numbers {numbers}",
        f"The average of the numbers {numbers}, what is its value?",
        f"Let's determine the average of the numbers {numbers}",
        f"The average of the numbers {numbers}",
        f"The average of the numbers {numbers}, what is the result?",
        f"The average of the numbers {numbers}, what does it give?",
        f"The average of the numbers {numbers} and provide the result",
        f"AVERAGE({numbers}), what does it yield?",
        f"The average of the numbers {numbers}, ignoring order",
        f"The result after calculating the average of the numbers {numbers}",
        f"The average of the numbers {numbers}, what is it?",
        f"Calculate the average of the numbers {numbers}, find the answer",
        f"The average of the numbers {numbers}, what does it give?",
        f"Let's find the result after calculating the average of the numbers {numbers}",
        f"The average of the numbers {numbers}, what is the output?",
        f"The result after calculating the average of the numbers {numbers}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_average_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
