import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_degrees_to_radians_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        degrees = RandomValueGenerator.generate_random_float(0.0, 360.0, round_to=1)
        examples.append({
            "inputStr": __random_explanation(degrees, (None if identifier is None else identifier+i)),
            "outputStr": f"##degrees_to_radians({degrees})",
        })
    return examples


def __random_explanation(degrees: float, identifier: int | None) -> str:
    explanations = [
        f"Converting {degrees} degrees to radians",
        f"{degrees} degrees in radians",
        f"Transform {degrees} degrees to radians",
        f"The result of converting {degrees} degrees to radians",
        f"{degrees} degrees as radians",
        f"Radians equivalent of {degrees} degrees",
        f"Convert {degrees} degrees to radians",
        f"{degrees} degrees represented in radians",
        f"{degrees} degrees, what is it in radians",
        f"Calculation: {degrees} degrees to radians",
        f"{degrees} degrees in radians, what does it give",
        f"{degrees} degrees to radians, find the result",
        f"Radians: {degrees} degrees",
        f"Let's convert {degrees} degrees to radians",
        f"Find the radians for {degrees} degrees",
        f"{degrees} degrees, its radians",
        f"{degrees} degrees in radians, result is",
        f"Convert {degrees} degrees into radians",
        f"The radians when you have {degrees} degrees",
        f"{degrees} degrees to radians, find the answer",
        f"Transformation: {degrees} degrees to radians",
        f"{degrees} degrees represented as radians",
        f"The radians for {degrees} degrees, what is it",
        f"Convert {degrees} degrees to radians and tell the result",
        f"Let's find the radians for {degrees} degrees",
        f"{degrees} degrees, what will be its radians",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_degrees_to_radians_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
