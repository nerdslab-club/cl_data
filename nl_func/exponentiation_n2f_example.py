import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_exponentiation_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_float()
        num2 = RandomValueGenerator.generate_random_float()
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
                "outputStr": f"##exponentiation({num1},{num2})",
            }
        )
    return examples


def __random_explanation(f1: float, f2: int, identifier: int | None) -> str:
    explanations = [
        f"Raising {f1} to the power of {f2}",
        f"{f1} raised to the power of {f2}",
        f"{f1} to the power of {f2}",
        f"{f1} exponentiated by {f2}",
        f"The result of {f1} raised to {f2}",
        f"{f1} raised to {f2}, what is it",
        f"Calculation: {f1} ** {f2}",
        f"{f1} raised to {f2}, equals",
        f"Taking {f1} and exponentiating by {f2}",
        f"{f1} raised to {f2}, the answer",
        f"{f1} to the power of {f2}, find the result",
        f"{f1} and {f2} exponentiation",
        f"The exponentiation of {f1} and {f2}",
        f"{f1} raised to {f2} is",
        f"{f1} raised to {f2} is equal to",
        f"{f1} and {f2} exponentiated, the result",
        f"Exponentiation: {f1} ** {f2}",
        f"Let's raise {f1} to the power of {f2}",
        f"Find the result of {f1} raised to {f2}",
        f"{f1} and {f2}, their exponentiation",
        f"{f1} raised to {f2}, result is",
        f"{f1} and {f2}, what will be the result",
        f"Exponentiation: {f1} ** {f2}, what is it",
        f"{f1} raised to {f2}, result",
        f"{f1} exponentiated by {f2}, the outcome",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_exponentiation_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
