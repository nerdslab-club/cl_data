import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_circle_area_example(count: int):
    examples = []
    for _ in range(count):
        radius = RandomValueGenerator.generate_random_float(1.0, 10.0)
        examples.append({
            "inputStr": __random_explanation(radius),
            "outputStr": f"##circle_area({radius})",
        })
    return examples


def __random_explanation(radius: float) -> str:
    explanations = [
        f"Calculate the area of a circle with radius {radius}",
        f"CIRCLE_AREA({radius})",
        f"Determine the area of a circle with radius {radius}",
        f"Find the area of a circle with radius {radius}",
        f"The result of calculating the area of a circle with radius {radius}",
        f"Performing the circle area calculation for the radius {radius}",
        f"The area of a circle with radius {radius}",
        f"CIRCLE_AREA calculation: {radius}",
        f"The result after calculating the area of a circle with radius {radius}, what is it?",
        f"The area of a circle with radius {radius}, what does it give?",
        f"Let's calculate the area of a circle with radius {radius}",
        f"The area of a circle with radius {radius}, result is",
        f"Calculating the area of a circle with radius {radius}",
        f"The area result after calculating the area of a circle with radius {radius}",
        f"The area of a circle with radius {radius}, what is its value?",
        f"Let's determine the area of a circle with radius {radius}",
        f"The area of a circle with radius {radius}",
        f"The area of a circle with radius {radius}, what is the result?",
        f"The area of a circle with radius {radius}, what does it give?",
        f"The area of a circle with radius {radius} and provide the result",
        f"CIRCLE_AREA({radius}), what does it yield?",
        f"The area of a circle with radius {radius}, ignoring order",
        f"The result after calculating the area of a circle with radius {radius}",
        f"The area of a circle with radius {radius}, what is it?",
        f"Calculate the area of a circle with radius {radius}, find the answer",
        f"The area of a circle with radius {radius}, what does it give?",
        f"Let's find the result after calculating the area of a circle with radius {radius}",
        f"The area of a circle with radius {radius}, what is the output?",
        f"The result after calculating the area of a circle with radius {radius}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_circle_area_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
