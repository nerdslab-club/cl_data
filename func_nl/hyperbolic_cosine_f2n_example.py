import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_hyperbolic_cosine_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##hyperbolic_cosine({x})",
                "outputStr": __random_explanation_hyperbolic_cosine(x),
            }
        )
    return examples


def __random_explanation_hyperbolic_cosine(x: float) -> str:
    explanations = [
        f"The hyperbolic cosine of {x}",
        f"hyperbolic_cosine({x})",
        f"The value of the hyperbolic cosine function for {x}",
        f"Calculation: hyperbolic_cosine({x})",
        f"The hyperbolic cosine value for {x} is",
        f"The result of applying the hyperbolic cosine function to {x}",
        f"The hyperbolic function corresponding to {x}",
        f"The value of the hyperbolic function at {x}",
        f"The hyperbolic function applied to the input {x}",
        f"The value of cosh({x})",
        f"The hyperbolic function evaluated at {x}",
        f"The hyperbolic function output for {x}",
        f"The result of the hyperbolic cosine function at {x}",
        f"The value of the cosh function for the input {x}",
        f"The hyperbolic cosine of the input {x}",
        f"The value of the hyperbolic_cosine function at {x}",
        f"The cosh function output for {x}",
        f"The hyperbolic cosine value of {x}",
        f"The value of the hyperbolic_cosine function for the input {x}",
        f"The value of the hyperbolic_cosine function evaluated at {x}",
        f"The value of cosh(x) for the given input {x}",
        f"The hyperbolic cosine function value for {x}",
        f"The value of cosh(x) at the input {x}",
        f"The hyperbolic function value for the input {x}",
        f"The value of the hyperbolic cosine function at {x} is",
        f"The cosh value for {x}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_hyperbolic_cosine_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
