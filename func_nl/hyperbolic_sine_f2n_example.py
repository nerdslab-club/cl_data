import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_hyperbolic_sine_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float()
        examples.append(
            {
                "inputStr": f"##hyperbolic_sine({x})",
                "outputStr": __random_explanation_hyperbolic_sine(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_hyperbolic_sine(x: float, identifier: int | None) -> str:
    explanations = [
        f"The hyperbolic sine of {x}",
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
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_hyperbolic_sine_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
