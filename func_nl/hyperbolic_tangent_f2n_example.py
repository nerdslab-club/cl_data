import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_hyperbolic_tangent_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##hyperbolic_tangent({x})",
                "outputStr": __random_explanation_hyperbolic_tangent(x),
            }
        )
    return examples


def __random_explanation_hyperbolic_tangent(x: float) -> str:
    explanations = [
        f"The hyperbolic tangent of {x}",
        f"hyperbolic_tangent({x})",
        f"The value of the hyperbolic tangent function for {x}",
        f"Calculation: hyperbolic_tangent({x})",
        f"The hyperbolic tangent value for {x} is",
        f"The result of applying the hyperbolic tangent function to {x}",
        f"The hyperbolic function corresponding to {x}",
        f"The value of the hyperbolic function at {x}",
        f"The hyperbolic function applied to the input {x}",
        f"The value of tanh({x})",
        f"The hyperbolic function evaluated at {x}",
        f"The hyperbolic function output for {x}",
        f"The result of the hyperbolic tangent function at {x}",
        f"The value of the tanh function for the input {x}",
        f"The hyperbolic tangent of the input {x}",
        f"The value of the hyperbolic_tangent function at {x}",
        f"The tanh function output for {x}",
        f"The hyperbolic tangent value of {x}",
        f"The value of the hyperbolic_tangent function for the input {x}",
        f"The value of the hyperbolic_tangent function evaluated at {x}",
        f"The value of tanh(x) for the given input {x}",
        f"The hyperbolic tangent function value for {x}",
        f"The value of tanh(x) at the input {x}",
        f"The hyperbolic function value for the input {x}",
        f"The value of the hyperbolic tangent function at {x} is",
        f"The tanh value for {x}",
        f"The output of the hyperbolic tangent function at {x}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_hyperbolic_tangent_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
