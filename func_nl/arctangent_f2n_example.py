import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_arctangent_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##arctangent({x})",
                "outputStr": __random_explanation_arctangent(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_arctangent(x: float, identifier: int | None) -> str:
    explanations = [
        f"The arctangent of {x}",
        f"arctan({x})",
        f"The angle whose tangent is {x}",
        f"Calculation: arctan({x})",
        f"The inverse tangent function applied to {x}",
        f"The arctangent value for {x} is",
        f"The angle whose tangent is equal to {x}",
        f"The trigonometric function that gives the angle whose tangent is {x}",
        f"The inverse of the tangent function for the value {x}",
        f"The result of applying the arctangent function to {x}",
        f"The angle in degrees with tangent value {x}",
        f"The angle whose tangent value is {x} degrees",
        f"The value of the inverse tangent function for {x}",
        f"The angle that corresponds to a tangent of {x}",
        f"The angle whose tangent equals {x}",
        f"The angle for which tan(angle) = {x}",
        f"The angle in radians such that tan(angle) = {x}",
        f"The angle for which the tangent value is {x}",
        f"The angle whose tangent is given by {x}",
        f"The angle for which tan(angle) is {x}",
        f"The angle whose tangent is represented by {x}",
        f"The angle whose tangent is expressed as {x}",
        f"The angle whose tangent yields {x}",
        f"The angle in degrees such that tan(angle) = {x}",
        f"The inverse tangent function output for {x}",
        f"The value of the arctangent function at {x}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_arctangent_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
