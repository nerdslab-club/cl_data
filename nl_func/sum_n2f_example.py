import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_sum_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        numbers = RandomValueGenerator.generate_random_list()
        examples.append({
            "inputStr": __random_explanation(numbers, (None if identifier is None else identifier+i)),
            "outputStr": f"##sum({numbers})",
        })
    return examples


def __random_explanation(numbers: list, identifier: int | None) -> str:
    explanations = [
        f"Calculate the sum of the numbers {numbers}",
        f"Determine the result of the sum for the numbers {numbers}",
        f"Find the sum of the numbers {numbers}",
        f"The result of calculating the sum of the numbers {numbers}",
        f"Performing the sum calculation for the numbers {numbers}",
        f"The sum of the numbers {numbers}",
        f"The result after calculating the sum of the numbers {numbers}, what is it",
        f"The sum of the numbers {numbers}, what does it give",
        f"Let's calculate the sum of the numbers {numbers}",
        f"The sum of the numbers {numbers}, result is",
        f"Calculating the sum of the numbers {numbers}",
        f"The sum result after calculating sum for the numbers {numbers}",
        f"The sum of the numbers {numbers}, what is its value",
        f"Let's determine the sum of the numbers {numbers}",
        f"The sum of the numbers {numbers}, what is the result",
        f"The result after calculating the sum of the numbers {numbers}",
        f"The sum of the numbers {numbers}, what is it",
        f"Calculate the sum of the numbers {numbers}, find the answer",
        f"The sum of the numbers {numbers}, what does it give",
        f"Let's find the result after calculating the sum of the numbers {numbers}",
        f"The sum of the numbers {numbers}, what is the output",
        f"The result after calculating the sum of the numbers {numbers}, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_sum_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
