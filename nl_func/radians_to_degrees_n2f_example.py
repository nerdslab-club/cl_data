import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_radians_to_degrees_example(count: int):
    examples = []
    for _ in range(count):
        radians = RandomValueGenerator.generate_random_float(0.0, 2 * 3.14159)
        examples.append({
            "inputStr": __random_explanation(radians),
            "outputStr": f"##radians_to_degrees({radians})",
        })
    return examples


def __random_explanation(radians: float) -> str:
    explanations = [
        f"Converting {radians} radians to degrees",
        f"{radians} radians in degrees",
        f"Transform {radians} radians to degrees",
        f"The result of converting {radians} radians to degrees",
        f"{radians} radians as degrees",
        f"Degrees equivalent of {radians} radians",
        f"Convert {radians} radians to degrees",
        f"{radians} radians represented in degrees",
        f"{radians} radians, what is it in degrees?",
        f"Calculation: {radians} radians to degrees",
        f"{radians} radians in degrees, what does it give?",
        f"{radians} radians to degrees, find the result",
        f"Degrees: {radians} radians",
        f"Let's convert {radians} radians to degrees",
        f"Find the degrees for {radians} radians",
        f"{radians} radians, its degrees?",
        f"{radians} radians in degrees, result is",
        f"Convert {radians} radians into degrees",
        f"The degrees when you have {radians} radians",
        f"{radians} radians to degrees, find the answer",
        f"Transformation: {radians} radians to degrees",
        f"{radians} radians represented as degrees",
        f"The degrees for {radians} radians, what is it?",
        f"Convert {radians} radians to degrees and tell the result",
        f"Let's find the degrees for {radians} radians",
        f"{radians} radians, what will be its degrees?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_radians_to_degrees_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
