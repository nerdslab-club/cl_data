import random
import math

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_logarithm_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(1.0, 1000.0)
        base = random.uniform(2.0, 10.0)
        examples.append(
            {
                "inputStr": f"##logarithm({x},{base})",
                "outputStr": __random_explanation_log(
                    x,
                    base,
                ),
            }
        )
    return examples


def __random_explanation_log(x: float, base: float) -> str:
    explanations = [
        f"The logarithm of {x} to the base {base}",
        f"log_{base}({x})",
        f"The result of taking the logarithm of {x} to the base {base}",
        f"Calculation: log_{base}({x})",
        f"The logarithm of {x} with base {base} is",
        f"The value of log_{base}({x})",
        f"The power to which {base} must be raised to get {x}",
        f"The logarithm of {x} with base {base} equals?",
        f"The exponent that produces {x} when {base} is raised to it",
        f"The logarithm with base {base} of {x}",
        f"The logarithm of {x} to the {base} base",
        f"The logarithm of {x} having base {base}",
        f"log_{base}({x}) is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_logarithm_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
