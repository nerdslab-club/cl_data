import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_degrees_to_radians_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(0.0, 360.0)
        examples.append(
            {
                "inputStr": f"##degrees_to_radians({x})",
                "outputStr": __random_explanation_degrees_to_radians(x),
            }
        )
    return examples


def __random_explanation_degrees_to_radians(x: float) -> str:
    explanations = [
        f"Convert {x} degrees to radians",
        f"degrees_to_radians({x})",
        f"The value of {x} degrees in radians",
        f"Calculation: degrees_to_radians({x})",
        f"The equivalent radians for {x} degrees",
        f"Converting {x} degrees to radians",
        f"The radian measure for {x} degrees",
        f"The radian value corresponding to {x} degrees",
        f"The angle conversion from degrees to radians for {x}",
        f"The value of radians after converting {x} degrees",
        f"The result of converting {x} degrees to radians",
        f"The radian measure for the input angle {x}",
        f"The radian value for the angle {x} degrees",
        f"The angle {x} degrees in radians",
        f"The equivalent radian value for {x} degrees",
        f"The radian equivalent of {x} degrees",
        f"The radian measurement for the angle {x}",
        f"The angle in radians corresponding to {x} degrees",
        f"The radian value for the input angle of {x} degrees",
        f"The radian representation of {x} degrees",
        f"The radian value of {x} degrees",
        f"The value of radians after converting {x} degrees is",
        f"The radian equivalent for the angle {x} degrees",
        f"The result of converting {x} degrees to radians is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_degrees_to_radians_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
