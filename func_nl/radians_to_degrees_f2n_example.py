import random
import math

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_radians_to_degrees_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(0.0, 2 * math.pi)
        examples.append(
            {
                "inputStr": f"##radians_to_degrees({x})",
                "outputStr": __random_explanation_radians_to_degrees(x),
            }
        )
    return examples


def __random_explanation_radians_to_degrees(x: float) -> str:
    explanations = [
        f"Convert {x} radians to degrees",
        f"radians_to_degrees({x})",
        f"The value of {x} radians in degrees",
        f"Calculation: radians_to_degrees({x})",
        f"The equivalent degrees for {x} radians",
        f"Converting {x} radians to degrees",
        f"The degree measure for {x} radians",
        f"The degree value corresponding to {x} radians",
        f"The angle conversion from radians to degrees for {x}",
        f"The value of degrees after converting {x} radians",
        f"The result of converting {x} radians to degrees",
        f"The degree measure for the input angle {x}",
        f"The degree value for the angle {x} radians",
        f"The angle {x} radians in degrees",
        f"The equivalent degree value for {x} radians",
        f"The degree equivalent of {x} radians",
        f"The degree measurement for the angle {x}",
        f"The angle in degrees corresponding to {x} radians",
        f"The degree value for the input angle of {x} radians",
        f"The degree representation of {x} radians",
        f"The angle conversion from radians to degrees yields",
        f"The degree value of {x} radians",
        f"The value of degrees after converting {x} radians is",
        f"The degree equivalent for the angle {x} radians",
        f"The result of converting {x} radians to degrees is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_radians_to_degrees_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
