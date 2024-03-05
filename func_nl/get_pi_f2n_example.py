import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_get_pi_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        examples.append(
            {
                "inputStr": "##get_pi()",
                "outputStr": __random_explanation_get_pi((None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_get_pi(identifier: int | None) -> str:
    explanations = [
        "The mathematical constant pi",
        "get_pi()",
        "The value of pi (π)",
        "Calculation: get_pi()",
        "The ratio of a circle's circumference to its diameter",
        "The outcome of evaluating get_pi()",
        "The well-known constant representing the circle's ratio of circumference to diameter",
        "The result of obtaining the value of pi (π)",
        "The computed result of evaluating get_pi()",
        "The constant pi (π) used in geometry and mathematics",
        "The outcome of calculating the value of pi (π)",
        "The value of the mathematical constant representing the circle's ratio",
        "The numerical value of the constant pi (π)",
        "The result of evaluating get_pi()",
        "The value of pi (π) approximated as",
        "The result derived from evaluating get_pi()",
        "The well-known constant used to represent the ratio of a circle's circumference to its diameter",
        "The value of the constant pi (π) is",
        "The computed value of pi (π) used in mathematics",
        "The result of determining the value of pi (π)",
        "The calculated result of get_pi() is",
        "The well-known mathematical constant representing the ratio of a circle's circumference to its diameter",
        "The numerical approximation of the constant pi (π)",
        "The value of pi (π) is commonly approximated as",
        "The calculated value of the mathematical constant pi (π)",
        "The constant pi (π) is approximately",
        "The value of pi (π) rounded to",
        "The calculated value of pi (π) is",
        "The outcome of evaluating get_pi() is",
        "The outcome of calculating the constant pi (π)",
        "The outcome of evaluating get_pi() is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_get_pi_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
