import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_sine_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        angle = RandomValueGenerator.generate_random_float(0.0, 360.0, seed=(None if identifier is None else identifier+i))
        examples.append(
            {
                "inputStr": f"##sine({angle})",
                "outputStr": __random_explanation_sine(
                    angle,
                    (None if identifier is None else identifier+i)
                ),
            }
        )
    return examples


def __random_explanation_sine(angle: float, identifier: int | None) -> str:
    explanations = [
        f"The sine of {angle} degrees",
        f"sin({angle})",
        f"The result of taking the sine of {angle} degrees",
        f"Calculation: sin({angle} degree)",
        f"The sine value of {angle} degree is",
        f"The value of sin({angle} degree)",
        f"The trigonometric sine function applied to {angle} degree",
        f"The sine of the angle {angle} degree",
        f"The sine function output for {angle} degree",
        f"The sine of {angle} degrees is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_sine_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
