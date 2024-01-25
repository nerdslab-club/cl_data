import random
import math  # Import the math module for hyperbolic sine function

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_hyperbolic_sine_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        value = RandomValueGenerator.generate_random_float(-10, 10, round_to=2)  # Random value in a suitable range
        examples.append(
            {
                "inputStr": __random_explanation_hyperbolic_sine(value, (None if identifier is None else identifier+i)),
                "outputStr": f"##hyperbolic_sine({value})",
            }
        )
    return examples


def __random_explanation_hyperbolic_sine(value: float, identifier: int | None) -> str:
    explanations = [
        f"Hyperbolic sine of {value}",
        f"Sinh({value})",
        f"The hyperbolic sine value for {value}",
        f"Calculate hyperbolic sine for {value}",
        f"Hyperbolic sine function applied to {value}",
        f"Sinh({value}), what is it?",
        f"The result of sinh({value})",
        f"Find the hyperbolic sine of {value}",
        f"Hyperbolic sine value when input is {value}",
        f"Input: {value}, hyperbolic sine?",
        f"Hyperbolic sine of {value}, tell me",
        f"Sinh({value}), the answer?",
        f"Calculate sinh({value})",
        f"The hyperbolic sine for input {value}",
        f"What is sinh({value})?",
        f"Hyperbolic sine of {value}, result?",
        f"Sinh({value}), find the value",
        f"The hyperbolic sine value for input {value}",
        f"Hyperbolic sine of input {value}, what does it give?",
        f"Find sinh({value})",
        f"Hyperbolic sine function for input {value}",
        f"Hyperbolic sine of {value}, what is the result?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_hyperbolic_sine_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
