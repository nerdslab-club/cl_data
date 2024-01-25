import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_arcsine_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = random.uniform(-1.0, 1.0)
        examples.append(
            {
                "inputStr": f"##arcsine({x})",
                "outputStr": __random_explanation_arcsine(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_arcsine(x: float, identifier: int | None) -> str:
    explanations = [
        f"The arcsine of {x}",
        f"arcsine({x})",
        f"The angle whose sine is {x}",
        f"Calculation: arcsine({x})",
        f"The inverse sine function applied to {x}",
        f"The arcsine value for {x} is",
        f"The angle whose sine is equal to {x}",
        f"The trigonometric function that gives the angle whose sine is {x}",
        f"The inverse of the sine function for the value {x}",
        f"The result of applying the arcsine function to {x}",
        f"The angle in degrees with sine value {x}",
        f"The angle whose sine value is {x} degrees",
        f"The value of the inverse sine function for {x}",
        f"The angle that corresponds to a sine of {x}",
        f"The angle whose sine equals {x}",
        f"The angle for which sin(angle) = {x}",
        f"The angle in radians such that sin(angle) = {x}",
        f"The angle for which the sine value is {x}",
        f"The angle whose sine is given by {x}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_arcsine_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
