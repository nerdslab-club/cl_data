import random
import math  # Import the math module for hyperbolic cosine function

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_hyperbolic_cosine_example(count: int):
    examples = []
    for _ in range(count):
        value = RandomValueGenerator.generate_random_float(-10, 10, round_to=2)  # Random value in a suitable range
        examples.append(
            {
                "inputStr": __random_explanation_hyperbolic_cosine(value),
                "outputStr": f"##hyperbolic_cosine({value})",
            }
        )
    return examples


def __random_explanation_hyperbolic_cosine(value: float) -> str:
    value = math.cosh(value)
    explanations = [
        f"Hyperbolic cosine of {value}",
        f"Cosh({value})",
        f"The hyperbolic cosine value for {value}",
        f"Calculate hyperbolic cosine for {value}",
        f"Hyperbolic cosine function applied to {value}",
        f"Cosh({value}), what is it?",
        f"The result of cosh({value})",
        f"Find the hyperbolic cosine of {value}",
        f"Hyperbolic cosine value when input is {value}",
        f"Input: {value}, hyperbolic cosine?",
        f"Hyperbolic cosine of {value}, tell me",
        f"Cosh({value}), the answer?",
        f"Calculate cosh({value})",
        f"The hyperbolic cosine for input {value}",
        f"What is cosh({value})?",
        f"Hyperbolic cosine of {value}, result?",
        f"Cosh({value}), find the value",
        f"The hyperbolic cosine value for input {value}",
        f"Hyperbolic cosine of input {value}, what does it give?",
        f"Find cosh({value})",
        f"Hyperbolic cosine function for input {value}",
        f"Hyperbolic cosine of {value}, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_hyperbolic_cosine_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
