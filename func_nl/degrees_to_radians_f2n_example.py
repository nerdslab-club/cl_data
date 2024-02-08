import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_degrees_to_radians_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float(0.0, 360.0, seed=(None if identifier is None else identifier+i))
        examples.append(
            {
                "inputStr": f"##degrees_to_radians({x})",
                "outputStr": __random_explanation_degrees_to_radians(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_degrees_to_radians(x: float, identifier: int | None) -> str:
    explanations = [
        f"Convert {x} degrees to radians",
        f"The value of {x} degrees in radians",
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
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_degrees_to_radians_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
