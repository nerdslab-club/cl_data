import random
import math

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_get_e_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        e_value = math.e
        examples.append(
            {
                "inputStr": "##get_e()",
                "outputStr": __random_explanation_get_e(e_value, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_get_e(e_value, identifier: int | None) -> str:
    explanations = [
        "The mathematical constant e",
        "get_e()",
        "The value of e",
        "Calculation: get_e()",
        "The base of the natural logarithm",
        "The outcome of evaluating get_e()",
        "The well-known constant representing the base of the natural logarithm",
        "The result of obtaining the value of e",
        "The computed result of evaluating get_e()",
        "The constant e used in calculus and mathematics",
        "The outcome of calculating the value of e",
        "The value of the mathematical constant representing the base of the natural logarithm",
        "The numerical value of the constant e",
        "The result of evaluating get_e()",
        "The value of e approximated as",
        "The result derived from evaluating get_e()",
        "The well-known constant used to represent the base of the natural logarithm",
        "The value of the constant e is",
        "The computed value of e used in mathematics",
        "The result of determining the value of e",
        "The calculated result of get_e() is",
        "The well-known mathematical constant representing the base of the natural logarithm",
        "The numerical approximation of the constant e",
        "The value of e is commonly approximated as",
        "The calculated value of the mathematical constant e",
        "The constant e is approximately",
        "The value of e rounded to",
        "The calculated value of e is",
        "The outcome of evaluating get_e() is",
        "The outcome of calculating the constant e",
        "The outcome of evaluating get_e() is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_get_e_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
