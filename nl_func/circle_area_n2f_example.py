import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_circle_area_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        radius = RandomValueGenerator.generate_random_float()
        examples.append({
            "inputStr": __random_explanation(radius, (None if identifier is None else identifier+i)),
            "outputStr": f"##circle_area({radius})",
        })
    return examples


def __random_explanation(f1: float, identifier: int | None) -> str:
    explanations = [
        f"Calculate the area of a circle with radius {f1}",
        f"Determine the area of a circle with radius {f1}",
        f"Find the area of a circle with radius {f1}",
        f"The result of calculating the area of a circle with radius {f1}",
        f"Performing the circle area calculation for the radius {f1}",
        f"The area of a circle with radius {f1}",
        f"The result after calculating the area of a circle with radius {f1}, what is it",
        f"The area of a circle with radius {f1}, what does it give",
        f"Let's calculate the area of a circle with radius {f1}",
        f"The area of a circle with radius {f1}, result is",
        f"Calculating the area of a circle with radius {f1}",
        f"The area result after calculating the area of a circle with radius {f1}",
        f"The area of a circle with radius {f1}, what is its value",
        f"Let's determine the area of a circle with radius {f1}",
        f"The area of a circle with radius {f1}, what is the result",
        f"The area of a circle with radius {f1}, ignoring order",
        f"The result after calculating the area of a circle with radius {f1}",
        f"The area of a circle with radius {f1}, what is it",
        f"Calculate the area of a circle with radius {f1}, find the answer",
        f"The area of a circle with radius {f1}, what does it give",
        f"Let's find the result after calculating the area of a circle with radius {f1}",
        f"The area of a circle with radius {f1}, what is the output",
        f"The result after calculating the area of a circle with radius {f1}, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_circle_area_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
