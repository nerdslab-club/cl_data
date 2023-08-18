import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_hyperbolic_sine_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##hyperbolic_sine({x})",
                "outputStr": __random_explanation_hyperbolic_sine(x),
            }
        )
    return examples


def __random_explanation_hyperbolic_sine(x: float) -> str:
    explanations = [
        f"The hyperbolic sine of {x}",
        f"hyperbolic_sine({x})",
        f"The value of the hyperbolic sine function for {x}",
        f"Calculation: hyperbolic_sine({x})",
        f"The hyperbolic sine value for {x} is",
        f"The result of applying the hyperbolic sine function to {x}",
        f"The hyperbolic function corresponding to {x}",
        f"The value of the hyperbolic function at {x}",
        f"The hyperbolic function applied to the input {x}",
        f"The value of sinh({x})",
        f"The hyperbolic function evaluated at {x}",
        f"The hyperbolic function output for {x}",
        f"The result of the hyperbolic sine function at {x}",
        f"The value of the sinh function for the input {x}",
        f"The hyperbolic sine of the input {x}",
        f"The value of the hyperbolic_sine function at {x}",
        f"The sinh function output for {x}",
        f"The hyperbolic sine value of {x}",
        f"The value of the hyperbolic_sine function for the input {x}",
        f"The value of the hyperbolic_sine function evaluated at {x}",
        f"The value of sinh(x) for the given input {x}",
        f"The hyperbolic sine function value for {x}",
        f"The value of sinh(x) at the input {x}",
        f"The hyperbolic function value for the input {x}",
        f"The value of the hyperbolic sine function at {x} is",
        f"The sinh value for {x}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_hyperbolic_sine_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
