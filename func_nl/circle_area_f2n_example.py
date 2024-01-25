import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_circle_area_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        radius = random.uniform(1.0, 50.0)
        examples.append(
            {
                "inputStr": f"##circle_area({radius})",
                "outputStr": __random_explanation_circle_area(radius, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_circle_area(radius: float, identifier: int | None) -> str:
    explanations = [
        f"The area of a circle with radius {radius}",
        f"circle_area({radius})",
        f"The result of calculating the area of a circle with radius {radius}",
        f"Calculation: circle_area({radius})",
        f"The area enclosed by a circle with radius {radius}",
        f"The outcome of finding the area of a circle with radius {radius}",
        f"The region covered by a circle with radius {radius}",
        f"The result of determining the circle area with radius {radius}",
        f"The computed result of calculating the area of a circle with radius {radius}",
        f"The space inside a circle with radius {radius}",
        f"The outcome of evaluating circle_area({radius})",
        f"The value obtained by finding the area of a circle with radius {radius}",
        f"The result of evaluating circle_area({radius})",
        f"The region bounded by a circle with radius {radius}",
        f"The computed area of a circle with radius {radius}",
        f"The region surrounded by a circle with radius {radius}",
        f"The calculated result of determining the circle area with radius {radius}",
        f"The area covered by a circle with radius {radius}",
        f"The result obtained from calculating the area of a circle with radius {radius}",
        f"The computed circle area with radius {radius}",
        f"The area within the boundary of a circle with radius {radius}",
        f"The calculated outcome of evaluating circle_area({radius})",
        f"The space enclosed by a circle with radius {radius}",
        f"The computed circle area value for a circle with radius {radius}",
        f"The calculated area of a circle with radius {radius}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_circle_area_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
