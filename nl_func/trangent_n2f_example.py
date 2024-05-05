import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_tangent_example(count: int, identifier: int | None, seed: int,):
    examples = []
    for i in range(count):
        angle = RandomValueGenerator.generate_random_float(0, 360, 1, seed=seed)
        examples.append(
            {
                "inputStr": __random_explanation_tangent(angle, (None if identifier is None else identifier+i)),
                "outputStr": f"##tangent({angle})",
            }
        )
    return examples


def __random_explanation_tangent(angle: float, identifier: int | None) -> str:
    angle_degrees = round(angle, 2)  # Round the angle to two decimal places
    explanations = [
        f"tangent value for {angle} degrees",
        f"tangent of {angle} degrees",
        f"tan of {angle} degrees",
        f"tangent({angle}) value",

        f"tangent of {angle_degrees} degrees",
        f"The tangent value for {angle_degrees} degrees",
        f"Calculate tangent for {angle_degrees} degrees",
        f"Tangent function applied to {angle_degrees}",
        f"Tangent of angle {angle_degrees}",
        f"The result of tan({angle_degrees})",
        f"Find the tangent of {angle_degrees} degrees",
        f"Tangent value when angle is {angle_degrees} degrees",
        f"Tangent of {angle_degrees}, tell me",
        f"The tangent for angle {angle_degrees}",
        f"What is tan({angle_degrees})",
        f"Tangent of {angle_degrees}, result",
        f"The tangent value for angle {angle_degrees}",
        f"Tangent of angle {angle_degrees}, what does it give",
        f"Tangent function for angle {angle_degrees}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_tangent_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
