import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_tangent_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        angle = RandomValueGenerator.generate_random_float(0.0, 360.0, seed=(None if identifier is None else identifier+i))
        examples.append(
            {
                "inputStr": f"##tangent({angle})",
                "outputStr": __random_explanation_tangent(angle, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_tangent(angle: float, identifier: int | None) -> str:
    explanations = [
        f"The tangent of {angle} degrees",
        f"The result of taking the tangent of {angle} degrees",
        f"The tangent value of {angle} degree is",
        f"The trigonometric tangent function applied to {angle} degree",
        f"The tangent of the angle {angle} degree",
        f"The tangent function output for {angle} degree",
        f"The tangent of {angle} degrees is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_tangent_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
