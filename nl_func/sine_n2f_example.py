import random
import math

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_n2f_sine_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        angle_degrees = round(random.uniform(0, 360), 1)
        examples.append(
            {
                "inputStr": __random_explanation(angle_degrees, (None if identifier is None else identifier+i)),
                "outputStr": f"##sine({angle_degrees})",
            }
        )
    return examples


def __random_explanation(angle_degrees: float, identifier: int | None) -> str:
    explanations = [
        f"The sine of {angle_degrees} degrees",
        f"Sine of {angle_degrees}°",
        f"Sine value for angle {angle_degrees}°",
        f"The value of sin({angle_degrees}°)",
        f"Calculate the sine of {angle_degrees}°",
        f"The result of sine {angle_degrees} degrees",
        f"The trigonometric function sine for {angle_degrees}°",
        f"Sine of {angle_degrees}°, equals",
        f"The sine value for the angle {angle_degrees}°",
        f"The sine of {angle_degrees}°, what is it",
        f"Sine calculation: sin({angle_degrees}°)",
        f"The sine of {angle_degrees}°, the answer",
        f"The sine of {angle_degrees}°, find it",
        f"The value of sine of {angle_degrees} degrees",
        f"Let's find the sine of {angle_degrees}°",
        f"Sine value calculation: sin({angle_degrees}°)",
        f"Find the value of sin({angle_degrees}°)",
        f"The sine of {angle_degrees}°, the outcome",
        f"Sine of {angle_degrees}°, what will you get",
        f"Sine calculation: sin({angle_degrees}°), what is it",
        f"The sine value for the angle {angle_degrees}°, result",
        f"The value of sine for the angle {angle_degrees}°",
        f"Sine of {angle_degrees}°, the value",
        f"Sine value for {angle_degrees}°, result is",
        f"Sine of {angle_degrees}°, in trigonometry",
        f"The outcome of calculating sin({angle_degrees}°)",
        f"The value of sin({angle_degrees}°), the result",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_sine_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
