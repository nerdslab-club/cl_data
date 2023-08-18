import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_logarithm_base_10_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(0.1, 100.0)
        examples.append(
            {
                "inputStr": f"##logarithm_base_10({x})",
                "outputStr": __random_explanation_logarithm_base_10(x),
            }
        )
    return examples


def __random_explanation_logarithm_base_10(x: float) -> str:
    explanations = [
        f"The base-10 logarithm of {x}",
        f"logarithm_base_10({x})",
        f"The value of the base-10 logarithm function for {x}",
        f"Calculation: logarithm_base_10({x})",
        f"The base-10 logarithm value for {x} is",
        f"The result of applying the base-10 logarithm function to {x}",
        f"The logarithm corresponding to base 10 for {x}",
        f"The value of the logarithm function with base 10 at {x}",
        f"The logarithm function with base 10 applied to the input {x}",
        f"The value of log10({x})",
        f"The logarithm function with base 10 evaluated at {x}",
        f"The logarithm function output for {x}",
        f"The result of the base-10 logarithm function at {x}",
        f"The value of the logarithm function with base 10 for the input {x}",
        f"The base-10 logarithm of the input {x}",
        f"The value of the logarithm_base_10 function at {x}",
        f"The base-10 log value for {x}",
        f"The value of the logarithm_base_10 function for the input {x}",
        f"The value of the logarithm_base_10 function evaluated at {x}",
        f"The value of log10(x) for the given input {x}",
        f"The base-10 logarithm function value for {x}",
        f"The value of log10(x) at the input {x}",
        f"The logarithm function value for the input {x}",
        f"The value of the logarithm_base_10 function at {x} is",
        f"The log10 value for {x}",
        f"The output of the base-10 logarithm function at {x}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_logarithm_base_10_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
