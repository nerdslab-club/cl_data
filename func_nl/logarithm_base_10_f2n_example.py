import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_logarithm_base_10_example(count: int):
    examples = []
    for _ in range(count):
        m = random.uniform(0.1, 100.0)
        examples.append(
            {
                "inputStr": f"##logarithm_base_10({m})",
                "outputStr": __random_explanation_logarithm_base_10(m),
            }
        )
    return examples


def __random_explanation_logarithm_base_10(m: float) -> str:
    explanations = [
        f"The base-10 logarithm of {m}",
        f"logarithm_base_10({m})",
        f"The value of the base-10 logarithm function for {m}",
        f"Calculation: logarithm_base_10({m})",
        f"The base-10 logarithm value for {m} is",
        f"The result of applying the base-10 logarithm function to {m}",
        f"The logarithm corresponding to base 10 for {m}",
        f"The value of the logarithm function with base 10 at {m}",
        f"The logarithm function with base 10 applied to the input {m}",
        f"The value of log10({m})",
        f"The logarithm function with base 10 evaluated at {m}",
        f"The logarithm function output for {m}",
        f"The result of the base-10 logarithm function at {m}",
        f"The value of the logarithm function with base 10 for the input {m}",
        f"The base-10 logarithm of the input {m}",
        f"The value of the logarithm_base_10 function at {m}",
        f"The base-10 log value for {m}",
        f"The value of the logarithm_base_10 function for the input {m}",
        f"The value of the logarithm_base_10 function evaluated at {m}",
        f"The value of log10(x) for the given input {m}",
        f"The base-10 logarithm function value for {m}",
        f"The value of log10(x) at the input {m}",
        f"The logarithm function value for the input {m}",
        f"The value of the logarithm_base_10 function at {m} is",
        f"The log10 value for {m}",
        f"The output of the base-10 logarithm function at {m}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_logarithm_base_10_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
