import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_tangent_example(count: int):
    examples = []
    for _ in range(count):
        angle = random.uniform(0.0, 360.0)
        examples.append(
            {
                "inputStr": f"##tangent({angle})",
                "outputStr": __random_explanation_tangent(angle),
            }
        )
    return examples


def __random_explanation_tangent(angle: float) -> str:
    explanations = [
        f"The tangent of {angle} degrees",
        f"tan({angle} °)",
        f"The result of taking the tangent of {angle} degrees",
        f"Calculation: tan({angle} °)",
        f"The tangent value of {angle}° is",
        f"The value of tan({angle} °)",
        f"The trigonometric tangent function applied to {angle} °",
        f"The tangent of {angle} ° equals?",
        f"The ratio of the length of the side opposite the angle to the length of the adjacent side",
        f"The tangent of the angle {angle} °",
        f"The tangent function output for {angle} °",
        f"The tangent of {angle} degrees is",
        f"The slope of the line passing through the origin and the point on the unit circle",
        f"The vertical displacement of a point on the unit circle from the origin",
        f"The value of the trigonometric function that relates to the angle {angle} °",
        f"The result of dividing the sine of the angle by the cosine of the angle",
        f"The tangent of an angle can be written as sin({angle} °) / cos({angle} °)",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_tangent_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
