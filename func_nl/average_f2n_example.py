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
    lst_str = ", ".join(str(num) for num in lst)
    explanations = [
        f"The average (mean) of the lst_str {lst_str}",
        f"average({lst_str})",
        f"The result of calculating the average of the lst_str {lst_str}",
        f"Calculation: average({lst_str})",
        f"The mean value of the lst_str {lst_str}",
        f"The outcome of finding the average of the lst_str {lst_str}",
        f"The arithmetic mean value of the lst_str {lst_str}",
        f"The result of determining the average of the lst_str {lst_str}",
        f"The computed result of calculating the average of the lst_str {lst_str}",
        f"The average (mean) of the given lst_str {lst_str}",
        f"The outcome of evaluating average({lst_str})",
        f"The value obtained by calculating the average of the lst_str {lst_str}",
        f"The result of evaluating average({lst_str})",
        f"The arithmetic mean of the given lst_str {lst_str}",
        f"The computed average value of the lst_str {lst_str}",
        f"The mean value of the given lst_str {lst_str}",
        f"The calculated result of determining the average of the lst_str {lst_str}",
        f"The average (mean) of the lst_str {lst_str} is",
        f"The result derived from calculating the average of the lst_str {lst_str}",
        f"The computed arithmetic mean of the lst_str {lst_str}",
        f"The calculated outcome of evaluating average({lst_str})",
        f"The computed mean value of the lst_str {lst_str}",
        f"The calculated average value of the lst_str {lst_str}",
        f"The calculated arithmetic mean of the lst_str {lst_str}",
        f"The outcome of finding the arithmetic mean of the lst_str {lst_str}",
        f"The calculated mean value of the lst_str {lst_str}",
        f"The calculated value of the average of the lst_str {lst_str}",
        f"The outcome of evaluating average({lst_str})",
        f"The outcome of calculating the average value of the lst_str {lst_str}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_average_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
