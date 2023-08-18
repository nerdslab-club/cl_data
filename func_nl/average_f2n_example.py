import random

from src.constants import TaskTypes
from src.utility import Utility
from src.random_value_generator import RandomValueGenerator


def create_f2n_average_example(count: int):
    examples = []
    for _ in range(count):
        item = RandomValueGenerator.generate_random_integer(2, 10)
        numbers = [random.uniform(-10.0, 1000.0) for _ in range(item)]
        examples.append(
            {
                "inputStr": f"##average({numbers})",
                "outputStr": __random_explanation_average(numbers),
            }
        )
    return examples


def __random_explanation_average(lst: list) -> str:
    numbers = ", ".join(str(num) for num in lst)
    explanations = [
        f"The average (mean) of the numbers {numbers}",
        f"average({numbers})",
        f"The result of calculating the average of the numbers {numbers}",
        f"Calculation: average({numbers})",
        f"The mean value of the numbers {numbers}",
        f"The outcome of finding the average of the numbers {numbers}",
        f"The arithmetic mean value of the numbers {numbers}",
        f"The result of determining the average of the numbers {numbers}",
        f"The computed result of calculating the average of the numbers {numbers}",
        f"The average (mean) of the given numbers {numbers}",
        f"The outcome of evaluating average({numbers})",
        f"The value obtained by calculating the average of the numbers {numbers}",
        f"The result of evaluating average({numbers})",
        f"The arithmetic mean of the given numbers {numbers}",
        f"The computed average value of the numbers {numbers}",
        f"The mean value of the given numbers {numbers}",
        f"The calculated result of determining the average of the numbers {numbers}",
        f"The average (mean) of the numbers {numbers} is",
        f"The result derived from calculating the average of the numbers {numbers}",
        f"The computed arithmetic mean of the numbers {numbers}",
        f"The calculated outcome of evaluating average({numbers})",
        f"The computed mean value of the numbers {numbers}",
        f"The calculated average value of the numbers {numbers}",
        f"The calculated arithmetic mean of the numbers {numbers}",
        f"The outcome of finding the arithmetic mean of the numbers {numbers}",
        f"The calculated mean value of the numbers {numbers}",
        f"The calculated value of the average of the numbers {numbers}",
        f"The outcome of evaluating average({numbers})",
        f"The outcome of calculating the average value of the numbers {numbers}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_average_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
