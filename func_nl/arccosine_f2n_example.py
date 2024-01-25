import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_arccosine_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = random.uniform(-1.0, 1.0)
        examples.append(
            {
                "inputStr": f"##arccosine({x})",
                "outputStr": __random_explanation_arccosine(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_arccosine(x: float, identifier: int | None) -> str:
    explanations = [
        f"The arccosine of {x}",
        f"arccos({x})",
        f"The angle whose cosine is {x}",
        f"Calculation: arccos({x})",
        f"The inverse cosine function applied to {x}",
        f"The arccosine value for {x} is",
        f"The angle whose cosine is equal to {x}",
        f"The trigonometric function that gives the angle whose cosine is {x}",
        f"The inverse of the cosine function for the value {x}",
        f"The result of applying the arccosine function to {x}",
        f"The angle in degrees with cosine value {x}",
        f"The angle whose cosine value is {x} degrees",
        f"The value of the inverse cosine function for {x}",
        f"The angle that corresponds to a cosine of {x}",
        f"The angle whose cosine equals {x}",
        f"The angle for which cos(angle) = {x}",
        f"The angle in radians such that cos(angle) = {x}",
        f"The angle for which the cosine value is {x}",
        f"The angle whose cosine is given by {x}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_arccosine_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
