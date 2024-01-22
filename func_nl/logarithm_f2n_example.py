import random
import math

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_logarithm_example(count: int):
    examples = []
    for _ in range(count):
        m = random.uniform(1.0, 100.0)
        base = random.uniform(2.0, 10.0)
        examples.append(
            {
                "inputStr": f"##logarithm({m},{base})",
                "outputStr": __random_explanation_log(
                    m,
                    base,
                ),
            }
        )
    return examples


def __random_explanation_log(m: float, base: float) -> str:
    explanations = [
        f"The logarithm of {m} to the base {base}",
        f"log_{base}({m})",
        f"The result of taking the logarithm of {m} to the base {base}",
        f"Calculation: log_{base}({m})",
        f"The logarithm of {m} with base {base} is",
        f"The value of log_{base}({m})",
        f"The power to which {base} must be raised to get {m}",
        f"The logarithm of {m} with base {base} equals?",
        f"The exponent that produces {m} when {base} is raised to it",
        f"The logarithm with base {base} of {m}",
        f"The logarithm of {m} to the {base} base",
        f"The logarithm of {m} having base {base}",
        f"log_{base}({m}) is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_logarithm_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
