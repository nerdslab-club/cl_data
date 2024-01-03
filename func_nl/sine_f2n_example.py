import random
import math

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_sine_example(count: int):
    examples = []
    for _ in range(count):
        angle = random.uniform(0.0, 360.0)
        examples.append(
            {
                "inputStr": f"##sine({angle})",
                "outputStr": __random_explanation_sine(
                    angle,
                ),
            }
        )
    return examples


def __random_explanation_sine(angle: float) -> str:
    radians = math.radians(angle)
    sine_value = round(math.sin(radians), 4)

    explanations = [
        f"The sine of {angle} degrees",
        f"sin({angle})",
        f"The result of taking the sine of {angle} degrees",
        f"Calculation: sin({angle} °)",
        f"The sine value of {angle} ° is",
        f"The value of sin({angle} °)",
        f"The trigonometric sine function applied to {angle} °",
        f"The sine of {angle} ° equals?",
        f"The sine of the angle {angle} °",
        f"The sine function output for {angle} °",
        f"The sine of {angle} degrees is",
    ]

    return f"{random.choice(explanations)} {sine_value}"


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_sine_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
