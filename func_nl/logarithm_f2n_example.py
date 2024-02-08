import random
import math

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_logarithm_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        m = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        base = RandomValueGenerator.generate_random_float(2.0, 10.0, seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": f"##logarithm({m},{base})",
                "outputStr": __random_explanation_log(
                    m,
                    base,
                    (None if identifier is None else identifier+i)
                ),
            }
        )
    return examples


def __random_explanation_log(m: float, base: float, identifier: int | None) -> str:
    explanations = [
        f"The logarithm of {m} to the base {base}",
        f"The result of taking the logarithm of {m} to the base {base}",
        f"The logarithm of {m} with base {base} is",
        f"The power to which {base} must be raised to get {m}",
        f"The logarithm of {m} with base {base} equals",
        f"The exponent that produces {m} when {base} is raised to it",
        f"The logarithm with base {base} of {m}",
        f"The logarithm of {m} to the {base} base",
        f"The logarithm of {m} having base {base}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_logarithm_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
