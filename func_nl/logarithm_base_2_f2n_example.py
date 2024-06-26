import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_logarithm_base_2_example(count: int):
    examples = []
    for _ in range(count):
        m = random.uniform(0.1, 100.0)
        examples.append(
            {
                "inputStr": f"##logarithm_base_2({m})",
                "outputStr": __random_explanation_logarithm_base_2(m),
            }
        )
    return examples


def __random_explanation_logarithm_base_2(m: float) -> str:
    explanations = [
        f"The base-2 logarithm of {m}",
        f"logarithm_base_2({m})",
        f"The value of the base-2 logarithm function for {m}",
        f"Calculation: logarithm_base_2({m})",
        f"The base-2 logarithm value for {m} is",
        f"The result of applying the base-2 logarithm function to {m}",
        f"The logarithm corresponding to base 2 for {m}",
        f"The value of the logarithm function with base 2 at {m}",
        f"The logarithm function with base 2 applied to the input {m}",
        f"The value of log2({m})",
        f"The logarithm function with base 2 evaluated at {m}",
        f"The logarithm function output for {m}",
        f"The result of the base-2 logarithm function at {m}",
        f"The value of the logarithm function with base 2 for the input {m}",
        f"The base-2 logarithm of the input {m}",
        f"The value of the logarithm_base_2 function at {m}",
        f"The base-2 log value for {m}",
        f"The value of the logarithm_base_2 function for the input {m}",
        f"The value of the logarithm_base_2 function evaluated at {m}",
        f"The value of log2(x) for the given input {m}",
        f"The base-2 logarithm function value for {m}",
        f"The value of log2(x) at the input {m}",
        f"The logarithm function value for the input {m}",
        f"The value of the logarithm_base_2 function at {m} is",
        f"The log2 value for {m}",
        f"The output of the base-2 logarithm function at {m}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_logarithm_base_2_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
