import random
import math  # Import the math module for hyperbolic tangent function

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_n2f_hyperbolic_tangent_example(count: int):
    examples = []
    for _ in range(count):
        value = round(random.uniform(-10, 10), 2) # Random value in a suitable range
        examples.append(
            {
                "inputStr": __random_explanation_hyperbolic_tangent(value),
                "outputStr": f"##hyperbolic_tangent({value})",
            }
        )
    return examples


def __random_explanation_hyperbolic_tangent(value: float) -> str:
    result = math.tanh(value)
    explanations = [
        f"Hyperbolic tangent of {value}",
        f"Tanh({value})",
        f"The hyperbolic tangent value for {value}",
        f"Calculate hyperbolic tangent for {value}",
        f"Hyperbolic tangent function applied to {value}",
        f"Tanh({value}), what is it?",
        f"The result of tanh({value})",
        f"Find the hyperbolic tangent of {value}",
        f"Hyperbolic tangent value when input is {value}",
        f"Input: {value}, hyperbolic tangent?",
        f"Hyperbolic tangent of {value}, tell me",
        f"Tanh({value}), the answer?",
        f"Calculate tanh({value})",
        f"The hyperbolic tangent for input {value}",
        f"What is tanh({value})?",
        f"Hyperbolic tangent of {value}, result?",
        f"Tanh({value}), find the value",
        f"The hyperbolic tangent value for input {value}",
        f"Hyperbolic tangent of input {value}, what does it give?",
        f"Find tanh({value})",
        f"Hyperbolic tangent function for input {value}",
        f"Hyperbolic tangent of {value}, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_hyperbolic_tangent_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
