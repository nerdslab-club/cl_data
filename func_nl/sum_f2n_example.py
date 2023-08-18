import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2n_sum_example(count: int):
    examples = []
    for _ in range(count):
        item = RandomValueGenerator.generate_random_integer(2, 10)
        numbers = [random.uniform(-100.0, 1000.0) for _ in range(item)]
        examples.append(
            {
                "inputStr": f"##sum({numbers})",
                "outputStr": __random_explanation_sum(numbers),
            }
        )
    return examples


def __random_explanation_sum(lst: list) -> str:
    numbers = ", ".join(str(num) for num in lst)
    explanations = [
        f"The sum of the numbers {numbers}",
        f"sum({numbers})",
        f"The result of calculating the sum of the numbers {numbers}",
        f"Calculation: sum({numbers})",
        f"The total value of the numbers {numbers}",
        f"The outcome of finding the sum of the numbers {numbers}",
        f"The summation value of the numbers {numbers}",
        f"The result of determining the sum of the numbers {numbers}",
        f"The computed result of calculating the sum of the numbers {numbers}",
        f"The sum of the given numbers {numbers}",
        f"The outcome of evaluating sum({numbers})",
        f"The value obtained by calculating the sum of the numbers {numbers}",
        f"The result of evaluating sum({numbers})",
        f"The summation of the given numbers {numbers}",
        f"The computed sum value of the numbers {numbers}",
        f"The total value of the given numbers {numbers}",
        f"The calculated result of determining the sum of the numbers {numbers}",
        f"The sum of the numbers {numbers} is",
        f"The result derived from calculating the sum of the numbers {numbers}",
        f"The computed summation value of the numbers {numbers}",
        f"The calculated outcome of evaluating sum({numbers})",
        f"The computed total value of the numbers {numbers}",
        f"The calculated sum value of the numbers {numbers}",
        f"The calculated summation value of the numbers {numbers}",
        f"The outcome of finding the summation value of the numbers {numbers}",
        f"The calculated total value of the numbers {numbers}",
        f"The calculated value of the sum of the numbers {numbers}",
        f"The outcome of evaluating sum({numbers})",
        f"The outcome of calculating the sum value of the numbers {numbers}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_sum_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
