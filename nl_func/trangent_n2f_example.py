import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_tangent_example(count: int):
    examples = []
    for _ in range(count):
        angle = round(random.uniform(0, 360), 2)  # Random angle in degrees
        examples.append(
            {
                "inputStr": __random_explanation_tangent(angle),
                "outputStr": f"##tangent({angle})",
            }
        )
    return examples


def __random_explanation_tangent(angle: float) -> str:
    angle_degrees = round(angle, 2)  # Round the angle to two decimal places
    explanations = [
        f"Tangent of {angle_degrees} degrees",
        f"Tan({angle_degrees})",
        f"The tangent value for {angle_degrees} degrees",
        f"Calculate tangent for {angle_degrees} degrees",
        f"Tangent function applied to {angle_degrees}",
        f"Tangent of angle {angle_degrees}",
        f"Tangent({angle_degrees}), what is it?",
        f"The result of tan({angle_degrees})",
        f"Find the tangent of {angle_degrees} degrees",
        f"Tangent value when angle is {angle_degrees} degrees",
        f"Angle: {angle_degrees}, tangent?",
        f"Tangent of {angle_degrees}, tell me",
        f"Tan({angle_degrees}), the answer?",
        f"Calculate tan({angle_degrees})",
        f"The tangent for angle {angle_degrees}",
        f"What is tan({angle_degrees})?",
        f"Tangent of {angle_degrees}, result?",
        f"Tan({angle_degrees}), find the value",
        f"The tangent value for angle {angle_degrees}",
        f"Tangent of angle {angle_degrees}, what does it give?",
        f"Find tan({angle_degrees})",
        f"Tangent function for angle {angle_degrees}",
        f"Tangent of {angle_degrees} degrees, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_tangent_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
